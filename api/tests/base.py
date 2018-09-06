""" This is the base class for all the tests"""
from unittest import TestCase
import unittest
import testing.postgresql
from api.app import APP

class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(self):
        """set up app configuration"""
        self.postgresql = testing.postgresql.Postgresql(port=7654)
        self.app = APP.test_client()
        self.app.testing = True
        self.users = [
            {
                "user_id":1,
                "username": "lau lau",
                "email": "mbuchez9@gmail.com",
                "password": "maembembili"
            },
            {
                "user_id":2,
                "username": "lau",
                "email": "mbuchez8@gmail.com",
                "password": "maembembili"
            },
            {
                "user_id":3,
                "username": "lalau",
                "email": "mbuchez8@gmail.com",
                "password": "maembembili"
            }
        ]
        self.person = {
            "username": "lauau",
            "email": "mbuch@gmail.com",
            "password": "maembembili"
        }
        self.person_no_username = {
            "email": "mbuchez8@gmail.com",
            "password": "maembembili"
        }
        self.person_no_email = {
            "username": "lawrence",
            "password": "maembembili"
        }
        self.person_no_password = {
            "username": "lawrence",
            "email": "mbuchez8@gmail.com",
        }
        self.person_invalid_email = {
            "username": "lawrence",
            "email": "mbuchez.com",
            "password": "maembembili"
        }
        self.person_existing_user = {
            "username": "test",
            "email": "test@gmail.com",
            "password": "password"
        }
        self.correct_login = {"username": "lau lau",
                              "password": "maembembili"}
        self.wrong_login = {"username": "lawrence",
                            "password": "mistubishi"}
        self.no_username = {"username": "",
                            "password": "maembembili"}
        self.no_password = {"username": "lawrence",
                            "password": ""}
        self.admin = {
            "username": "admin",
            "email": "admin@gmail.com",
            "password": "admin1234"
        }
        self.admin_correct = {"username": "admin",
                              "password": "admn1234"}
        self.admin_wrong = {"username": "lawrence",
                            "password": "mimi"}

        self.question = {
            "title":"how are you doing?",
            "body": "fogort hammer"
        }
        self.update_question ={
            "title":"how are they doing?",
            "body": "fogort hammer"
        }
        self.update_question_no_body ={
            "title":"how are they doing?",
            "body": ""
        }
        self.update_question_no_title ={
            "title":"",
            "body": "fogort hammer"
        }
        self.update_answer = {
            "title":"how are they doing?",
            "body": "fogort hammer"
        }
        self.update_answer_no_body = {
            "title":"how are they doing?",
            "body": ""
        }
        self.update_answer_no_title = {
            "title":"",
            "body": "fogort hammer"
        }
        self.questions = [
            {
                "question_id": 1,
                "user_id":1,
                "title": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            },
            {
                "question_id": 2,
                "user_id":1,
                "title": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            },
            {
                "question_id": 3,
                "user_id":2,
                "title": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            },
            {
                "question_id": 1,
                "user_id":1,
                "title": "how are you doing?",
                "body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            }
        ]
        self.question_no_title = {
            "question_id": 1,
            "user_id":1,
            "title": "",
            "body": "fogort hammer",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.question_no_body = {
            "question_id": 1,
            "user_id":1,
            "title": "how are you doing?",
            "body": "",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.question_invalid_title = {
            "question_id": 1,
            "user_id":1,
            "title": 1234,
            "body": "How come it 1234",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.answer = {
            "answer_id": 1,
            "user_id":1,
            "question_id":2,
            "title":"oh baby",
            "body": "baby i am lost",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
            "status": "Pending"
        }
        self.answers = [
            {
                "answer_id": 1,
                "user_id":1,
                "question_id":2,
                "body": "i wish i knew",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
                "status": "Pending"
            },
            {
                "answer_id": 2,
                "user_id":1,
                "question_id":2,
                "body": "nobody knows",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
                "status": "Pending"
            },
            {
                "answer_id": 3,
                "user_id":1,
                "question_id":2,
                "body": "things are better",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
                "status": "Pending"
            }
        ]
        self.answer_no_body = {
            "answer_id": 3,
            "user_id":1,
            "question_id":2,
            "title": "how are you doing?",
            "body": "",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
            "status": "Pending"
        }
        self.answer_no_title = {
            "answer_id": 3,
            "user_id":1,
            "question_id":2,
            "title": "",
            "body": "mama mhu fer",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
            "status": "Pending"
        }
        self.accept_answer = {
            "status": "Accept"
        }

    def tearDown(self):
        
        self.postgresql.stop()

if __name__ == '__main__':
    unittest.main()
