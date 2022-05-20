from cmath import log
from typing import get_args
from flask import request
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity, jwt_required

from .. import api
from app.models.users import User

## Get current user -> GET /api/v1/user
## Update user -> PUT /api/v1/user
## Get profile -> GET /api/v1/profiles/:username

class UserResource(Resource):
    ## FETCHING user data
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
    ## FETCHING self profile data
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.get_by_id(id=user_id)
        data = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }

        return data, HTTPStatus.OK
        # user = User.get_by_id(id = get_jwt_identity())
        # data = {
        #     'id': user.id,
        #     'username': user.username,
        #     'email': user.email
        # }
        
        #return data, HTTPStatus.OK

api.add_resource(UserResource, '/user/<string:username>')
api.add_resource(MeResource, '/me/')