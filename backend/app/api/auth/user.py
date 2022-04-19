from os import access
from flask import request, jsonify, make_response
from flask_restful import Resource
from http import HTTPStatus
from flask_jwt_extended import (create_access_token, create_refresh_token,
    set_access_cookies, set_refresh_cookies, unset_jwt_cookies, get_jwt_identity,
    jwt_required)

from .. import api
from app.models.users import User
from .util import hash_password, check_password

## Authentication -> POST /api/v1/users/login
## Registration -> POST /api/v1/users

class UserRegisterResource(Resource):
    ## Registration
    def post(self):
        json_data = request.get_json()

        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')

        if (User.get_by_username(username) or 
                User.get_by_email(email)):
            return {'message': 'Username already used'}, HTTPStatus.BAD_REQUEST

            
        if User.get_by_email(email):
            return {'message': 'Email already used'}, HTTPStatus.BAD_REQUEST

        password = hash_password(non_hash_password)

        user = User(
            username = username,
            email = email,
            password = password
        )

        user.save()

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = jsonify({
            'message': 'Success. User registrated.',
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return make_response(response, HTTPStatus.CREATED)

class UserAuthResource(Resource):
    #Authentication
    def post(self):
        json_data = request.get_json()
        user_data = json_data.get("user")
        email = user_data['email']
        password = user_data['password']
        # email = json_data.get("email")
        # password = json_data.get("password")
        print("Auth: " + email + password)

        user = User.get_by_email(email=email)

        if not user or not check_password(password, user.password):
            return {'message' : 'Email or password is incorrect'}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        response = jsonify({
            'user':{
                'id': user.id,
                'username':user.username,
                'email': user.email
            }
        })

        set_access_cookies(response, access_token)
        set_refresh_cookies(response, refresh_token)

        return make_response(response, HTTPStatus.OK)

class UserLogoutResource(Resource):
    def post(self):
        response = jsonify({"message": "logged out"})
        unset_jwt_cookies(response)
        return make_response(response, HTTPStatus.OK)

class RefreshTokenResource(Resource):
    @jwt_required(refresh=True)
    def post(self):
        user_id = get_jwt_identity()
        user = User.get_by_id(id=user_id)
        access_token = create_access_token(identity=user_id)

        response = jsonify()
        set_access_cookies(response, access_token)

        return make_response(response, HTTPStatus.CREATED)


api.add_resource(UserRegisterResource, "/users/register")
api.add_resource(UserAuthResource, "/user/login")
api.add_resource(UserLogoutResource, "/user/logout")
api.add_resource(RefreshTokenResource, "/user/refresh")