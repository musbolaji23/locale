from http import HTTPStatus
from flask_restx import Namespace, Resource, fields
from werkzeug.exceptions import NotFound
from ..models.state import State
from ..models.lga import Lga
from ..utils.apirequired import api_key_required

state_namespace = Namespace('state', description='name space for state')

state_model = state_namespace.model(
    'State', {
    'id': fields.Integer(),
    'region_id': fields.Integer(),
    'name': fields.String(required=True, description="name of statr"),
    'capital': fields.String(),
    'governor': fields.String(),
    'slogan': fields.String(),
    'no_of_lgas': fields.Integer()
}
)   

get_one_state_model = state_namespace.model(
    'GetOneState', {
    'state_name': fields.String(required=True, description="name of state")
    }
)   


lga_model = state_namespace.model(
    'Lga', {
    'id': fields.Integer(),
    'region_id': fields.Integer(),
    'state_id': fields.Integer(),
    'name': fields.String(required=True, description="name of lga"),
}
)  

error_model = state_namespace.model(
    'ErrorModel', {
    'message': fields.String(required=True, description="name of state")
    }
)   


@state_namespace.route('/')
class GetAllState(Resource):
    @api_key_required
    @state_namespace.marshal_with(state_model)
    def get(self):
        states = State.query.all()
        return states, HTTPStatus.OK
    

@state_namespace.route('/<string:state_name>')
class GetOneState(Resource):
    @state_namespace.expect(get_one_state_model)
    @state_namespace.marshal_with(state_model)
    def get(self, state_name):
        state = State.query.filter_by(name=state_name).first()

        if not state:
            return {"message": "State not found"}, 404

        return state, HTTPStatus.OK

@state_namespace.route('/<string:state_name>/lgas')
class GetAllLgasInState(Resource):
    @state_namespace.expect(get_one_state_model)
    @state_namespace.marshal_with(lga_model)
    def get(self, state_name):
        state = State.query.filter_by(name=state_name).first()

        if not state:
            raise NotFound("Cannot fetch LGAs, State not found")
                
        lgas = Lga.query.filter_by(state_id=state.id).all()

        return lgas, HTTPStatus.OK