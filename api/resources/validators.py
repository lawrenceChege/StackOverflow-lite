import re
from flask import request, jsonify


def check_email(data):
    vemail = re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", data)
    if not vemail:
        return {'message': 'Email is invalid'}

def check_password(password):
    password = re.match(r'[a-zA-Z_]+[\d\w]{8,}', password)
    if password is None:
        return {'message': 'password should contain atleast (a-z), (0-4), (-), characters(8)'}
