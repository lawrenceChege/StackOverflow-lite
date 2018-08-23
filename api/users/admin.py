"""API endpoints for the maintenance maintenancedb app"""
import psycopg2
from flask import jsonify
from flask_restful import Resource, reqparse,fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from api.helpers.helper_admin import HelpAdmin
from api.resources.validators import check_request, check_user



conn= psycopg2.connect("dbname='maintenancedb' user='postgres' password='       ' host='localhost'")
cur = conn.cursor()
resource_fields = {
    'status': fields.String,
}

class Admin(Resource):
    """defines methods for admin"""
    def post(self):
        """
        Logs in Admin.
        ---
        """
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str, required = True,
        help ="Username is required!")
        self.reqparse.add_argument('password', type = str, required = True,
        help = "Passord is required!", location = 'json')
        args =  self.reqparse.parse_args()
        check_user(args)
        usernm, pssword = args["username"], args["password"]
        return HelpAdmin().login_admin(usernm,pssword)

class Admin_get_all(Resource):
    """Gets all users"""
    @jwt_required
    def get(self):
        """
        Gets all users.
        ---
        """
        current_user = get_jwt_identity()
        return HelpAdmin().get_all_users(),current_user


class Admin_get_user(Resource):
    """ gets a user"""
    @jwt_required
    def get(self, user_id):
        """
        Gets a user.
        ---
            """
        current_user = get_jwt_identity()
        return  HelpAdmin().get_user(user_id),current_user

    def delete(self,user_id):
        """
        deletes a new user.
        ---
        """
        current_user = get_jwt_identity()
        return  HelpAdmin().delete_user(user_id),current_user

class Admin_approve_request(Resource):
    """defines methods for changing the status of a request"""
    @jwt_required
    def put(self, request_id, **kwargs):
        """
        updates a request's status.
        ---
        """
        check_request(resource_fields)
        current_user = get_jwt_identity()
        status =resource_fields['status']
        req = {
            'status': status
        }
        return jsonify(logged_in_as=current_user),HelpAdmin().change_status(request_id, req)

class Admin_get_requests(Resource):
  """gets all requests from all users """
  def get(self):
    return HelpAdmin().get_all_requests()
