""" defines CRUD methods for questions """
from flask import Blueprint, jsonify, request
from flask_restful import fields, marshal_with, reqparse, Resource
from app.helpers.resources import QNS


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
QUESTION_FIELDS = {
    "question_id": fields.Integer,
    "user_id": fields.Integer,
    "Title": fields.String,
    "Body": fields.String,
    "date_created": fields.DateTime,
    "date_modified": fields.DateTime,
    "upvotes": 3,
    "downvotes": 1,
    "answers": fields.Integer
}


class Questions(Resource):
    """ methods for questions"""
    @marshal_with(QUESTION_FIELDS)
    def post(self):
        """
        Posts a new question.
        ---
        tags:
            - New Question
        parameters:
        - in: formData
            name: title
            type: string
            required: true
        - in: formData
            name: body
            type: string
            required: true
        responses:
        200:
            description: The request was successful.
        201:
            description: New request created.
        400:
            description: Bad request made.
        401:
            description: Unauthorised access.
        404:
            description: Page not found.
        """
        if 'title' in request.json and not request.json['title']:
            return {"message": "Please enter a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "body must be a string."}, 400

        title, body, = request.json['title'], request.json['body']
        qns = [qns for qns in QNS if qns['question_id'] == 0]
        single_qn = {
            'question_id': qns['id'] + 1,
            "Title": title,
            "Body": body,
            "date_created": fields.DateTime,
            "date_modified": fields.DateTime,
            "upvotes": 0,
            "downvotes": 0,
            "answers": 0,
        }
        return QNS.append(single_qn)

    def get(self):
        """get all questsions"""
        return jsonify({"message": "all requests found successfully"}, {"questions": QNS})


class Qusetion(Resource):
    """methods for single questions"""
    def get(self, question_id):
        """"
        Gets a question.
        ---
        tags:
            - Questions
        Parameters:
            - in: formData
            name: question_id
            type: integer
            required: true
        responses:
        200:
            description: The request was successful.
        201:
        description: New request created.
        400:
            description: Bad request made.
        401:
            description: Unauthorised access.
        404:
            description: Page not found.
        """
        single_qn = [single_qn for single_qn in QNS if single_qn['question_id'] == question_id]
        return single_qn

    @marshal_with(QUESTION_FIELDS)
    def put(self, question_id):
        """
        Modifies a request.
        ---
        tags:
            - The Requests
        parameters:
            - in: formData
            name: title
            type: string
            - in: formData
            name: body
            type: string
            - in: formData
            name: question_id
            type: integer
            required: true
        responses:
        200:
            description: The request was successful.
        201:
            description: New request created.
        400:
            description: Bad request made.
        401:
            description: Unauthorised access.
        404:
            description: Page not found.
        """
        single_qn = [single_qn for single_qn in QNS if single_qn['question_id'] == question_id]
        if 'title' in request.json and not isinstance(request.json['title'], str):
            return jsonify({"message": "Title should be a string"})
        if 'body' in request.json and not isinstance(request.json['body'], str):
            return jsonify({"message": "Question body is a string"})

        single_qn[0]['title'] = request.json.get('title', single_qn[0]['title']),
        single_qn[0]['description'] = request.json.get(
            'description', single_qn[0]['description']),
        return jsonify({"message": "Question successfully updated"},
                       {"single_qn": single_qn})

    def delete(self, question_id):
        """
        Creates a new request.
        ---
        tags:
            - The Requests
        parameters:
            - in: formData
            name: request_id
            type: integer
            required: true
        responses:
        200:
            description: The request was successful.
        201:
            description: New request created.
        400:
            description: Bad request made.
        401:
            description: Unauthorised access.
        404:
            description: Page not found.
        """
        single_qn = [single_qn for single_qn in QNS if single_qn['question_id'] == question_id]
        QNS.remove(single_qn[0])
        return
