from typing import Dict, List, Set
from app.config import settings


class VocabularyAnalyzer:
    
    def __init__(self):
        self.filler_words = settings.filler_words
    
    def calculate_ttr(self, words: List[str]) -> float:

        if not words:
            return 0.0
        
        unique_words = set(words)
        ttr = (len(unique_words) / len(words)) * 100
        return round(ttr, 2)
    
    def detect_filler_words(self, text: str, words: List[str]) -> Dict:
  
        text_lower = text.lower()
        filler_count = 0
        filler_details = {}
        
        for filler in self.filler_words:
            count = text_lower.count(filler)
            if count > 0:
                filler_count += count
                filler_details[filler] = count
        
        filler_rate = (filler_count / len(words)) * 100 if words else 0.0
        
        return {
            'filler_count': filler_count,
            'filler_rate': round(filler_rate, 2),
            'filler_details': filler_details
        }
    
    def calculate_vocabulary_score(self, ttr: float) -> float:

        if ttr >= 70:
            return 90 + ((ttr - 70) / 30) * 10
        elif ttr >= 50:
            return 70 + ((ttr - 50) / 20) * 20
        elif ttr >= 30:
            return 50 + ((ttr - 30) / 20) * 20
        else:
            return (ttr / 30) * 50
    
    def calculate_clarity_score(self, filler_rate: float) -> float:

        if filler_rate == 0:
            return 100.0
        elif filler_rate <= 2:
            return 100 - (filler_rate * 5)
        elif filler_rate <= 5:
            return 90 - ((filler_rate - 2) * 6.67)
        else:
            return max(0, 70 - ((filler_rate - 5) * 10))
    
    def analyze(self, text: str, words: List[str]) -> Dict:

        ttr = self.calculate_ttr(words)
        vocabulary_score = self.calculate_vocabulary_score(ttr)
        filler_analysis = self.detect_filler_words(text, words)
        clarity_score = self.calculate_clarity_score(filler_analysis['filler_rate'])
        
        return {
            'ttr': ttr,
            'vocabulary_score': vocabulary_score,
            'filler_count': filler_analysis['filler_count'],
            'filler_rate': filler_analysis['filler_rate'],
            'filler_details': filler_analysis['filler_details'],
            'clarity_score': clarity_score
        }
