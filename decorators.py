from functools import wraps
from flask import request, jsonify
from custommodels import User

def admins_only(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    auth_token = request.headers.get('Authorization').split()[1]
    user = User.decode_token(auth_token)
    if not user.is_admin:
      return jsonify({'success':False, 'message':'This is only available to admins.'})
    return f(*args, **kwargs)
    
  return wrapper


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
    # A user was found with the token so all is good. 
    # (yes, someone can use someone else's token, but how would they get it?)
    return f(*args, **kwargs, token=auth_token, user=user)
  return wrapper