import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = 'http://api.openweatherapp.org/data/2.5/weather?q=()&units=imperial&appid=c88c9c32bcfb7efbf075d5d544c6bdbd'
    return render_template('weather.html')
