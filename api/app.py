""" initializes the app , holds blue prints and routes"""
from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from api.views.questions import QUESTIONS, Qusetion, Questions


app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)
app.register_blueprint(QUESTIONS)
api.add_resource(Questions, '/api/v1/questions/')
api.add_resource(Qusetion, '/api/v1/questions/<int:question_id>')
