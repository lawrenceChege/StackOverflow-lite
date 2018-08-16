""" This is the base class for all the tests"""
from unittest import TestCase
import unittest
from app.app import app

class BaseTestCase(TestCase):
    """ set up configurations for the test environment"""
    @classmethod
    def setUpClass(self):
        """set up app configuration"""
        self.app = app.test_client()
        self.app.testing = True
        self.users = [
            {
                "id":1,
                "username": "lau lau",
                "email": "mbuchez9@gmail.com",
                "password": "maembembili"
            },
            {
                "id":2,
                "username": "lau",
                "email": "mbuchez8@gmail.com",
                "password": "maembembili"
            },
            {
                "id":3,
                "username": "lalau",
                "email": "mbuchez8@gmail.com",
                "password": "maembembili"
            }
        ]
        self.person = {
            "username": "lau lau",
            "email": "mbuchez9@gmail.com",
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
            "id": 1,
            "user_id":1,
            "Title":"how are you doing?",
            "Body": "fogort hammer",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.questions = [
            {
                "id": 1,
                "user_id":1,
                "Title": "how are you doing?",
                "Body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            },
            {
                "id": 2,
                "user_id":1,
                "Title": "how are you doing?",
                "Body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            },
            {
                "id": 3,
                "user_id":2,
                "Title": "how are you doing?",
                "Body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            },
            {
                "id": 1,
                "user_id":1,
                "Title": "how are you doing?",
                "Body": "fogort hammer",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
            }
        ]
        self.question_no_title = {
            "id": 1,
            "user_id":1,
            "Title": "",
            "Body": "fogort hammer",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.question_no_body = {
            "id": 1,
            "user_id":1,
            "Title": "how are you doing?",
            "Body": "",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.question_invalid_title = {
            "id": 1,
            "user_id":1,
            "Title": 1234,
            "Body": "How come it 1234",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
        }
        self.answer = {
            "id": 1,
            "user_id":1,
            "question_id":2,
            "Body": "baby i am lost",
            "date_created": 11/3/18,
            "date_modified":12/3/18,
            "upvotes":3,
            "downvotes":1,
            "answers":0,
            "status": "Pending"
        }
        self.answers = [
            {
                "id": 1,
                "user_id":1,
                "question_id":2,
                "Body": "i wish i knew",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
                "status": "Pending"
            },
            {
                "id": 2,
                "user_id":1,
                "question_id":2,
                "Body": "nobody knows",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
                "status": "Pending"
            },
            {
                "id": 3,
                "user_id":1,
                "question_id":2,
                "Body": "things are better",
                "date_created": 11/3/18,
                "date_modified":12/3/18,
                "upvotes":3,
                "downvotes":1,
                "answers":0,
                "status": "Pending"
            }
        ]
        self.answer_no_body = {
            "id": 3,
            "user_id":1,
            "question_id":2,
            "Title": "how are you doing?",
            "Body": "",
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
if __name__ == '__main__':
    unittest.main()
