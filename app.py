# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import session
import model
import requests #To access our API
# -- Initialization section --
app = Flask(__name__)
## secret key for session (In production, you would set this key via an environment variable)
app.secret_key = b'HO\xf8\xff+\n\x1e\\~/;}'
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    session['username'] = 'bob'
    data = {
        
    }
    return render_template('index.html', data=data)
@app.route('/random')
def random_clue():
    clue = model.random_clue()
    data = {
        'clue':clue,
    }
    return render_template('clue.html',data=data)