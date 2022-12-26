from email.policy import default
from sqlalchemy import ForeignKey
from extensions import db, login_manager
from app import app as app
from flask_login import UserMixin
from flask_security import UserMixin, RoleMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


# News table
class News(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.Date, nullable=True, default=datetime.now())
    news_content = db.Column(db.Text, nullable = False)


    def __repr__(self):
        return self.title

    def add(self):
        db.session.add(self)
        db.session.commit()




roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer,
                       db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer,
                       db.ForeignKey('role.id'))
                    )


# User table
class User(db.Model, UserMixin):
    id  = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users'), lazy='dynamic')


# Role table
class Role(db.Model, RoleMixin):
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)



class LoanRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    job = db.Column(db.String(30), nullable = False)
    prefix = db.Column(db.String(30), nullable = False)
    p_number = db.Column(db.String(30), nullable = False)
    def __repr__(self):
        return self.first_name
    def add(self):
        db.session.add(self)
        db.session.commit()
class CardRequest(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    card = db.Column(db.String(30), nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False)
    code=db.Column(db.Integer, nullable = False)
    prefix = db.Column(db.String(30), nullable = False)
    p_number = db.Column(db.String(30), nullable = False)
    branch = db.Column(db.String(30), nullable = False)
    file1=db.Column(db.String(255), nullable = False)
    file2=db.Column(db.String(255), nullable = False)
    def __repr__(self):
        return self.card
    def add(self):
        db.session.add(self)
        db.session.commit()
class Cards(db.Model):
    card_id = db.Column(db.Integer, primary_key = True)
    card_header = db.Column(db.String(30), nullable = False)
    card_info = db.Column(db.Text, nullable = False)
    term = db.Column(db.String(30), nullable = False)
    currency = db.Column(db.String(30), nullable = False)
    cashback = db.Column(db.String(30), nullable = False)
    def __repr__(self):
        return self.title
    def add(self):
        db.session.add(self)
        db.session.commit()
class Loans(db.Model):
    loan_id = db.Column(db.Integer, primary_key = True)
    loan_header = db.Column(db.String(30), nullable = False)
    loan_info = db.Column(db.Text, nullable = False)
    amount = db.Column(db.String(30), nullable = False)
    term = db.Column(db.String(30), nullable = False)
    int_payment = db.Column(db.String(30), nullable = False)
    def __repr__(self):
        return self.title
    def add(self):
        db.session.add(self)
        db.session.commit()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)