from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import os
from time import sleep



app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/')
def homeSecond():
    return render_template('home.html')

@app.route('/links')
def links():
  return render_template('links.html')

@app.route('/projects')
def projects():
  return render_template('projects.html')

@app.route('/comingsoon')
def comingsoon():
  return render_template('comingsoon.html')

app.run(host='0.0.0.0', port=8080, debug=True)
