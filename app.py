# ./app.py
from flask import (Flask, jsonify, render_template)
from flask import request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
	text = "hello what is your name"
	analyzer = SentimentIntensityAnalyzer()
	vs = analyzer.polarity_scores(text)
	return str(vs)

@app.route('/analyze')
def analyze():
	text = request.args.get('text')
	analyzer = SentimentIntensityAnalyzer()
	vs = analyzer.polarity_scores(text)
	return str(vs)

if __name__ == "__main__":
	app.run()