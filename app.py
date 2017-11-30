# ./app.py
from flask import Flask
from flask import request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/analyze')
def index():
	text = request.args.get('text')
	analyzer = SentimentIntensityAnalyzer()
	vs = analyzer.polarity_scores(text)
	return vs

if __name__ == "__main__":
	app.run()