import psycopg2
import json
import unicodedata
from flask import request, abort
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from manage import Database

class HelpAdmin():
    """helper methods for Admin"""
    def __init__(self):
        """initialize db"""
        self.conn = psycopg2.connect(
            "dbname='maintenancedb' user='postgres' password='       ' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()

    def get_user(self, user_id):
        try:
            self.cur.execute(
                """ SELECT * FROM users where user_id=%s""", (user_id,))
            user = self.cur.fetchall()
            if user:
                return user,200
            else:
                return {"message":"user does not exitst!"},400
        except:
            return {"message":"I could not read from users"},400

    def get_all_users(self):
        self.cur.execute(""" SELECT * FROM users""")
        result = self.cur.fetchall()
        return result

    def change_status(self, request_id, data):
        try:
            self.cur.execute(
                """ SELECT TRIM(status) FROM requests WHERE request_id=%s""", (request_id,))
            result = self.cur.fetchall()
            if len(result) > 0:
                self.cur.execute("UPDATE requests SET status=%(status)s", data)
                self.conn.commit()
                return {"message":"Request status updated !"},200
            else:
                return {"message":"username does not exitst!"},400
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"I could not read from users"},400

    def login_admin(self, username, password):
        """logs in admin"""
        content = request.get_json()
        username = (content['username'])
        password = (content['password'])
        user = "Admin"
        if username == user:
            self.cur2.execute(
                """ SELECT password FROM users WHERE username = %s """, (user,))
            pssword = self.cur2.fetchone()
            pasword = pssword[0]
            if check_password_hash(pasword, password):
                access_token = create_access_token(identity=user)
                token = access_token
                return {"message":"You know What to do !"},token
            else:
                return {"message":"wrong password"},401
        else:
            return {"message":"You are not admin ...shu shu!"},401

    def delete_user(self, user_id):
        """delete a user"""
        try:
            self.cur.execute(
                "SELECT * FROM users WHERE user_id = %s", (user_id,))
            request_i = self.cur.fetchall()
            if len(request_i) > 0:
                self.cur.execute(
                    """ DELETE FROM users WHERE user_id = %s""", (user_id,))
                self.conn.commit()
                return {"message":"Request deleted successfully!"},200
            else:
                return {"message":"Request does not exitst!"},400
        except:
            return {"message":"I could not see inside"},400
    
    def get_all_requests(self):
        """ get all requests from all users"""
        try:
            self.cur.execute(
                "SELECT * FROM requests"
            )
            requests = self.cur.fetchall()
            return {"message":"all requests found successfully","requests":requests}
        except:
            return {"message":"I could not see inside"}