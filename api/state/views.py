from flask_restx import Namespace, Resource

state_namespace = Namespace('state', description='name space for state')

@state_namespace.route('/')
class HelloState(Resource):
    def get(self):
        return {'message': 'Hello Region nice to see you '}