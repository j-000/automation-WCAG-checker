from sqlalchemy import desc, asc
from flask_login import UserMixin
from server import db, app
import json
import hashlib
from werkzeug.security import check_password_hash, generate_password_hash
import datetime
from random import randint
import jwt
from time import time


'''
User Class
'''
class User(db.Model, UserMixin):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(25), nullable=False)
  email = db.Column(db.String(50), nullable=False)
  password = db.Column(db.Text(), nullable=False)
  scan_quota = db.Column(db.Integer(), default=31)
  is_admin = db.Column(db.Boolean(), default=False)
  has_premium = db.Column(db.Boolean(), default=False)
  token = db.Column(db.Text())
  invoices = db.relationship('Invoice', backref='user', lazy=True, cascade="all,delete")
  scans = db.relationship('Scan', backref='user', lazy=True, cascade="all,delete")

  def __repr__(self):
    return '{id} - {name}'.format(id=self.id, name=self.name)
  
  def __init__(self, name, email, password):
    if self.exists(email):
        return
    self.name = name
    self.email = email
    self.password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
    db.session.add(self)
    db.session.commit()
    return
  
  @staticmethod
  def decode_token(token):
    try:
      tk = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
      return False
    except Exception as e:
      return False
    usertoken = User.query.filter_by(email=tk['user_email']).first()
    if not usertoken:
      return False
    return usertoken

  @staticmethod
  def fetch(email=None, id=None):
    if not email and not id:
      raise 'Required params: Email or Id'
    if email:
      return User.query.filter_by(email=email).first()
    if id:
      return User.query.get(id)

  @staticmethod
  def exists(email):
    return User.query.filter_by(email=email).first()

  @staticmethod
  def delete(user):
    db.session.delete(user)
    db.session.commit()
    return

  def check_password(self, password_to_compare):
    return check_password_hash(self.password, password_to_compare)

  def generate_session_token(self, expires_in=3600):
    # DO NOT rename 'exp' flag. This is used inside jwt.encode() to verify if the token has expired.
    token = jwt.encode({'user_email': self.email, 'id' : self.id , 
    'exp': time() + expires_in}, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    self.token = token
    db.session.commit()
    return token

  def delete_token(self):
    self.token = None
    db.session.add(self)
    db.session.commit()

  def start_new_scan(self, checkpoints, url, alias):
    Scan(self.id, url, alias, checkpoints)
    self._reduce_scan_quota()
    return
  
  def add_premium(self):
    self.has_premium = True
    db.session.add(self)
    db.session.commit()
    return
  
  def remove_premium(self):
    self.has_premium = False
    db.session.add(self)
    db.session.commit()
    return
  
  def _reduce_scan_quota(self):
    self.scan_quota -= 1
    db.session.add(self)
    db.session.commit()
    return


'''
Scan Class
'''
class Scan(db.Model):
  __tablename__ = 'scans'

  id = db.Column(db.Integer, primary_key=True)
  timestamp = db.Column(db.DateTime(), default=datetime.datetime.now())
  finished = db.Column(db.DateTime(), default=None, nullable=True)
  report = db.relationship('Report', backref='scan', lazy=True, cascade="all,delete", uselist=False)
  checkpoints = db.relationship('Checkpoint', backref='scan', lazy=True, cascade='all,delete')
  hashid = db.Column(db.String(200), nullable=False)
  userid = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)
  url = db.Column(db.Text())
  alias = db.Column(db.String(200))

  def __repr__(self):
    return f'[Scan] #{self.id}'

  def __init__(self, userid, url, alias, checkpoints):
    reportstring = f'{url}-{str(datetime.datetime.now())}-{randint(0, 1000)}'
    self.hashid = hashlib.sha256(reportstring.encode('utf-8')).hexdigest()
    self.userid = userid
    self.url = url
    self.alias = alias
    self._add_checkpoints(checkpoints)
    return

  def _add_checkpoints(self, checkpoints):
    for checkpoint in checkpoints:
      self.checkpoints.append(checkpoint)
    db.session.add(self)
    db.session.commit()
    return
  
  def update_scan_status(self):
    self.finished = datetime.datetime.now()
    db.session.add(self)
    db.session.commit()
    return
  
  def add_report(self, seo, accessibility, usability, results):
    Report(self.id, seo, accessibility, usability, results)
    return


'''
Invoice Class
'''
class Invoice(db.Model):
  __tablename__ = 'invoices'

  id = db.Column(db.Integer, primary_key=True)
  datetime = db.Column(db.DateTime(), default=datetime.datetime.now())
  ispaid = db.Column(db.Boolean(), default=False)
  paymentconfirmationid = db.Column(db.String(50))
  discount = db.Column(db.Float(), default=0)
  amountdue = db.Column(db.Float(), nullable=False)
  tax = db.Column(db.Float(), nullable=False)
  description = db.Column(db.Text(), nullable=False)
  userid = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable=False)

  def __repr__(self):
    return f'[Invoice] #{self.id}: On: {self.datetime} Due: {self.amountdue} Paid: {self.ispaid}'

  def __init__(self, amountdue, tax, description, userid):
    self.amountdue = amountdue
    self.tax = tax
    self.description = description
    self.userid = userid
    db.session.add(self)
    db.session.commit()
    return
  
    
'''
Checkpoint Class
'''
class Checkpoint(db.Model):
  __tablename__ = 'checkpoints'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.Text())
  wcaglevels = db.Column(db.String(20))
  benefits = db.Column(db.String(40))
  regex = db.Column(db.Text())
  scanid = db.Column(db.Integer(), db.ForeignKey('scans.id'), nullable=True)

  def __str__(self):
    return f'{self.id} - {self.name}'
  
  def __init__(self, name, wcaglevels, benefits, regex, scanid):
    self.name = name
    self.wcaglevels = wcaglevels
    self.benefits = benefits
    self.regex = regex
    self.scanid = scanid
    db.session.add(self)
    db.session.commit()
    return



'''
Report Class
'''
class Report(db.Model):
  __tablename__ = 'reports'

  id = db.Column(db.Integer, primary_key=True)
  results = db.Column(db.Text())
  seo = db.Column(db.Float())
  accessibility = db.Column(db.Float())
  usability = db.Column(db.Float())
  scanid = db.Column(db.Integer, db.ForeignKey('scans.id'), nullable=False)

  def __init__(self, scanid, seo, accessibility, usability, results):
    self.scanid = scanid
    self.seo = seo
    self.accessibility = accessibility
    self.usability = usability
    self.results = results
    db.session.add(self)
    db.session.commit()
    return

  def get_json_results(self):
    if self.results:
      return json.loads(self.results.replace("'",'"'))
    return None
