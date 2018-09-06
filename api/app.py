""" initializes the app , holds blue prints and routes"""
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from api.views.questions import QUESTIONS, Qusetion, Questions
from api.views.answers import ANSWERS, Answer, Answers, Ans
from api.users.users import USER, User, UserLogin, GetUserRequests

CONNECT_CREDS = {
    "host": os.getenv('DB_HOST'),
    "database": os.getenv('DB_NAME'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD')
}
DATABASE_URL = os.getenv('DATABASE_URL')

def connectTODB():
    try:
        print("connecting to database ...")
        try:
            return psycopg2.connect(DATABASE_URL)
        except:
            return psycopg2.connect(**CONNECT_CREDS)
    except:
        print("Connection to database failed!")

APP = Flask(__name__)
API = Api(APP)
jwt = JWTManager(APP)
APP.config['JWT_SECRET_KEY'] = 'raiseSONDecodeErrorExpectingromNone' 
APP.register_blueprint(QUESTIONS)
APP.register_blueprint(ANSWERS)
APP.register_blueprint(USER)
API.add_resource(Questions, '/api/v1/questions/')
API.add_resource(Qusetion, '/api/v1/questions/<int:question_id>/')
API.add_resource(Ans, '/api/v1/answers/')
API.add_resource(Answers, '/api/v1/answers/<int:question_id>/')
API.add_resource(Answer, '/api/v1/answers/<int:question_id>/<int:answer_id>/')
API.add_resource(User, '/api/v1/auth/signup/')
API.add_resource(UserLogin, '/api/v1/auth/login/')
API.add_resource(GetUserRequests, '/api/v1/auth/requests/<int:user_id>')


