"""Tests for users"""
from api.tests.base import BaseTestCase

import json

class TestUserTestCase(BaseTestCase):
    """ Test for normal user"""
       
    def test_user_signup_no_username(self):
        """Test for user signup no username"""
        #no username
        response = self.app.post('/api/v1/auth/signup/',
                                 data=json.dumps(self.person_no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        print(response)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Username is required')

    def test_user_signup_no_email(self):
        """Test for user signup no email"""
        #no email
        response = self.app.post('api/v1/auth/signup/',
                                 data=json.dumps(self.person_no_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Email is required!')

    def test_user_signup_no_password(self):
        """Test for user signup no password"""
        #no password
        response = self.app.post('api/v1/auth/signup/',
                                 data=json.dumps(self.person_no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Passord is required!')

    def test_user_signup(self):
        """Test for user signup"""
        #correct details
        # response = self.app.post('api/v1/auth/signup/',
        #                          data=json.dumps(self.person),
        #                          headers={'content-type': "application/json"})
        # self.assertEqual(response.status_code,201)
        # dataman = json.loads(response.get_data())
        # self.assertEqual(dataman['message'],'User created successfully!')
        pass

    def test_user_signup_existing(self):
        """Test for user signup existing user"""
        #existing user
        response = self.app.post('api/v1/auth/signup/',
                                 data=json.dumps(self.person_existing_user),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User already exists!')

    def test_login_no_password(self):
        """Test for login no password"""
        #nopassword
        response = self.app.post('api/v1/auth/login/',
                                 data=json.dumps(self.no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Password is required')

    def test_login_no_username(self):
        """Test for login no uswername"""
        #no username
        response = self.app.post('api/v1/auth/login/',
                                 data=json.dumps(self.no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Username is required')

    def test_login_incorrect_credentials(self):
        """Test for login incorrect credentials"""
        #incorrect
        response = self.app.post('api/v1/auth/login/',
                                 data=json.dumps(self.wrong_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 401)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'Wrong password!')
    
    def test_login_correct_credentials(self):
        """Test for login"""
        response = self.app.post('api/v1/auth/login/',
                                 data=json.dumps(self.correct_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code,201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'],'User successfully logged in')
        