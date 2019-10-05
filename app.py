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
    print(articles)
    return render_template('index.html', articles_list=articles)


def get_wiki(keyword):
    return None


def get_keyword(article):
    return None


@app.route('/tech.html')
def tech():
    return render_template('tech.html')


@app.route('/math.html')
def math():
    return render_template('math.html')


@app.route('/science.html')
def science():
    return render_template('science.html')


@app.route('/politics.html')
def politics():
    return render_template('politics.html')


if __name__ == '__main__':
    app.run()
