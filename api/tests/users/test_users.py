"""Tests for users"""
import json
import unittest
from tests.basetest import BaseTestCase


class TestUserTestCase(BaseTestCase):
    """ Test for normal user"""
    def test_user_signup(self):
        """Test for user signup"""
        #no username
        response = self.app.post('/api/v1/auth/signup',
                                 data=json.dumps(self.person_no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Username is required')

        #no email
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_no_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Email is required!')

        #invalid email
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_invalid_email),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Email is invalid')
        #no password
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Passord is required!')
        #correct details
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'User created successfully!')
        #existing user
        response = self.app.post('api/v1/auth/signup',
                                 data=json.dumps(self.person_existing_user),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'User already exists!')

    def test_login(self):
        """Test for login"""
        #nopassword
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.no_password),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Password is required')
        #no username
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.no_username),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Username is required')
        #incorrect
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.wrong_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 401)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'Wrong password!')
        #empty
        response = self.app.post('api/v1/auth/login',
                                 data=json.dumps(self.correct_login),
                                 headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        dataman = json.loads(response.get_data())
        self.assertEqual(dataman['message'], 'User successfully logged in')
