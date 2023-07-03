from http import HTTPStatus
from flask_restx import Namespace, Resource, fields
from ..models.region import Region
from ..utils.apirequired import api_key_required

region_namespace = Namespace('region', description='name space for region')

region_model = region_namespace.model(
    'Region', {
    'id': fields.Integer(),
    'name': fields.String(required=True, description="name of region"),
    'no_of_states': fields.Integer()
    }
)   

get_one_region_model = region_namespace.model(
    'GetOneRegion', {
    'region_name': fields.String(required=True, description="name of region")
    }
)   



@region_namespace.route('/')
class GetAllRegion(Resource):
    @api_key_required
    @region_namespace.marshal_with(region_model)
    def get(self):
        regions = Region.query.all()
        return regions, HTTPStatus.OK
    

@region_namespace.route('/<string:region_name>')
class GetOneRegion(Resource):
    @region_namespace.expect(get_one_region_model)
    @region_namespace.marshal_with(region_model)
    def get(self, region_name):
        region = Region.query.filter_by(name=region_name).first()
        
        return region, HTTPStatus.OK