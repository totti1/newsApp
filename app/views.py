from flask import render_template
from app import app
from .api_request import my_news

@app.route('/')
def home():
    myNewsData = my_news()
    return render_template('home.html', data= myNewsData)