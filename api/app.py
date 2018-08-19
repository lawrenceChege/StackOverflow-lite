""" initializes the app , holds blue prints and routes"""
from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from api.views.questions import QUESTIONS, Qusetion, Questions
from api.views.answers import ANSWERS, Answer, Answers, Ans

APP = Flask(__name__)
API = Api(APP)
SWAGGER = Swagger(APP)
APP.register_blueprint(QUESTIONS)
APP.register_blueprint(ANSWERS)
API.add_resource(Questions, '/api/v1/questions/')
API.add_resource(Qusetion, '/api/v1/questions/<int:question_id>/')
API.add_resource(Ans, '/api/v1/answers/')
API.add_resource(Answers, '/api/v1/answers/<int:question_id>/')
API.add_resource(Answer, '/api/v1/answers/<int:question_id>/<int:answer_id>/')
