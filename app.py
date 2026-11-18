from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine


app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
    "host": "mongo",
    "port": 27017,
    "username": "admin",
    "password": "admin"

}
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('first_name', type=str, required=True, help="First name is required")
_user_parser.add_argument('last_name', type=str, required=True, help="Last name is required")
_user_parser.add_argument('email', type=str, required=True, help="Email is required")
_user_parser.add_argument('cpf', type=str, required=True, help="CPF is required")
_user_parser.add_argument('birth_date', type=str, required=True, help="Birth date is required")


api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True, max_length=50)
    last_name = db.StringField(required=True, max_length=50)
    birth_date = db.DateField(required=True)


class Users(Resource):
    def get(self):
        return {'message': 'User 1'}


class User(Resource):
    def post(self):

        data = _user_parser.parse_args()

        UserModel(**data).save()
        return {'message': 'User created successfully'}, 200

    def get(self, cpf):
        return {'message': f'User with CPF: {cpf}'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
