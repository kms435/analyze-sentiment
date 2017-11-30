# ./app.py
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/analyze')
def index():
	text = request.args.get('text')
	return text

if __name__ == "__main__":
	app.run()