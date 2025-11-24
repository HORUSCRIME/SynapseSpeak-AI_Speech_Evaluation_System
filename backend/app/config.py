from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import field_validator
from typing import List, Union
import os


class Settings(BaseSettings):
    
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_parse_none_str='null'
    )
    
    environment: str = "development"
    
    allowed_origins: Union[str, List[str]] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000"
    ]
    
    @field_validator('allowed_origins', mode='before')
    @classmethod
    def parse_allowed_origins(cls, v):
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(',')]
        return v
    
    model_cache_dir: str = "./models"
    sentence_transformer_model: str = "all-MiniLM-L6-v2"
    
    optimal_wpm_min: int = 120
    optimal_wpm_max: int = 150
    min_word_count: int = 50
    max_word_count: int = 500
    
    max_grammar_errors_per_100_words: float = 5.0
    
    filler_words: List[str] = [
        "um", "uh", "like", "you know", "basically", "actually",
        "literally", "sort of", "kind of", "i mean", "well"
    ]
    
    salutation_keywords: List[str] = [
        "hello", "hi", "good morning", "good afternoon", "good evening",
        "greetings", "hey", "namaste"
    ]
    
    personal_info_keywords: dict = {
        "name": ["name", "called", "i'm", "i am"],
        "age": ["age", "years old", "year old"],
        "school": ["school", "studying", "student"],
        "grade": ["grade", "class", "standard"],
        "family": ["family", "parents", "siblings", "brother", "sister", "mother", "father"]
    }
    
    hobbies_keywords: List[str] = [
        "hobby", "hobbies", "like", "love", "enjoy", "interested",
        "passion", "favorite", "play", "read", "draw", "dance", "sing"
    ]


settings = Settings()


