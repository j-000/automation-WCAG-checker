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
        email = data.get('email')
        if not url:
            return jsonify({'message':'Url parameter missing.', 'level':'text-danger'})
        if not email:
            return jsonify({'message':'Email parameter missing.', 'level':'text-danger'})
        t = Thread(target=initializescan, kwargs={'url':url, 'email':email})
        t.start()
        threads.append(t)
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

    return

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
  def get(self):
    return jsonify({'verified':True})
    
  
  def post(self):
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    if not email:
      return jsonify({'message':'Email parameter can\'t be empty.', 'success':False})
    if not password:
      return jsonify({'message':'Password parameter can\'t be empty.', 'success':False})
    
    user = User.query.filter_by(email=email).first()
    if not user:
      return jsonify({'message':'User is not registered.', 'success':False})

    verify_password = user.check_password(password_to_compare=password)
    if verify_password:
      token = user.generate_session_token()
      return jsonify({'user':{'name':user.name, 'id': user.id}, 'token':token, 'expires':'3600', 'success':True, 'message':f'Welcome, {user.name}'})
    else:
      return jsonify({'message':'Password verification failed.', 'success':False})
      
  @jwt_required
  def put(self):
    return
  
  @jwt_required
  def delete(self):
    return

''' /api/v1/register'''
class Register(Resource):
  
  @admins_only
  @jwt_required
  def get(self):
    return jsonify({'m':'you are admin'})

  def post(self):
    data = request.get_json()
    print(data)
    if not data:
      return jsonify({'message':'Missing json data.', 'success':False})
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name:
      return jsonify({'message':'Name field is required.', 'success':False})
    if not email:
      return jsonify({'message':'Email field is required.', 'success':False})
    if not password:
      return jsonify({'message':'Password field is required.', 'success':False})

    already_registered = User.exists(email)
    if already_registered:
      return jsonify({'message': 'That email is already registered.'})          
    User(name, email, password)
    user = User.fetch(email=email)
    return jsonify({'message':'You have successfully registered.', 'success':True, 'user': {'id': user.id, 'name':user.name}})