from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)

app.config['MONGODB_SETTINGS'] = {
    "db": "myapp",
    "host": "mongobd",
    "port": 27017,
    "username": "admin",
    "password": "admin"

}

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
        return {'message': 'teste'}

    def get(self, cpf):
        return {'message': f'User with CPF: {cpf}'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)