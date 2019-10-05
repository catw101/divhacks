from flask import Flask, render_template
import requests
import wikipedia
from newsapi import NewsApiClient

app = Flask(__name__)
wikipedia.set_lang('simple')
newsapi = NewsApiClient(api_key='466f16c5dc2445eabe6a30991514a281')


@app.route('/', methods=['GET'])
def main():
    articles = []
    tech_article = newsapi.get_top_headlines(sources='techcrunch', page_size=1).get('articles')
    science_article = newsapi.get_top_headlines(sources='new-scientist', page_size=1).get('articles')
    math_article = newsapi.get_everything(q='math', sources='new-scientist', page_size=1).get('articles')
    politics_article = newsapi.get_everything(q='politics', sources='bbc-news', page_size=1).get('articles')
    articles.append(math_article)
    articles.append(politics_article)
    articles.append(tech_article)
    articles.append(science_article)
    return render_template('index.html', articles_list=articles)


def get_wiki(keyword):
    return None


def get_keyword(article):
    return None


@app.route('/tech.html')
def tech():
    articles = []
    tech_articles = newsapi.get_top_headlines(sources='techcrunch', page_size=20).get('articles')
    for article in tech_articles:
        articles.append(article)
    return render_template('tech.html', articles_list=articles)


@app.route('/math.html')
def math():
    articles = []
    math_articles = newsapi.get_everything(q='math', sources='new-scientist').get('articles')
    for article in math_articles:
        articles.append(article)
    return render_template('math.html', articles_list=articles)


@app.route('/science.html')
def science():
    articles = []
    science_articles = newsapi.get_top_headlines(sources='new-scientist', page_size=20).get('articles')
    for article in science_articles:
        articles.append(article)
    return render_template('science.html', articles_list=articles)


@app.route('/politics.html')
def politics():
    articles = []
    politics_articles = newsapi.get_everything(q='politics', sources='bbc-news', page_size=20).get('articles')
    for article in politics_articles:
        articles.append(article)
    return render_template('politics.html', articles_list=articles)


if __name__ == '__main__':
    app.run()
