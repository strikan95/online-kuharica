from typing import get_args
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity, jwt_required

from . import api
from ..models.users import User
from .auth.util import hash_password
from .auth.token import TokenResource

class UserListResource(Resource):
    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')

        if User.get_by_username(username):
            return {'message': 'Username already used'}, HTTPStatus.BAD_REQUEST

            
        if User.get_by_email(email):
            return {'message': 'Email already used'}, HTTPStatus.BAD_REQUEST

        #TODO Hash password
        password = hash_password(non_hash_password)

        user = User(
            username = username,
            email = email,
            password = password
        )

        user.save()

        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        
        return data, HTTPStatus.CREATED

class UserResource(Resource):
    @jwt_required(optional=True)
    def get(self, username):
        user = User.get_by_username(username = username)

        if user is None:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        current_user = get_jwt_identity()

        if current_user == user.id:
            data = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        else:
            data = {
                'id': user.id,
                'username': user.username,
            }
        
        return data, HTTPStatus.OK

class MeResource(Resource):
    @jwt_required(optional=False)
    def get(self):
        user = User.get_by_id(id = get_jwt_identity())
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        return data, HTTPStatus.OK

api.add_resource(UserListResource, '/users')
api.add_resource(UserResource, '/users/<string:username>')
api.add_resource(TokenResource, '/token')
api.add_resource(MeResource, '/me')