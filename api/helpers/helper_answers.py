import psycopg2
import json
import unicodedata
from flask import request, abort
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash


class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect(
            "dbname='maintenancedb' user='postgres' password='       ' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()
        
    def create_request(self, title, req):
        content = request.get_json()
        Title = (content['title'])
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE title = %s", (Title,))
            request_i = self.cur.fetchall()
            if len(request_i)!=0:
                return {"message":"Request with similar title exists"},400
            else:
                self.cur.execute(""" 
                                    INSERT INTO requests (category, title, frequency, description, status ,username)
                                                            VALUES ( %(category)s, %(title)s, %(frequency)s,  %(description)s, %(status)s, %(username)s)
                                """, req)
                self.conn.commit()
                return {"message":"Request created successfully!"},201

        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"I could not red from requests"},400

    def update_request(self, request_id, data):
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE request_id = %s", (request_id,))
            request_i = self.cur.fetchone()
            if request_i:
                self.cur.execute(
                    "UPDATE requests SET category=%(category)s, frequency=%(frequency)s, title=%(title)s, description=%(description)s", data)
                self.conn.commit()
                return {"message":"Request updated successfully!"},200
            else:
                return {"message":"Request does not exist"},400
        except:
            return {"message":"I could not select from requests"},400

    def delete_request(self,request_id):
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE request_id = %s", (request_id,))
            request_details = self.cur.fetchall()
            if len(request_details)!=0:
                self.cur.execute(
                    """ DELETE FROM requests WHERE request_id = %s""", (request_id,))
                self.conn.commit()
                return {"message":"Request deleted successfully!"},200
            else:
                return {"message":"Request does not exitst!"},400
        except:
            return {"message":"I could not see inside"},400

    def get_request(self, request_id):
        try:
            self.cur.execute(
                "SELECT * FROM requests WHERE request_id = %s", (request_id,))
            request_i = self.cur.fetchall()
            if len(request_i) > 0:
                return request_i,200
            else:
                return {"message":"Request does not exitst!"},400
        except:
            return {"message":"I could not read from requests"},400