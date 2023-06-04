from flask_restx import Namespace, Resource

region_namespace = Namespace('region', description='name space for region')

@region_namespace.route('/')
class HelloRegion(Resource):
    def get(self):
        return {'message': 'Hello Region nice to see you '}