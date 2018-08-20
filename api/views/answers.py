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
class Ans(Resource):
    """ method for getting all answers"""
    def get(self):
        """ gets all answers"""
        return jsonify({"message":"all answers found successfully"},
                       {"answers":ANS})


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
        ANS.append(single_ans)
        return jsonify({"message": "answer posted successfully!"},
                       {"sigle_ans": single_ans})
    def get(self,question_id):
        """get all answers to a question"""
        qn_ans = [qn_ans for qn_ans in ANS if qn_ans['question_id'] == question_id]
        return jsonify({"message": "all answers to this question found successfully"},
                       {"answers": qn_ans})


class Answer(Resource):
    """methods for single answers"""
    def get(self, question_id, answer_id):
        """"
        Gets an answer.
        
        """
        qn_ans = [qn_ans for qn_ans in ANS if qn_ans['question_id'] == question_id]
        single_ans = [single_ans for single_ans in qn_ans if single_ans['answer_id'] == answer_id]
        if len(single_ans) == 0:
            return {"message": "answer does not exist"}, 404
        return jsonify({"message": "answer successfully retrieved"},
                       {"single_ans": single_ans})

    def put(self, question_id, answer_id):
        """
        Modifies an answer.
        ---
        
        """
        qn_ans = [qn_ans for qn_ans in ANS if qn_ans['question_id'] == question_id]
        si_ans = [si_ans for si_ans in qn_ans if si_ans['answer_id'] == answer_id]
        if 'body' in request.json and not request.json['body']:
            return {"message": "body must be a string."}, 400
        si_ans[0]['body'] = request.json.get('body', si_ans[0]['body'])
        si_ans[0]['date_modified'] = str(datetime.datetime.now())
        return jsonify({"message": "Answer successfully updated"},
                       {"single_ans": si_ans[0]})

    def delete(self, question_id, answer_id):
        """
        delete an answer.
        --- 
        """
        qn_ans = [qn_ans for qn_ans in ANS if qn_ans['question_id'] == question_id]
        single_ans = [single_ans for single_ans in qn_ans if single_ans['answer_id'] == answer_id]
        ANS.remove(single_ans[0])
        return jsonify({"message":"Answer successfuly deleted"})
