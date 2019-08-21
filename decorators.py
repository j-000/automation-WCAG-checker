from functools import wraps
from flask import request, jsonify
from custommodels import User


def jwt_required(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    # get auth header
    auth_header = request.headers.get('Authorization')
    # decline if not implemented
    if not auth_header:
      return jsonify({"message": "No authorization header defined.", 'success':False})
    # try to slit and get the token
    try:
      auth_token = auth_header.split()[1]
    # decline if no token found
    except:
      return jsonify({"message": "No token found in authorization header.", 'success':False})
    # try get the user from the token payload
    user = User.decode_token(auth_token)
    # deline if no user found with the payload data (email)
    if not user:
        return jsonify({'message':'Invalid or expired token.', 'success':False})
    # verify if the token is valid for the user found:
    # when loggin in the token is set in the user model along with sid
    validtoken = user.verify_session_token(auth_token)
    # decline if the token is not valid for the user
    if not validtoken:
        return jsonify({'message':'Invalid or expired token','success':False})
    # ALL CLEAR
    return f(*args, **kwargs)
    
  return wrapper