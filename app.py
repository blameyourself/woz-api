#dependencies import
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

#import login file
from src.Auth.login import Login
from src.profile.create_user_profile import UserCredential
from src.profile.create_user_uploadid import UserUploadFile
from src.profile.user_email_verify import UserEmailVerify

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


api.add_resource(Login, '/vs/login')
api.add_resource(UserCredential,'/vs/create_user')
api.add_resource(UserUploadFile,'/vs/upload_file')
api.add_resource(UserEmailVerify,'/vs/email_verification')

if __name__ == '__main__':
   app.run(debug = True)