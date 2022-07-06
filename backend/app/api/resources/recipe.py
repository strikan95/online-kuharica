import http
from urllib import response
from flask import jsonify, make_response, request
from flask_restful import Resource
from http import HTTPStatus

from flask_jwt_extended import ( get_jwt_identity, jwt_required )

from sqlalchemy import true

from .. import api
from app.models.recipes import Recipe as RecipeModel


class Recipes(Resource):
    def get(self):
        #params = request.args

        recipes = RecipeModel.get_all_published()
        recipe_count = len(recipes)
        recipe_data = []

        for recipe in recipes:
            recipe_data.append(recipe.data())

        payload = {
            'recipes' : recipe_data,
            'recipe_count' : recipe_count
        }

        return make_response(payload, HTTPStatus.OK)

    @jwt_required(refresh=True)
    def post(self):
        received = request.get_json()
        data = received['recipe']
        user_id = get_jwt_identity()

        recipe = RecipeModel( name = data['name'],
                              description = data['description'],
                              num_of_servings = 1,
                              cook_time = 1,
                              directions = "",
                              user_id = user_id )
        recipe.is_publish = True
        recipe.save()

        payload = {
            'message' : 'recipe created',
            'recipe'  : recipe.data()
        }

        return make_response(payload, HTTPStatus.CREATED)


class Recipe(Resource):
    def get(self, recipe_id: int):

        recipe = RecipeModel.get_by_id(recipe_id)
        
        if(recipe != None):
            recipe_data = recipe.data()

            payload = {
                'recipe' : recipe_data
            }
        
            response = make_response(payload, HTTPStatus.OK)
        
        else:
            response = make_response({'message' : 'recipe not found'}, HTTPStatus.NOT_FOUND)

        return response
    
    @jwt_required(refresh=True)
    def put(self):
        pass

    @jwt_required(refresh=True)
    def delete(self, recipe_id: int):
        user_id = get_jwt_identity()
        recipe = RecipeModel.get_by_id(recipe_id)

        if (recipe.user_id != user_id):
            response = make_response({'message': "not authorized"}, HTTPStatus.UNAUTHORIZED)
        else:
            recipe.delete()
            response = make_response({'messsage' : "recipe deleted"}, HTTPStatus.OK)
        
        return response


# class RecipeListResource(Resource):
#     def get(self):
#         recipes = Recipe.get_all_published()
#         data = []
#         recipe_count = 0
#         for recipe in recipes:
#             data.append(recipe.data())
#             recipe_count += 1

#         return {'recipes' : data, 'recipesCount' : recipe_count}, HTTPStatus.OK

#     @jwt_required(refresh=True)
#     def post(self):
#         json_data = request.get_json()
#         user_id = get_jwt_identity()
#         recipe_name = json_data['payload']['name']
#         recipe_description = json_data['payload']['description']
#         print(recipe_description)

#         recipe = Recipe(name=recipe_name,
#                             description=recipe_description,
#                             num_of_servings=1,
#                             cook_time=1,
#                             directions="",
#                             user_id=user_id)
#         recipe.is_publish = True
#         recipe.save()

#         return make_response({"message": "recipe created"}, HTTPStatus.CREATED)

# class RecipeResource(Resource):
#     def get(self, recipe_id):

#         print(recipe_id)
#         recipe = Recipe.get_by_id(recipe_id)

#         # recipe = next((recipe for recipe in recipe_list if recipe.id ==
#         #     recipe_id and recipe.is_publish == True), None)

#         if recipe is None:
#             return {'message' : 'recipe not found'}, HTTPStatus.NOT_FOUND

#         return {'recipe': recipe.data()}, HTTPStatus.OK

#     def put(self, recipe_id):
#         data = request.get_json()

#         recipe = next((recipe for recipe in recipe_list if recipe.id ==
#             recipe_id), None)

#         if recipe is None:
#             return {'message' : 'recipe not found'}, HTTPStatus.NOT_FOUND

#         recipe.name = data['name']
#         recipe.description = data['description']
#         recipe.num_of_servings = data['num_of_servings']
#         recipe.cook_time = data['cook_time']
#         recipe.directions = data['directions']

#         return recipe.data, HTTPStatus.OK

#     def delete(self, recipe_id):
#         recipe = next((recipe for recipe in recipe_list if recipe.id ==
#             recipe_id), None)
        
#         if recipe is None:
#             return {'message': "Recipe not found"}, HTTPStatus.NOT_FOUND

#         recipe_list.remove(recipe)

#         return {}, HTTPStatus.NO_CONTENT

# class RecipePublishResource(Resource):
#     def put(self, recipe_id):
#         recipe = next((recipe for recipe in recipe_list if recipe.id ==
#             recipe_id), None)

#         if recipe is None:
#             return {'message' : 'recipe not found'}, HTTPStatus.NOT_FOUND

#         recipe.is_publish = True

#         return {}, HTTPStatus.NO_CONTENT

#     def delete(self, recipe_id):
#         recipe = next((recipe for recipe in recipe_list if recipe.id ==
#             recipe_id), None)
#         if recipe is None:
#             return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

#         recipe.is_publish = False

#         return {}, HTTPStatus.NO_CONTENT

# api.add_resource(RecipeListResource, '/recipes/')
# api.add_resource(RecipeResource, '/recipes/<int:recipe_id>')
# api.add_resource(RecipePublishResource, '/recipes/<int:recipe_id>/publish')

api.add_resource(Recipes, '/recipes/')
api.add_resource(Recipe, '/recipes/<int:recipe_id>')