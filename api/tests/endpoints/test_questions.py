"""Test for methods applied to Questions"""
from tests.baseTest import BaseTestCase

import unittest
import json


class TestRequestsTestCase(BaseTestCase):
    """Tests for Questions"""

    def setUp(self):
        pass

    def test_user_new_question(self):
        """Test for posting a question"""
        #correct request
        response = self.app.post('/api/v1/questions/', data=json.dumps(
            self.question), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Question posted successfully!')
        #no title
        response = self.app.post('/api/v1/questions/', data=json.dumps(
            self.question_no_title), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Questions need a title')
        #invalid title
        response = self.app.post('/api/v1/questions/', data=json.dumps(
            self.question_invalid_title), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Title should be a string')
        #no body
        response = self.app.post('/api/v1/questions/', data=json.dumps(
            self.question_no_body), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'],'Body is a required')

    def test_user_view_all_questions(self):
        """Test for viewing all questions"""

        response = self.app.get('/api/v1/questions/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'],"all questions found successfully")

    def test_user_view_a_users_questions(self):
        """Test for viewing a user's questions """
        response = self.app.get('/api/v1/questions/1/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'],"all question found successfully")
        

    def test_user_view_a_question(self):
        """Test for vieving a particular question"""

        response_message = self.app.get('/api/v1/questions/6')
        self.assertEqual(response_message.status_code, 200)

    def test_user_modify_a_question(self):
        """Test for modifying a request"""
        
        response = self.app.put('/api/v1/questions/5',
                                        data=json.dumps(
                                            dict(body="no more games")),
                                        headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data=json.loads(response.get_data())
        self.assertEqual(data['message'], "Question successfully updated")

    def test_user_delete_a_request(self):
        """Test for deleting a question"""

        response = self.app.delete('/api/v1/questions/5')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual( data['message'] , "Question successfuly deleted")
