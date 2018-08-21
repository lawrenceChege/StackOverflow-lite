""" defines CRUD methods for answers """
import datetime
from flask import Blueprint, jsonify, request
from flask_restful import reqparse, Resource
from api.resources.resources import ANSWERS_DICT


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
        return jsonify({"message":"all answers found successfully"},
                       {"answers":ANSWERS_DICT})


class Answers(Resource):
    """ methods for answers"""
    def post(self, question_id):
        """
        Posts a new answer.
        """
        if 'body' in request.json and not request.json['body']:
            return {"message": "Body is required"}, 400
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
        ANSWERS_DICT.append(single_ans)
        return jsonify({"message": "answer posted successfully!"},
                       {"sigle_ans": single_ans})
    def get(self,question_id):
        """get all answers to a question"""
        question_ans = [question_ans for question_ans in ANSWERS_DICT if question_ans['question_id'] == question_id]
        return jsonify({"message": "all answers to this question found successfully"},
                       {"answers": question_ans})


class Answer(Resource):
    """methods for single answers"""
    def get(self, question_id, answer_id):
        """"
        Gets an answer.
        
        """
        question_ans = [question_ans for question_ans in ANSWERS_DICT if question_ans['question_id'] == question_id]
        single_ans = [single_ans for single_ans in question_ans if single_ans['answer_id'] == answer_id]
        if len(single_ans) == 0:
            return {"message": "answer does not exist"}, 404
        return jsonify({"message": "answer successfully retrieved"},
                       {"single_ans": single_ans})

    def put(self, question_id, answer_id):
        """
        Modifies an answer.
        ---
        
        """
        question_ans = [question_ans for question_ans in ANSWERS_DICT if question_ans['question_id'] == question_id]
        single_answer = [single_answer for single_answer in question_ans if single_answer['answer_id'] == answer_id]
        if 'body' in request.json and not request.json['body']:
            return {"message": "body must be a string."}, 400
        single_answer[0]['body'] = request.json.get('body', single_answer[0]['body'])
        single_answer[0]['date_modified'] = str(datetime.datetime.now())
        return jsonify({"message": "Answer successfully updated"},
                       {"single_ans": single_answer[0]})

    def delete(self, question_id, answer_id):
        """
        delete an answer.
        ---
        """
        question_ans = [question_ans for question_ans in ANSWERS_DICT if question_ans['question_id'] == question_id]
        single_ans = [single_ans for single_ans in question_ans if single_ans['answer_id'] == answer_id]
        ANSWERS_DICT.remove(single_ans[0])
        return jsonify({"message":"Answer successfuly deleted"})
