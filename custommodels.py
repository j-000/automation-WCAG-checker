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
    token = db.Column(db.Text())

    def __repr__(self):
        return '{id} - {name}'.format(id=self.id, name=self.name)
    
    def __init__(self, name, email, password):
        exists = User.query.filter_by(email=email).first()
        if exists:
            return
        self.name = name
        self.email = email
        self.password = generate_password_hash(password, method="pbkdf2:sha256", salt_length=8)
        db.session.add(self)
        db.session.commit()
        return

    def check_password(self, password_to_compare):
        return check_password_hash(self.password, password_to_compare)


    @staticmethod
    def exists(email):
        return User.query.filter_by(email=email).first()

    def generate_session_token(self, expires_in=3600):
        # DO NOT rename 'exp' flag. This is used inside jwt.encode() to verify if the token has expired.
        token = jwt.encode({'user_email': self.email, 'id' : self.id , 'exp': time() + expires_in}, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
        self.token = token
        db.session.commit()
        return token

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

    def verify_session_token(self, token):
        usertoken = self.decode_token(token)
        if usertoken.id != self.id:
            return False
        if self.token != token:
            return False
        return True

    def delete_token(self):
        self.token = None
        db.session.add(self)
        db.session.commit()


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

    def __str__(self):
        return f'{self.id} - {self.name}'
    
    def __init__(self, id, name, wcaglevels, benefits, regex):
        self.id = id
        self.name = name
        self.wcaglevels = wcaglevels
        self.benefits = benefits
        self.regex = regex
        db.session.add(self)
        db.session.commit()
        return

    @staticmethod
    def get(id):
        c = Checkpoint.query.get(id)
        if c:
            checkpoint_object = {
                'id':c.id, 
                'name':c.name,
                'wcaglevels':c.wcaglevels, 
                'benefits':c.benefits,
                'regex':c.regex
                }
            return checkpoint_object
        return None
    
    @staticmethod
    def get_all():
        checkpoints_array = [{
            'id':c.id, 
            'name':c.name,
            'wcaglevels':c.wcaglevels, 
            'benefits':c.benefits,
            'regex':c.regex
            } for c in Checkpoint.query.all()]
        return checkpoints_array


class Report(db.Model):
  __tablename__ = 'reports'

  id = db.Column(db.Integer, primary_key=True)
  url = db.Column(db.Text())
  results = db.Column(db.Text())
  hashid = db.Column(db.String(200))

  def __init__(self, url):
    self.url = url
    reportstring = f'{url}-{str(datetime.datetime.now())}-{randint(0, 1000)}'
    self.hashid = hashlib.sha256(reportstring.encode('utf-8')).hexdigest()
    return
  
  @staticmethod
  def fetch(reportid):
    return Report.query.filter_by(hashid=reportid).first()
  
  def update_results(self, results):
    self.results = results
    db.session.add(self)
    db.session.commit()
    return self

  def get_json_results(self):
    return json.loads(self.results.replace("'",'"'))