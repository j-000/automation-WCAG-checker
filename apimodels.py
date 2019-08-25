from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
from Scanner import Scanner
from custommodels import Report, User
from threading import Thread
from server import app
from emailer import sendemail
import datetime
from decorators import jwt_required, admins_only
import hashlib

threads = []


def initializescan(url, email):
    report = Report(url)
    scanner = Scanner()
    try:
        results = scanner.scan(url)
        report.update_results(str(results))
    except Exception as e:
        report.update_results(str(e))

    with app.app_context():
        emailtext = f'''
        Your report is ready.\n
        Simply follow the link below to see your website's results.
        \n\n
        http://allgreencode.s3-website.eu-west-2.amazonaws.com/reports/{report.hashid}
        \n\n
        www.allgreencode.com
        '''
        sendemail(f'Your scan is ready! - {str(datetime.datetime.today())}', recipients=[email], email_text=emailtext)    
    return


'''/api/v1/scans'''
class Scan(Resource):

    def get(self):
        return jsonify({'threads': [{'name':t.name, 'alive':t.is_alive()}  for t in threads]})
    
    @jwt_required
    def post(self):
        data = request.get_json()
        url = data.get('url')
        if not url:
            return jsonify({'message':'Url parameter missing.', 'level':'text-danger'})
        
        token = request.headers.get('Authorization').split()[1]
        user = User.decode_token(token)
        Report(url, user.id)
        
        # t = Thread(target=initializescan, kwargs={'url':url, 'email':email})
        # t.start()
        # threads.append(t)
        return jsonify({'message':'Scan started. You will receive an email with a unique link to your results.', 'level':'text-success'})
    
    def put(self):
        return
    
    def delete(self):
        return


'''/api/v1/user/<userid>/reports'''
class UserReports(Resource):

  @jwt_required
  def get(self, userid):
    try:
      user = User.query.filter_by(id=int(userid)).first()
    except Exception as e:
      return jsonify({'message':'Invalid user id.', 'success':False})

    return jsonify({'reports': [f'{r.id}' for r in user.reports]})

  @jwt_required  
  def post(self, userid):
      return

  @jwt_required  
  def put(self, userid):
      return

  @jwt_required  
  def delete(self, userid):
      return


'''/api/v1/reports/<reportid>'''
class ScanReport(Resource):

    @jwt_required
    def get(self, reportid):
        report = Report.fetch(reportid)
        if report:
            return jsonify({'message': 'Report found.', 'id':report.hashid, 'results': report.get_json_results()})
        return jsonify({'message': 'No report found with that id.'})
    
    def post(self, reportid):
        return
    
    def put(self, reportid):
        return
    
    def delete(self, reportid):
        return








'''/api/v1/authenticate'''
class Authentication(Resource):

  @jwt_required
  def get(self, token, user):
    '''
    Verify session
    '''
    # token and user are received from the decorator
    if user.token != token:
      return jsonify({'message':'You are not logged in.', 'success':False})
    return jsonify({'verified':True})
    
  def post(self):
    '''
    Login user
    '''
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    for param, var in [('data',data),('email',email),('password',password)]:
      if not var:
        return jsonify({'message':f'{param} field is missing.', 'success':False})

    user = User.query.filter_by(email=email).first()
    if not user:
      return jsonify({'message':'User is not registered.', 'success':False})

    verify_password = user.check_password(password_to_compare=password)
    if verify_password:
      token = user.generate_session_token()
      return jsonify({'user':{'name':user.name, 'id': user.id, 'admin':user.is_admin}, 'token':token, 'expires':'3600', 'success':True, 'message':f'Welcome, {user.name}'})
    else:
      return jsonify({'message':'Password verification failed.', 'success':False})
      
  @jwt_required
  def put(self):
    return
  
  @jwt_required
  def delete(self, token, user):
    # token and user are received from the decorator
    if user.token != token:
      return jsonify({'message':'You are not logged in.', 'success':False})
    return jsonify({'message':'Logout complete', 'success':True, 'token':token})



''' /api/v1/register'''
class Register(Resource):
  
  @jwt_required
  def get(self):
    return

  def post(self):
    ''' 
    Register new user. 
    '''
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    for param, var in [('data', data), ('name', name), ('email', email), ('password', password)]:
      if not var:
        return jsonify({'message': f'{param} field missing.', 'success':False})

    already_registered = User.exists(email)
    if already_registered:
      return jsonify({'message': 'That email is already registered.', 'success':False})

    User(name, email, password)
    user = User.fetch(email=email)
    return jsonify({'message':'You have successfully registered.', 'success':True, 'token': user.generate_session_token()})

  @jwt_required
  def put(self):
    return
  
  @jwt_required
  def delete(self, token, user):
    # token and user are received from the decorator
    if user.token != token:
      return jsonify({'message':'You are not logged in.', 'success':False})
    User.delete(user)
    return jsonify({'message':'Account deleted.', 'success':True})