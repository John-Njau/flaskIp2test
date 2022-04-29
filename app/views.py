from unicodedata import name
from flask import render_template
from .requests import get_news

from app import app

@app.route('/')
def home():
    name= 'NEWS ROOM'
    title= "News Room -- For all news all over the world."
    news_outlet = get_news('popularity')
    print(news_outlet)
    
    return render_template('index.html', name=name, title=title, news_outlet=news_outlet )

@app.route('/news')
def news():
    return render_template('news.html')