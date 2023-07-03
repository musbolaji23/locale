from flask_restx import Namespace, Resource, fields
from flask import request, json
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
import secrets

user_namespace = Namespace('region', description='name space for user')

user_model = user_namespace.model(
    'user', {
    'id': fields.Integer(),
    'name': fields.String(required=True, description="name of user"),
    'email': fields.String(required=True, description="email of user"),
    'password': fields.String(required=True, description="password of user"),
    'api_key': fields.String(required=True, description="api_key of user")
    }
)   

signup_model = user_namespace.model(
    'User', {
    'id': fields.Integer(),
    'name': fields.String(required=True, description="A firstname"),
    'email': fields.String(required=True, description="An email"),
    'password': fields.String(required=True, description="A password")
    }
)    

login_model = user_namespace.model(
    'login', {
    'email': fields.String(required=True, description="An email"),
    'password': fields.String(required=True, description="A password")
    }
)

@user_namespace.route('/signup')
class Signup(Resource):

    @user_namespace.expect(signup_model)
    @user_namespace.marshal_with(user_model)
    def post(self):
        """
            Sign up a user
        """
        data = request.get_json()
        
        new_user = User(
            name = data.get('name'),
            email = data.get('email'),
            password = generate_password_hash(data.get('password')),
            api_key = secrets.token_urlsafe(20)
        )
        
        new_user.save()

        return new_user, HTTPStatus.CREATED

@user_namespace.route('/login')
class Login(Resource):

    def post(self):
        """
            Generate JWT Token
        """

        data = request.get_json()

        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if (user is not None) and check_password_hash(user.password_hash, password):

            access_token = create_access_token(identity=user.user_id)
            refresh_token = create_refresh_token(identity=user.user_id)

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }

            return response, HTTPStatus.CREATED
