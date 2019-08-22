from flask_restful import Resource
from flask import request, jsonify, make_response
import requests
from Scanner import Scanner
from custommodels import Report, User
from threading import Thread
from server import app
from emailer import sendemail
import datetime
from decorators import jwt_required
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
      return jsonify({'user':user.name, 'token':token, 'expires':'3600', 'success':True})
    else:
      return jsonify({'message':'Password verification failed.', 'success':False})
      
  
  def put(self):
    return
  
  def delete(self):
    return
