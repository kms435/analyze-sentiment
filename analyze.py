from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

class Analyzer():
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()

    def result(self, text):
        return str(self.analyzer.polarity_scores(text))