import psycopg2
import os
import json
import unicodedata
from datetime import timedelta
from flask import request, abort
from psycopg2.extras import RealDictCursor
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

DATABASE_URL = os.getenv('DATABASE_URL')

def connectTODB():
    try:
        print("connecting to database ...")
        try:
            return psycopg2.connect(DATABASE_URL)
            print("connected to the database")
        except:
            return psycopg2.connect('postgresql://localhost/stackoverflow?user=postgres&password=3162')
            print("connected to the database")
    except:
        print("Connection to database failed!")

class HelperDb(object):
    """ Helper methods for connecting to db"""
    def __init__(self):
        """initialize db"""
        self.conn = connectTODB()
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        self.cur2 = self.conn.cursor()

    def register_user(self, username,email, data):
        """helper for registering a user"""
        try:
            self.cur.execute("SELECT TRIM(username) FROM users WHERE username=%s",(username,))
            user_username = self.cur.fetchall()
            self.cur.execute("SELECT TRIM(email) FROM users WHERE email=%s",(email,))
            email_user = self.cur.fetchall()
            if len(user_username)!=0:
                return {"message":"Username already exists!"}, 400
            elif len(email_user)!=0:
                return {"message":" Email already exists!"}, 400
            else:
                self.cur.execute(""" 
                                    INSERT INTO users (username, email, password, role) 
                                                    VALUES ((%(username)s), %(email)s, %(password)s, %(role)s)
                                """, data)
                self.conn.commit()
                return {"message":"User created successfully!"}, 201
        except(Exception, psycopg2.DatabaseError) as error:
            print(error)
            return {"message":"There was an error querrying the database"}, 500

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
                timeout = timedelta(minutes=300)
                access_token = create_access_token(identity=logged_in_user, expires_delta=timeout)
                token = access_token
                print ({"user logged in": logged_in_user})
                return {"message" : "User successfully logged in", "token": token, "username":logged_in_user }
            else:
                abort(401, "Wrong credentials!")
                
        else:
            return {"message" : "user not registered"}, 400

    def get_user_Requests(self, user_id):
        try:
            self.cur.execute("""SELECT * FROM requests WHERE user_id = user_id""")
            result = self.cur.fetchall()
            if user_id in result:
                return result
            else:
                return {"message":"User not found!"}
        except:
            return {"message":"I could not  select from users"}