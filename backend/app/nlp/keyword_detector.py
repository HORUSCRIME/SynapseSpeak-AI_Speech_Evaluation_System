import re
from typing import Dict, List, Set
from app.config import settings


class KeywordDetector:
    
    def __init__(self):
        self.salutation_keywords = settings.salutation_keywords
        self.personal_info_keywords = settings.personal_info_keywords
        self.hobbies_keywords = settings.hobbies_keywords
    
    def detect_salutation(self, text: str) -> tuple[bool, str]:
  
        text_lower = text.lower()
        
        for keyword in self.salutation_keywords:
            if keyword in text_lower:
                return True, keyword.title()
        
        return False, ""
    
    def detect_personal_info(self, text: str, words: List[str]) -> Dict[str, bool]:

        text_lower = text.lower()
        results = {}
        
        for category, keywords in self.personal_info_keywords.items():
            found = False
            for keyword in keywords:
                if keyword in text_lower:
                    found = True
                    break
            results[category] = found
        
        return results
    
    def detect_hobbies(self, text: str) -> bool:

        text_lower = text.lower()
        
        for keyword in self.hobbies_keywords:
            if keyword in text_lower:
                return True
        
        return False
    
    def get_keywords_summary(self, text: str, words: List[str]) -> Dict:

        salutation_found, salutation_text = self.detect_salutation(text)
        personal_info = self.detect_personal_info(text, words)
        hobbies_found = self.detect_hobbies(text)
        
        found_keywords = []
        missing_keywords = []
        
        if salutation_found:
            found_keywords.append("salutation")
        else:
            missing_keywords.append("salutation")
        
        for category, found in personal_info.items():
            if found:
                found_keywords.append(category)
            else:
                missing_keywords.append(category)
        
        if hobbies_found:
            found_keywords.append("hobbies")
        else:
            missing_keywords.append("hobbies")
        
        return {
            'salutation_found': salutation_found,
            'salutation_text': salutation_text,
            'personal_info': personal_info,
            'hobbies_found': hobbies_found,
            'keywords_found': found_keywords,
            'keywords_missing': missing_keywords,
            'completeness_score': len(found_keywords) / (len(found_keywords) + len(missing_keywords))
        }
