""" defines CRUD methods for questions """
import datetime
from flask import Blueprint, jsonify, request
from flask_restful import reqparse, Resource
from api.resources.resources import QUESTION_DICT


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
    def post(self):
        """
        Posts a new question.
        ---
        """
        if 'title' in request.json and not request.json['title']:
            return {"message": "Questions need a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400

        title, body, question_id = (request.json['title'],
                                    request.json['body'],
                                    request.json['question_id'])
        single_questn = {
            'question_id': question_id,
            "title": title,
            "body": body,
            "date_created": str(datetime.datetime.now()),
            "date_modified": str(datetime.datetime.now()),
            "upvotes": 0,
            "downvotes": 0,
            "answers": 0,
        }
        QUESTION_DICT.append(single_questn)
        return jsonify({"message": "Question posted successfully!"},
                       {"sigle_qn": single_questn})
    def get(self):
        """get all questsions"""
        return jsonify({"message": "all questions found successfully"}, {"questions": QUESTION_DICT})


class Qusetion(Resource):
    """methods for single questions"""
    def get(self, question_id):
        """"
        Gets a question.
        ---
        """
        single_questn = [single_questn for single_questn in QUESTION_DICT if single_questn['question_id'] == question_id]
        if len(single_questn) == 0:
            return {"message": "Question does not exist"}, 404
        return jsonify({"message": "Question successfully retrieved"},
                       {"single_questn": single_questn})

    def put(self, question_id):
        """
        Modifies a question.
        ---
        """
        single_question = [single_question for single_question in QUESTION_DICT if single_question['question_id'] == question_id]
        if 'body' in request.json and not request.json['body']:
            return {"message": "body must be a string."}, 400
        single_question[0]['title'] = request.json.get('title', single_question[0]['title'])
        single_question[0]['body'] = request.json.get('body', single_question[0]['body'])
        single_question[0]['date_modified'] = str(datetime.datetime.now())
        return jsonify({"message": "Question successfully updated"},
                       {"single_questn": single_question})

    def delete(self, question_id):
        """
        deletes a question.
        ---
        
        """
        single_questn = [single_questn for single_questn in QUESTION_DICT if single_questn['question_id'] == question_id]
        QUESTION_DICT.remove(single_questn[0])
        return jsonify({"message":"Question successfuly deleted"})
