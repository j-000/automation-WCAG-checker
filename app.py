from server import app
from flask import jsonify, request
from devsettings import DEVELOPMENT
from flask_login import login_required, current_user, LoginManager, login_user, logout_user

from custommodels import User

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


@app.route('/api/register', methods=['POST'])
def register():
    request_data = request.get_json();
    if request_data:
        name = request_data.get('name')
        email = request_data.get('email')

        if not name or not email:
            return jsonify({'error':'You need to provide a name and an email to register.'})

        if User.exists(email):
            return jsonify({'info':'That email is already registered.'})

        User(name, email)
        user = User.exists(email)
    return jsonify({'success':True, 'info':'User created successfully.', 'user_id': user.id, 'email': user.email})







@app.route('/api/ping')
def ping():
    return jsonify({'pong': True})








if __name__ == "__main__": 

    if DEVELOPMENT:
        app.run(debug=True)
    else:
        app.run()