# ./app.py
from flask import Flask
# from analyze import Analyzer

app = Flask(__name__)

@app.route('/')
def index():
	result = "I hate your guts"
	# vader = Analyzer()
	# result = vader.result(text)
	return result

# @app.route('/analyze')
# def analyze():
# 	text = request.args.get('text')
# 	analyzer = SentimentIntensityAnalyzer()
# 	vs = analyzer.polarity_scores(text)
# 	return str(vs)

if __name__ == "__main__":
	app.run()