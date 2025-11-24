from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import Dict


class SentimentAnalyzer:
    
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
    
    def analyze_sentiment(self, text: str) -> Dict:

        scores = self.analyzer.polarity_scores(text)
        
        compound = scores['compound']
        positive = scores['pos']
        negative = scores['neg']
        neutral = scores['neu']

        engagement_score = self._calculate_engagement_score(compound, positive)
        
        sentiment_label = self._get_sentiment_label(compound)
        
        return {
            'compound': compound,
            'positive': positive,
            'negative': negative,
            'neutral': neutral,
            'engagement_score': engagement_score,
            'sentiment_label': sentiment_label
        }
    
    def _calculate_engagement_score(self, compound: float, positive: float) -> float:

        compound_normalized = ((compound + 1) / 2) * 100
        
        positive_normalized = positive * 100
        
        engagement = (compound_normalized * 0.7) + (positive_normalized * 0.3)
        
        return round(engagement, 2)
    
    def _get_sentiment_label(self, compound: float) -> str:
        if compound >= 0.5:
            return "Very Positive"
        elif compound >= 0.1:
            return "Positive"
        elif compound >= -0.1:
            return "Neutral"
        elif compound >= -0.5:
            return "Negative"
        else:
            return "Very Negative"
