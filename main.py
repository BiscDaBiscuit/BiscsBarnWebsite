from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import os
from flask_sqlalchemy import SQLAlchemy
from time import sleep

app = Flask(__name__)
app.secret_key = os.getenv("secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=30)
db = SQLAlchemy(app)



@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/')
def homeSecond():
    return render_template('home.html')

@app.route('/links')
def links():
  return render_template('links.html')

@app.route('/comingsoon')
def comingsoon():
  return render_template('comingsoon.html')

db.create_all()
app.run(host='0.0.0.0', port=8080, debug=True)
