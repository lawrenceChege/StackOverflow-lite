""" defines CRUD methods for answers """
import datetime
from flask import Blueprint, jsonify, request
from flask_restful import reqparse, Resource
from api.resources.resources import ANS


ANSWERS = Blueprint('answers', __name__,
                    url_prefix='/api/v1/answers/')

POST_PARSER = reqparse.RequestParser()
POST_PARSER.add_argument(
    'body', dest='body',
    type=str, location='form',
    required=True, help='The answer body',
)

class Answers(Resource):
    """ methods for answers"""
    def post(self, question_id):
        """
        Posts a new answer.
        ---
        tags:
            - New answer
        parameters:
        - in: formData
            name: body
            type: string
            required: true
        - in: formData
            name: question_id
            type: int
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
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400
        if 'question_id' in request.json and not request.json['question_id']:
            return {"message": "Question id is required"}, 400
        body, answer_id, question_id = (request.json['body'],
                                        request.json['answer_id'],
                                        request.json['question_id'])
        single_ans = {
            'answer_id': answer_id,
            "question_id": question_id,
            "body": body,
            "date_created": str(datetime.datetime.now()),
            "date_modified": str(datetime.datetime.now()),
            "upvotes": 0,
            "downvotes": 0,
            "status": "pending",
        }
        ANS.append(single_ans)
        return jsonify({"message": "answer posted successfully!"},
                       {"sigle_ans": single_ans})
    def get(self,question_id):
        """get all answers to a question"""
        qn_ans = [qn_ans for qn_ans in ANS if qn_ans['question_id'] == question_id]
        return jsonify({"message": "all answers found successfully"}, {"answers": qn_ans})


class Answer(Resource):
    """methods for single answers"""
    def get(self, answer_id):
        """"
        Gets an answer.
        ---
        tags:
            - answers
        Parameters:
            - in: formData
            name: answer_id
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
        single_ans = [single_ans for single_ans in ANS if single_ans['answer_id'] == answer_id]
        if len(single_ans) == 0:
            return {"message": "answer does not exist"}
        return jsonify({"message": "answer successfully retrieved"},
                       {"single_ans": single_ans})

    def put(self, answer_id):
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
            name: answer_id
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
        si_ans = [si_ans for si_ans in ANS if si_ans['answer_id'] == answer_id]
        if 'title' in request.json and not request.json['title']:
            return {"message": "Please enter a title"}, 400
        if 'body' in request.json and not request.json['body']:
            return {"message": "body must be a string."}, 400
        si_ans[0]['title'] = request.json.get('title', si_ans[0]['title'])
        si_ans[0]['body'] = request.json.get('body', si_ans[0]['body'])
        si_ans[0]['date_modified'] = str(datetime.datetime.now())
        return jsonify({"message": "answer successfully updated"},
                       {"single_ans": si_ans})

    def delete(self, answer_id):
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
        single_ans = [single_ans for single_ans in ANS if single_ans['answer_id'] == answer_id]
        ANS.remove(single_ans[0])
        return jsonify({"message":"answer successfuly deleted"})
