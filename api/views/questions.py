""" defines CRUD methods for questions """
import datetime
from flask import Blueprint, jsonify, request
from flask_restful import reqparse, Resource
from api.resources.resources import QNS


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
            return {"message": "Questions need a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400

        title, body, question_id = (request.json['title'],
                                    request.json['body'],
                                    request.json['question_id'])
        single_qn = {
            'question_id': question_id,
            "title": title,
            "body": body,
            "date_created": str(datetime.datetime.now()),
            "date_modified": str(datetime.datetime.now()),
            "upvotes": 0,
            "downvotes": 0,
            "answers": 0,
        }
        QNS.append(single_qn)
        return jsonify({"message": "Question posted successfully!"},
                       {"sigle_qn": single_qn})
    def get(self):
        """get all questsions"""
        return jsonify({"message": "all questions found successfully"}, {"questions": QNS})


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
        if len(single_qn) == 0:
            return {"message": "Question does not exist"},404
        return jsonify({"message": "Question successfully retrieved"},
                       {"single_qn": single_qn})

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
        si_qn = [si_qn for si_qn in QNS if si_qn['question_id'] == question_id]
        if 'title' in request.json and not request.json['title']:
            return {"message": "Please enter a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "body must be a string."}, 400
        si_qn[0]['title'] = request.json.get('title', si_qn[0]['title'])
        si_qn[0]['body'] = request.json.get('body', si_qn[0]['body'])
        si_qn[0]['date_modified'] = str(datetime.datetime.now())
        return jsonify({"message": "Question successfully updated"},
                       {"single_qn": si_qn})

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
        return jsonify({"message":"Question successfuly deleted"})
