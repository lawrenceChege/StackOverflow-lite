"""Test for methods applied to Questions"""
import json
from api.tests.base import BaseTestCase


class TestRequestsTestCase(BaseTestCase):
    """Tests for Questions"""

    def test_user_new_question(self):
        """Test for posting a question"""
        #correct request
        # response = self.app.post('/api/v1/questions/', data=json.dumps(
        #     self.question), headers={'content-type': "application/json"})
        # self.assertEqual(response.status_code, 201)
        # data = json.loads(response.get_data())
        # self.assertEqual(data[0]['message'], 'Question posted successfully!')
        #no title
        response = self.app.post('/api/v1/questions/', data=json.dumps(
            self.question_no_title), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Questions need a title')
        #no body
        response = self.app.post('/api/v1/questions/', data=json.dumps(
            self.question_no_body), headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Body is required')

    def test_user_view_all_questions(self):
        """Test for viewing all questions"""

        response = self.app.get('/api/v1/questions/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "all questions found successfully")

    def test_user_view_a_question(self):
        """Test for vieving a particular question"""
        #existing quesion
        response = self.app.get('/api/v1/questions/2/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data[0]['message'], "Question successfully retrieved")

        #question does not exist
        response = self.app.get('/api/v1/questions/87878/')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Request does not exitst!")


    def test_user_modify_a_question(self):
        """Test for modifying a question """
        response = self.app.put('/api/v1/questions/2/',
                                data=json.dumps(self.update_question),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Request updated successfully!")

        #invalid body
        response = self.app.put('/api/v1/questions/1/',
                                data=json.dumps(
                                    dict(body="")),
                                headers={'content-type': "application/json"})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], "Body is required")


    def test_user_delete_a_question(self):
        """Test for deleting a question"""
        # response = self.app.delete('/api/v1/questions/1/')
        # self.assertEqual(response.status_code, 200)
        # data = json.loads(response.get_data())
        # self.assertEqual(data['message'], "Question successfuly deleted")
