from flask_restful import Resource, request
from include.profile.create_user_profile_func import addUserCredential
from flask import jsonify
import os
import json

class UserCredential(Resource):
    def post(self):
        jsn = {}
        data = request.data
        data = json.loads(data)

        fullname = data['fullname']
        emailadd = data['email']
        password = data['password']
        birthdate = data['birthdate']
        gender = data['gender']
        address = data['address']
        country = data['country']
      
        res = json.dumps(addUserCredential(fullname = fullname,
                                           email = emailadd,
                                           password = password,
                                           birtdate = birthdate, 
                                           gender = gender, 
                                           address = address, 
                                           country = country))
        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'),
               "message": res.get('message')}, res.get('status')

        return jsn   
