import re
import nltk
from typing import Dict, List
from app.config import settings

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab', quiet=True)


class TextPreprocessor:
    
    def __init__(self):
        self.min_word_count = settings.min_word_count
        self.max_word_count = settings.max_word_count
    
    def clean_text(self, text: str) -> str:
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'[^\w\s.,!?\'-]', '', text)
        return text.strip()
    
    def tokenize_words(self, text: str) -> List[str]:
        words = re.findall(r'\b\w+\b', text.lower())
        return words
    
    def tokenize_sentences(self, text: str) -> List[str]:
        try:
            sentences = nltk.sent_tokenize(text)
            return [s.strip() for s in sentences if s.strip()]
        except Exception:
            sentences = re.split(r'[.!?]+', text)
            return [s.strip() for s in sentences if s.strip()]
    
    def calculate_word_count(self, text: str) -> int:
        words = self.tokenize_words(text)
        return len(words)
    
    def calculate_sentence_count(self, text: str) -> int:
        sentences = self.tokenize_sentences(text)
        return len(sentences)
    
    def estimate_speech_rate(self, word_count: int, assumed_duration_minutes: float = 1.0) -> float:
 
        if word_count < 100:
            assumed_duration_minutes = 0.5
        elif word_count > 200:
            assumed_duration_minutes = 1.5
        
        wpm = word_count / assumed_duration_minutes
        return round(wpm, 2)
    
    def process(self, text: str) -> Dict:
 
        cleaned_text = self.clean_text(text)
        words = self.tokenize_words(cleaned_text)
        sentences = self.tokenize_sentences(cleaned_text)
        word_count = len(words)
        sentence_count = len(sentences)
        wpm = self.estimate_speech_rate(word_count)
        
        return {
            'cleaned_text': cleaned_text,
            'words': words,
            'sentences': sentences,
            'word_count': word_count,
            'sentence_count': sentence_count,
            'wpm': wpm
        }
