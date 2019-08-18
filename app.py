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


from apimodels import (Scan, ScannReports)
base_api_url = '/api/v1'
api.add_resource(Scan, f'{base_api_url}/scans')
api.add_resource(ScannReports, f'{base_api_url}/reports/<reportid>')




@app.route('/api/register', methods=['POST'])
def register():
    # Get request data
    request_data = request.get_json();
    if request_data:
        # Handle request data
        name = request_data.get('name')
        email = request_data.get('email')
        # Check all parameters are present
        if not name or not email:
            return jsonify({'error':'You need to provide a name and an email to register.'})
        # Check whether user already exists
        if User.exists(email):
            return jsonify({'info':'That email is already registered.'})
        # Creates user
        User(name, email)
        # Fetch new user
        user = User.exists(email)
    # Return new user created
    return jsonify({'success':True, 'info':'User created successfully.', 'user_id': user.id, 'email': user.email})


@app.route('/api/checkpoints', methods=['GET', 'POST'])
def checkpoints():
    if request.method == 'POST':
        request_data = request.get_json()
        id = request_data.get('id')
        name = request_data.get('name')
        wcaglevels = request_data.get('wcaglevels')
        benefits = request_data.get('benefits')
        regex = request_data.get('regex')
        # Check all parameters are present
        _params = [id, name, wcaglevels, benefits, regex]
        for _p in _params:
            if not _p:
                return jsonify({'error':f'You must specify "id:int", "name:str", "wcaglevels:str", "benefits:str" and "regex:str".'})
        # Check whether the id is valid
        checkpoint = Checkpoint.get(id)
        if checkpoint:
            return jsonify({'error': 'That checkpoint id already exists.'})  
        # Checkpoint creation
        try:
            Checkpoint(id, name, wcaglevels, benefits, regex)
            checkpoint = Checkpoint.get(id)
            return jsonify({'success':True, 'checkpoint': checkpoint, 'message': 'Checkpoint added successfully.'})
        # Handle any exception - this mght be due to SQL constrains
        except BaseException as e:
            return jsonify({'error': 'Creation failed.'})
    # Get request, send all checkpoints
    all_checkpoints = Checkpoint.get_all()
    return jsonify({'checkpoints':all_checkpoints})


@app.route('/api/scann', methods=['POST'])
def scann():
    # Get request data
    request_data = request.get_json()
    if request_data:
        url = request_data.get('url')
        # Get all checkpoints
        checkpoints = Checkpoint.get_all()
        # Initialise the Scanner class
        scan = Scanner(checkpoints)
        # Run scan method with url from request form
        response = scan.scan(url)
        if 'error' in response:
            return jsonify({'error': f'Request to {url} failed.'})
    # Return response and results from scanner
    return jsonify({'success': True, 'results': [{ 'id':e, 'info':response[e]} for e in response] })



if __name__ == "__main__": 
    if DEVELOPMENT:
        app.run(debug=True)
    else:
        app.run()