from flask_restful import Resource, request
from include.profile.create_user_uploadid_func import addUserFileUpload
from werkzeug.utils import secure_filename
from src.profile.fileUploadSecurity import allowed
from flask import jsonify
import os
import json

class UserUploadFile(Resource):
   
    def post(self):
        data = []
        data = request.data
        data = json.loads(data)
        
        token = data.get('token')
        fileUpload = data.get('file')
       

        res = json.dumps(addUserFileUpload(token = token, fileUpload = fileUpload))

        res = json.loads(res)
        res = res[0]

        jsn = {"status": res.get('status'),
                        "message": res.get('message')}, res.get('status')

        return jsn
        
       