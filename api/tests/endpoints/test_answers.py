"""Test for methods applied to answers"""
import json
import unittest
from tests.basetest import BaseTestCase



class TestRequestsTestCase(BaseTestCase):
    """Tests for answers"""

    def setUp(self):
        pass

    def test_user_new_answer(self):
        """Test for posting a question"""
        #correct request
        response = self.app.post('/api/v1/answers/', data=json.dumps(
            self.answer), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Question posted successfully!')
        #no body
        response = self.app.post('/api/v1/answers/', data=json.dumps(
            self.answer_no_body), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Body is a required')

    def test_user_view_all_answers(self):
        """Test for viewing all answers"""

        response = self.app.get('/api/v1/answers/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "all answers found successfully")

    def test_view_answers_to_question(self):
        """Test for viewing a user's answers """
        response = self.app.get('/api/v1/answers/1/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "all question anwers found successfully")

    def test_user_view_an_answer(self):
        """Test for vieving a particular question"""

        response_message = self.app.get('/api/v1/answers/6')
        self.assertEqual(response_message.status_code, 200)

    def test_user_modify_an_answer(self):
        """Test for modifying a request"""

        response = self.app.put('/api/v1/answers/5',
                                data=json.dumps(
                                    dict(body="no more games")),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Answer successfully updated")

    def test_user_delete_an_answer(self):
        """Test for deleting an answer"""

        response = self.app.delete('/api/v1/answers/5')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Answer successfuly deleted")
        