""" defines CRUD methods for answers """
import datetime
from flask import Blueprint, jsonify, request
from flask_restful import reqparse, Resource
from flask_jwt_extended import get_jwt_identity
from api.helpers.helper_answers import HelperDb


ANSWERS = Blueprint('answers', __name__,
                    url_prefix='/api/v1/answers/')

POST_PARSER = reqparse.RequestParser()
POST_PARSER.add_argument(
    'body', dest='body',
    type=str, location='form',
    required=True, help='The answer body',
)
class Ans(Resource):
    """ method for getting all answers"""
    def get(self):
        """ gets all answers"""
        return HelperDb().get_all_answers()


class Answers(Resource):
    """ methods for answers"""
    def post(self, question_id):
        """
        Posts a new answer.
        """
        if 'title' in request.json and not request.json['title']:
            return {"message": "Questions need a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400
        body, title, question_id = (request.json['body'],
                                    request.json['title'],
                                    request.json['question_id'])
        single_answer = {
            "question_id": question_id,
            "body": body,
            "title":title,
            "date_created": str(datetime.datetime.now()),
            "date_modified": str(datetime.datetime.now()),
            "upvotes": 0,
            "downvotes": 0,
            "status": "pending",
            "username": get_jwt_identity(),
        }
        return HelperDb().create_request(single_answer)
    def get(self,question_id):
        """get all answers to a question"""
        return HelperDb().get_answers(question_id)


class Answer(Resource):
    """methods for single answers"""
    def get(self, answer_id):
        """"
        Gets an answer.
        
        """
        return HelperDb().get_request(answer_id)

    def put(self,answer_id):
        """
        Modifies an answer.
        ---
        
        """
        if 'title' in request.json and not request.json['title']:
            return {"message": "Questions need a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400
        title, body = (request.json['title'],
                       request.json['body'])
        single_answer = {
            "body": body,
            "title":title,
            "date_created": str(datetime.datetime.now()),
            "date_modified": str(datetime.datetime.now()),
            "upvotes": 0,
            "downvotes": 0,
            "status": "pending",
        }
        return HelperDb().update_request(answer_id, single_answer)

    def delete(self, question_id, answer_id):
        """
        delete an answer.
        ---
        """
        return HelperDb().delete_request(answer_id)
