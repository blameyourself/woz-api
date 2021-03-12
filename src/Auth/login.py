"""Do something Here!"""
from flask_restful import Resource, request
from flask import jsonify
import os
import json
from include.Auth.login_function import LoginFunction

class Login(Resource):
    def post(self):
        data = request.data
        data = json.loads(data)
        
        email = data['email']
        password = data['password']

        res = json.dumps(LoginFunction(email, password))
        res = json.loads(res)
        res = res[0]
        
        jsn = {"status": res.get('status'), 
               "message": res.get('message'), 
               "body": res.get('body') }, res.get('status')

        return jsn
        