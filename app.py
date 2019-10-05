from flask import Flask, render_template
import requests
import wikipedia

app = Flask(__name__)
wikipedia.set_lang('simple')


@app.route('/index.html', methods=['GET'])
def main():
    page_title = wikipedia.search('tropical storm barry')[0]
    page = wikipedia.page(page_title)
    return render_template('index.html', title=page_title, link=page.url, summary=page.summary)

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
