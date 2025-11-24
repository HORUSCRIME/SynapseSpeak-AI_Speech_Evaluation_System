from pydantic import BaseModel, Field, validator
from typing import List, Dict, Optional


class TranscriptRequest(BaseModel):
    transcript: str = Field(..., min_length=10, max_length=5000)
    
    @validator('transcript')
    def validate_transcript(cls, v):
        if not v.strip():
            raise ValueError('Transcript cannot be empty')
        return v.strip()


class CriterionScore(BaseModel):
    criterion: str
    score: float
    max_score: float
    feedback: str
    weight: float
    percentage: float = Field(default=0.0)
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.max_score > 0:
            self.percentage = (self.score / self.max_score) * 100


class DetailedAnalysis(BaseModel):
    keywords_found: List[str]
    keywords_missing: List[str]
    grammar_errors: int
    grammar_error_rate: float
    filler_words_count: int
    filler_word_rate: float
    sentiment_score: float
    vocabulary_richness: float
    speech_rate_wpm: float
    salutation_detected: Optional[str] = None


class EvaluationResponse(BaseModel):
    overall_score: float
    grade: str
    word_count: int
    sentence_count: int
    criteria_scores: List[CriterionScore]
    detailed_analysis: DetailedAnalysis
    summary: str
    
    @validator('grade', always=True)
    def calculate_grade(cls, v, values):
        if 'overall_score' not in values:
            return 'N/A'
        
        score = values['overall_score']
        if score >= 90:
            return 'A+'
        elif score >= 85:
            return 'A'
        elif score >= 80:
            return 'B+'
        elif score >= 75:
            return 'B'
        elif score >= 70:
            return 'C+'
        elif score >= 65:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'


class HealthResponse(BaseModel):
    status: str
    version: str
    models_loaded: bool
