from flask_restx import Namespace, Resource

lga_namespace = Namespace('lga', description='name space for lga')

@lga_namespace.route('/')
class Hellolga(Resource):
    def get(self):
        return {'message': 'Hello lga nice to see you '} 