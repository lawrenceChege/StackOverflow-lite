"""Test for methods applied to answers"""
import json
from api.tests.base import BaseTestCase


class TestRequestsTestCase(BaseTestCase):
    """Tests for answers"""

    def set_up(self):
        """setup class"""
        pass

    def test_user_new_answer(self):
        """Test for posting a answer with correct details"""
        response = self.app.post('/api/v1/answers/1/', data=json.dumps(
            self.answer), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'answer posted successfully!')
    
    def test_answer_no_body(self):
        """Test for posting a answer with no body"""
        response = self.app.post('/api/v1/answers/1/', data=json.dumps(
            self.answer_no_body), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Body is required')

    def test_answer_no_title(self):
        """Test for posting a answer with no title"""
        response = self.app.post('/api/v1/answers/1/', data=json.dumps(
            self.answer_no_title), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Answers need a title')

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

    def test_user_view_an_answer(self):
        """Test for vieving a particular answer"""
        response_message = self.app.get('/api/v1/answers/1/5/')
        self.assertEqual(response_message.status_code, 200)

    def test_answer_not_found(self):
        """Test for vieving a non-existent answer"""
        response = self.app.get('/api/v1/answers/1/19999999/')
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Request does not exist!")


    def test_user_modify_an_answer(self):
        """Test for modifying a request"""
        response = self.app.put('/api/v1/answers/1/5/',
                                data=json.dumps(self.update_answer),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Answer updated successfully!")
    def test_modify_anwer_no_body(self):
        """Test for modifying a request no body"""
        response = self.app.put('/api/v1/answers/1/2/',
                                data=json.dumps(self.update_answer_no_body),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Body is required")

    def test_modify_anwer_no_title(self):
        """Test for modifying a request no title"""
        response = self.app.put('/api/v1/answers/1/2/',
                                data=json.dumps(self.update_answer_no_title),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Answer need a title")

    def test_user_delete_an_answer(self):
        # """Test for deleting an answer"""
        # response = self.app.delete('/api/v1/answers/1/2/')
        # self.assertEqual(response.status_code, 200)
        # data = json.loads(response.get_data())
        # self.assertEqual(data['message'], "Answer successfuly deleted")
        pass
