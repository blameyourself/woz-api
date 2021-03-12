from flask_restful import Resource, request
from include.profile.user_email_verify_func import emailVerification
from flask import jsonify
import os
import json


class UserEmailVerify(Resource):
    def post(self):
        jsn = {}
        data = request.data
        data = json.loads(data)

        code = data['code']
        to_email_verify = data['email']

        res = json.dumps(emailVerification(code = code,
                                           email = to_email_verify))
        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'),
               "message": res.get('message')}, res.get('status')

        return jsn   
