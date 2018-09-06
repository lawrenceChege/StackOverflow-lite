import psycopg2
import json
import unicodedata
from flask import request, abort, jsonify
from psycopg2.extras import RealDictCursor
from api.app import CONNECT_CREDS, DATABASE_URL, connectTODB

class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = connectTODB()
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()
    
    def create_request(self, single_answer):
        """helper for posting a answer"""
        content = request.get_json()
        Title = (content['title'])
        try:
            self.cur.execute(
                "SELECT * FROM answers WHERE title = %s", (Title,))
            request_i = self.cur.fetchall()
            if len(request_i)!= 0:
                return {"message":"answer with similar title exists"}, 400
            else:
                self.cur.execute(""" 
                                    INSERT INTO answers (question_id, title, body, username, upvotes, downvotes, status)
                                                            VALUES (%(question_id)s, %(title)s, %(body)s, %(username)s, %(upvotes)s, %(downvotes)s, %(status)s)
                                """, single_answer)
                self.conn.commit()
                return {"message":"answer posted successfully!"}, 201
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500

    def update_request(self, question_id, answer_id, single_answer):
        """elper for updating a answer"""
        try:
            self.cur.execute(
                "SELECT * FROM answers WHERE question_id = %s and answer_id = %s", (question_id, answer_id))
            answer_i = self.cur.fetchone()
            if answer_i:
                self.cur.execute(
                    "UPDATE answers SET title=%(title)s, body=%(body)s, date_modified=%(date_modified)s", single_answer)
                self.conn.commit()
                return {"message":"Answer updated successfully!"}, 200
            else:
                return {"message":"Answer does not exist"}, 400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500

    def delete_request(self, answer_id):
        """handles deleting the answer from database"""
        try:
            self.cur.execute(
                "SELECT * FROM answers WHERE answer_id = %s", (answer_id,))
            answer_details = self.cur.fetchall()
            if len(answer_details)!=0:
                self.cur.execute(
                    """ DELETE FROM answers WHERE answer_id = %s""", (answer_id,))
                self.conn.commit()
                return {"message":"Request deleted successfully!"}, 200
            else:
                return {"message":"Request does not exitst!"}, 400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500

    def get_answers(self, question_id):
        """helper for retrieving  answers for one question"""
        try:
            self.cur.execute(
                "SELECT * FROM answers WHERE question_id = %s", (question_id,))
            request_i = self.cur.fetchall()
            answers = str(request_i)
            if len(request_i) > 0:
                return {"answers": answers}, 200
            else:
                return {"message":"Answers do not exitst!"}, 400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500

    def get_request(self, question_id, answer_id):
        """helper for retrieving an answer"""
        try:
            self.cur.execute(
                "SELECT * FROM answers WHERE question_id = %s and answer_id = %s", (question_id, answer_id))
            single_answer = self.cur.fetchall()
            output = str(single_answer)
            if len(single_answer) > 0:
                return {"single_answer": output}
            else:
                return {"message":"Request does not exist!"}, 400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500

    def get_all_answers(self):
        """helper for getting all answers"""
        try:
            self.cur.execute(
                "SELECT * FROM answers"
            )
            answers = self.cur.fetchall()
            if len(answers) > 0:
                return jsonify({"message": "all answers found successfully"},
                               {"answers": answers})
            else:
                return {"message": " No answers found"}
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500
