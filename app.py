from server import app, api
from flask import jsonify, request
from flask_login import LoginManager
from custommodels import User, Checkpoint
from Scanner import Scanner
from devsettings import DEVELOPMENT


# initiate the user loader
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'


# user loader functions
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


# Unauthorised handler
@login_manager.unauthorized_handler
def unauthorized():
  return jsonify({'error': 'You must login first in order to access that route.'})


from apimodels import (Scan, ScanReport, UserReports, Authentication, Register)
base_api_url = '/api/v1'
api.add_resource(Scan, f'{base_api_url}/scans')
api.add_resource(UserReports, f'{base_api_url}/user/<userid>/reports')
api.add_resource(ScanReport, f'{base_api_url}/user/<userid>/reports/<reporthid>')
api.add_resource(Authentication, f'{base_api_url}/authenticate')
api.add_resource(Register, f'{base_api_url}/register')



@app.route('/', defaults={'path':''})
@app.route('/<path:path>')
def home(path):
    return "Nothing to see here :) @j-000"

if __name__ == "__main__": 
    if DEVELOPMENT:
        app.run(debug=True)
    else:
        app.run()