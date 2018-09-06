"""this holds the methods for the users"""
import psycopg2
from flask import jsonify, request, Blueprint
from flask_restful import Resource, reqparse
from werkzeug.security import generate_password_hash
from api.helpers.helper_users import HelperDb


USER = Blueprint("user", __name__, 
                url_prefix="api/v2/auth/")

CONNECT_CREDS = {
    "host": os.getenv('DB_HOST'),
    "database": os.getenv('DB_NAME'),
    "user": os.getenv('DB_USER'),
    "password": os.getenv('DB_PASSWORD')
}
DATABASE_URL = os.getenv('DATABASE_URL')

def connectTODB():
    try:
        print("connecting to database ...")
        try:
            return psycopg2.connect(DATABASE_URL)
        except:
            return psycopg2.connect(**CONNECT_CREDS)
    except:
        print("Connection to database failed!")

conn = connectTODB()
cur = conn.cursor()

class User(Resource):
    """This class will define methods for the user"""
    def post(self):
        """
        Registers a new user.
        ---
        """
        self.reqparse = reqparse.RequestParser()

        self.reqparse.add_argument("username", location='json')

        self.reqparse.add_argument('email', location='json')

        self.reqparse.add_argument('password', location='json')
        args = self.reqparse.parse_args()
        if not request.json:
            return jsonify({"message" : "check your request type"})
        if 'username' not in request.json or not request.json['username']:
            return {"message" : "Username is required"}, 400
        if 'email' not in request.json or not request.json['email']:
            return {"message" : "Email is required!"}, 400
        if 'password' not in request.json or not request.json['password']:
            return {"message" : "Passord is required!"}, 400
        username, email, password = args["username"], args["email"], args["password"]
        hash_password = generate_password_hash(password)
        data = {
            "username": username,
            "email": email,
            "password": hash_password,
            "role": "user"
        }
        user = HelperDb().register_user(username, email, data)
        return user


class UserLogin(Resource):
    """this logs in the user"""
    def post(self):
        """
        Signs in a new user.
        ---
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', location='json')
        self.reqparse.add_argument('password', location='json')
        if not request.json:
            return jsonify({"message" : "check your request type"})
        if 'username' in request.json and not request.json['username']:
            return {"message" : "Username is required"}, 400
        if 'password' in request.json and not request.json['password']:
            return {"message" : "Password is required"}, 400
        args = self.reqparse.parse_args()
        usernm, pssword = args["username"], args["password"]
        return HelperDb().login_user(usernm, pssword), 201


class GetUserRequests(Resource):
    """"""
    def get(self, user_id):
        """
        Registers a new user.
        ---
        """
        try:
            cur.execute("""SELECT * FROM requests WHERE user_id = user_id""")
            result = cur.fetchall()
            if user_id in result:
                return jsonify(result)
            else:
                return {"message":"User not found!"}
        except:
            return {"message":"I could not  select from users"}
