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









#class users(db.Model):
  #_id = db.Column('id', db.Integer, primary_key=True)
  #name = db.Column(db.String(100))
  #email = db.Column(db.String(100))

  #def __init__(self, name, email):
    #self.name = name
    #self.email = email
  
#@app.route('/user', methods=['POST', 'GET'])
#def user():
#  email = None
#  if 'user' in session:
#    user = session['user']
#
#    if request.method == 'POST':
#      email = request.form['email']
#      session['email'] = email
#      found_user = users.query.filter_by(name=user).first()
#      found_user.email = email
#      db.session.commit()
#    else:
#      if "email" in session:
#        email = session['email']
#      return render_template('user.html', email=email)
#    return redirect(url_for('home'))

#  else:
#    flash('Your are not logged in.')
#    return redirect(url_for('login'))

#@app.route('/login', methods=["POST", "GET"])
#def login():
#  if request.method == 'POST':
#    session.permanent = True
#    user = request.form['nm']
#    session['user'] = user

    ##-------Delete Users From Website/AdminView-------##
    #Delete the current users.sqlite3 while the replit is stopped than run it again and the adminview and the accounts (users) saved will be deleted and refreshed.
    ##-----------------------------------------##
    
#    found_user = users.query.filter_by(name=user).first()
#    if found_user:
#      session['email'] = found_user.email
#    else:
#      usr = users(user, '')
#      db.session.add(usr)
#      db.session.commit()

#    flash('Logged In Successfully!')
#    return redirect(url_for('user'))
#  else:
#    if 'user' in session:
#      flash(f'You are already logged in.')
#      return redirect(url_for('home'))
#      
#    return render_template("login.html")

#@app.route('/logout')
#def logout():
#  flash(f'Goodbye, you have successfully logged out!', 'info')
#  session.pop('user', None)
#  session.pop('email', None)
#  return redirect(url_for('login'))
