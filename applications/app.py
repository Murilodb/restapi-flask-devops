from flask import Flask, jsonify
from flask_restful import Resource, reqparse
from flask_mongoengine import MongoEngine
from mongoengine import NotUniqueError
from validate_docbr import CPF
from .model import UserModel


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name', type=str, required=True, help="First name is required")
_user_parser.add_argument('last_name', type=str, required=True, help="Last name is required")
_user_parser.add_argument('email', type=str, required=True, help="Email is required")
_user_parser.add_argument('cpf', type=str, required=True, help="CPF is required")
_user_parser.add_argument('birth_date', type=str, required=True, help="Birth date is required")





cpf_validator = CPF()





class Users(Resource):
    def get(self):
        return jsonify(UserModel.objects())


class User(Resource):
    def post(self):

        data = _user_parser.parse_args()

        if not cpf_validator.validate(data['cpf']):
            return {'message': 'Invalid CPF'}, 400

        try:
            UserModel(**data).save()
            return {'message': 'User created successfully'}, 200
        except NotUniqueError:
            return {'message': 'User with this CPF already exists'}, 400

    def get(self, cpf):

        response = (UserModel.objects(cpf=cpf))
        if response:
            return jsonify(response)
        
        return {'message': 'User not found in database'}, 404





