from flask import Flask, render_template
import requests
import wikipedia

app = Flask(__name__)
wikipedia.set_lang('simple')


@app.route('/', methods=['GET'])
def main():
    page_url = wikipedia.search('')
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
