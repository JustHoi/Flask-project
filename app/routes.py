from app import app
from flask import render_template, url_for

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/user/<username>')
def return_user_profile(username):
    return 'User, %s' % username
