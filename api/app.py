""" initializes the app , holds blue prints and routes"""
from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from api.views.questions import QUESTIONS, Qusetion, Questions


APP = Flask(__name__)
API = Api(APP)
SWAGGER = Swagger(APP)
APP.register_blueprint(QUESTIONS)
API.add_resource(Questions, '/api/v1/questions/')
API.add_resource(Qusetion, '/api/v1/questions/<int:question_id>')
