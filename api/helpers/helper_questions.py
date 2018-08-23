import psycopg2
import json
import unicodedata
from flask import request, abort, jsonify
from psycopg2.extras import RealDictCursor


class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect(
            "dbname='stackoverflow' user='postgres' password='12345678' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()
    
    def create_request(self, single_question):
        """helper for posting a question"""
        content = request.get_json()
        Title = (content['title'])
        try:
            self.cur.execute(
                "SELECT * FROM questions WHERE title = %s", (Title,))
            request_i = self.cur.fetchall()
            if len(request_i)!= 0:
                return {"message":"Question with similar title exists"}, 400
            else:
                self.cur.execute(""" 
                                    INSERT INTO questions (title, body, username, upvotes, downvotes, answers)
                                                            VALUES (%(title)s, %(body)s, %(username)s, %(upvotes)s, %(downvotes)s, %(answers)s)
                                """, single_question)
                self.conn.commit()
                return {"message":"Question posted successfully!"}, 201
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message": error}, 400

    def update_request(self, question_id, single_question):
        """elper for updating a question"""
        try:
            self.cur.execute(
                "SELECT * FROM questions WHERE question_id = %s", (question_id,))
            question_i = self.cur.fetchone()
            if question_i:
                self.cur.execute(
                    "UPDATE questions SET title=%(title)s, body=%(body)s, date_modified=%(date_modified)s", single_question)
                self.conn.commit()
                return {"message":"Request updated successfully!"}, 200
            else:
                return {"message":"Request does not exist"}, 400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message": error}, 400

    def delete_request(self, question_id):
        """handles deleting the question from database"""
        try:
            self.cur.execute(
                "SELECT * FROM questions WHERE question_id = %s", (question_id,))
            question_details = self.cur.fetchall()
            if len(question_details)!=0:
                self.cur.execute(
                    """ DELETE FROM questions WHERE question_id = %s""", (question_id,))
                self.conn.commit()
                return {"message":"Request deleted successfully!"}, 200
            else:
                return {"message":"Request does not exitst!"}, 400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message": error}, 400

    def get_request(self, question_id):
        """helper for retrieving one question"""
        try:
            self.cur.execute(
                "SELECT * FROM questions WHERE question_id = %s", (question_id,))
            request_i = self.cur.fetchall()
            if len(request_i) > 0:
                return request_i, 200
            else:
                return {"message":"Request does not exitst!"},400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message": error}, 400

    def get_all_questions(self):
        """helper for getting all questions"""
        try:
            self.cur.execute(
                "SELECT * FROM questions"
            )
            questions = self.cur.fetchall()
            if len(questions) > 0:
                return jsonify({"message": "all questions found successfully"},
                               {"questions": questions})
            else:
                return {"message": " No questions found"}
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message": error}, 400
