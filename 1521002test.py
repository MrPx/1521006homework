import unittest
# from hello import Users
import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
moment = Moment(app)
db = SQLAlchemy(app)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    age = db.Column(db.String(64), unique=True, index=True)
	
    def __init__(self, username='1521002杜烺钰', age=20):
        self.username = username
        self.age = 20
		
    def __repr__(self):
        return '<User %r>' % self.username

class TestHelloCase(unittest.TestCase):
    
    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.drop_all()
        
    def test_add1(self):
        user1 = Users('1521002杜烺钰')
        db.session.add(user1)
        db.session.commit()
        retUser = Users.query.first()
        self.assertEqual(retUser.username, '1521002杜烺钰')
    
    def test_add2(self):
        user2 = Users('1521002杜烺钰')
        self.assertEqual(user2.age, 20)
		
    def test_add3(self):
        user3 = Users('1521002杜烺钰')
        user3.age = 24
        self.assertEqual(user3.age, 24)

if __name__ == '__main__':
unittest.main()
