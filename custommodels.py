from sqlalchemy import desc, asc
from flask_login import UserMixin
from server import db


'''
User Class
'''
class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    email = db.Column(db.String(50))

    def __repr__(self):
        return '{id} - {name}'.format(id=self.id, name=self.name)
    
    def __init__(self, name, email):
        self.name = name
        self.email = email
        db.session.add(self)
        db.session.commit()
        return

    @staticmethod
    def exists(email):
        return User.query.filter_by(email=email).first()