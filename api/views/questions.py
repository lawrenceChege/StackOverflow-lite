""" defines CRUD methods for questions """
import datetime
from flask import Blueprint, jsonify, request
from flask_restful import reqparse, Resource
from api.helpers.helper_questions import HelperDb
from flask_jwt_extended import get_jwt_identity, jwt_required


QUESTIONS = Blueprint('questions', __name__,
                      url_prefix='/api/v1/questions/')

POST_PARSER = reqparse.RequestParser()
POST_PARSER.add_argument(
    'title', dest='title', type=str,
    location='form', required=True,
    help='The question title',
)
POST_PARSER.add_argument(
    'body', dest='body',
    type=str, location='form',
    required=True, help='The question body',
)

class Questions(Resource):
    """ methods for questions"""
    @jwt_required
    def post(self):
        """
        Posts a new question.
        ---
        """
        if 'title' in request.json and not request.json['title']:
            return {"message": "Questions need a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400
        title, body = (request.json['title'],
                        request.json['body'])
        current_user = get_jwt_identity()
        single_question = {
            "title": title,
            "body": body,
            "date_created": str(datetime.datetime.now()),
            "date_modified": str(datetime.datetime.now()),
            "upvotes": 0,
            "downvotes": 0,
            "answers": 0,
            "username":current_user,
        }
        return HelperDb().create_request(single_question)

    def get(self):
        """get all questsions"""
        return HelperDb().get_all_questions()

class Qusetion(Resource):
    """methods for single questions"""
    def get(self, question_id):
        """"
        Gets a question.
        ---
        """
        return HelperDb().get_request(question_id)
    @jwt_required
    def put(self, question_id):
        """
        Modifies a question.
        ---
        """
        if 'title' in request.json and not request.json['title']:
            return {"message": "Questions need a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400
        title, body = (request.json['title'],
                        request.json['body'])
        single_question = {
            "title": title,
            "body": body,
            "date_modified": str(datetime.datetime.now()),
        }
        return HelperDb().update_request(question_id, single_question)
    @jwt_required
    def delete(self, question_id):
        """
        deletes a question.
        ---
        """
        return HelperDb().delete_request(question_id)
