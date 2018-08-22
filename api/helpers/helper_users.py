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
            "dbname='stackoverflow' user='postgres' password='12345678' host='localhost'")
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()

    def register_user(self, username,email, data):
        """helper for registering a user"""
        try:
            self.cur.execute("SELECT TRIM(username) FROM users WHERE username=%s",(username,))
            user_username = self.cur.fetchall()
            self.cur.execute("SELECT TRIM(email) FROM users WHERE email=%s",(email,))
            email_user = self.cur.fetchall()
            if len(user_username)!=0 and email_user is not None:
                return {"message":"User already exists!"},400
            else:
                self.cur.execute(""" 
                                    INSERT INTO users (username, email, password, role) 
                                                    VALUES ((%(username)s), %(email)s, %(password)s, %(role)s)
                                """, data)
                self.conn.commit()
                return {"message":"User created successfully!"},201
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"culd not see"},400

    def login_user(self, password, username):
        """helper for confirming user using id"""
        content = request.get_json()
        username = (content['username'])
        password = (content['password'])
        self.cur.execute(
            """ SELECT TRIM(username) FROM users WHERE username = %s """, (username,))
        user = self.cur.fetchall()
        logged_in_user_dict = user[0]
        logged_in_user = (logged_in_user_dict['btrim'])
        if user:
            self.cur2.execute(
                """ SELECT password FROM users WHERE username = %s """, (username,))
            pssword = self.cur2.fetchone()
            pasword = pssword[0]
            if check_password_hash(pasword, password):
                access_token = create_access_token(identity=logged_in_user)
                token = access_token
                return {"message" : "User successfully logged in","token": token}
            else:
                abort(401, "Wrong password!")
                
        else:
            return {"message" : "user not registered"},400