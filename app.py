from flask import Flask, render_template
import requests
import wikipedia

app = Flask(__name__)
wikipedia.set_lang('simple')


@app.route('/', methods=['GET'])
def main():
    page_title = wikipedia.search('tropical storm barry')[0]
    page = wikipedia.page(page_title)
    return render_template('index.html', title=page_title, link=page.url, summary=page.summary)


if __name__ == '__main__':
    app.run()
