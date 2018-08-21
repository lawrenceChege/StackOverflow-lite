"""Test for methods applied to answers"""
import json
from api.tests.base import BaseTestCase


class TestRequestsTestCase(BaseTestCase):
    """Tests for answers"""

    def set_up(self):
        """setup class"""
        pass

    def test_user_new_answer(self):
        """Test for posting a answer"""
        #correct request
        response = self.app.post('/api/v1/answers/1/', data=json.dumps(
            self.answer), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], 'answer posted successfully!')
        #no body
        response = self.app.post('/api/v1/answers/1/', data=json.dumps(
            self.answer_no_body), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Body is required')

    def test_user_view_all_answers(self):
        """Test for viewing all answers"""
        response = self.app.get('/api/v1/answers/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "all answers found successfully")

    def test_view_answers_to_question(self):
        """Test for viewing answers to a specific question"""
        response = self.app.get('/api/v1/answers/1/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "all answers to this question found successfully")

    def test_user_view_an_answer(self):
        """Test for vieving a particular question"""
        response_message = self.app.get('/api/v1/answers/1/1/')
        self.assertEqual(response_message.status_code, 200)

        #answer not found
        response = self.app.get('/api/v1/answers/1/19999999/')
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "answer does not exist")


    def test_user_modify_an_answer(self):
        """Test for modifying a request"""
        response = self.app.put('/api/v1/answers/2/2/',
                                data=json.dumps(
                                    dict(body="no more games")),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "Answer successfully updated")
        #invalid input
        response = self.app.put('/api/v1/answers/2/2/',
                                data=json.dumps(
                                    dict(body="")),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "body must be a string.")


    def test_user_delete_an_answer(self):
        """Test for deleting an answer"""
        response = self.app.delete('/api/v1/answers/3/4/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Answer successfuly deleted")
