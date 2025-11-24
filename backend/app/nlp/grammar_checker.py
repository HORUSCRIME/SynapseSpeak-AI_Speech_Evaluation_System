import language_tool_python
from typing import Dict, List
from app.config import settings


class GrammarChecker:
    
    def __init__(self):
        try:
            self.tool = language_tool_python.LanguageTool('en-US')
        except Exception as e:
            print(f"Warning: Could not initialize LanguageTool: {e}")
            self.tool = None
    
    def check_grammar(self, text: str) -> Dict:

        if not self.tool:
            return {
                'error_count': 0,
                'errors': [],
                'error_rate': 0.0,
                'score': 100.0
            }
        
        try:
            matches = self.tool.check(text)
            
            significant_errors = [
                m for m in matches 
                if m.ruleIssueType in ['grammar', 'misspelling', 'typographical']
            ]
            
            error_count = len(significant_errors)
            
            errors = []
            for match in significant_errors[:10]:  
                errors.append({
                    'message': match.message,
                    'context': match.context,
                    'suggestions': match.replacements[:3] if match.replacements else []
                })
            
            return {
                'error_count': error_count,
                'errors': errors,
                'error_rate': 0.0,  
                'score': 0.0 
            }
        
        except Exception as e:
            print(f"Grammar check error: {e}")
            return {
                'error_count': 0,
                'errors': [],
                'error_rate': 0.0,
                'score': 100.0
            }
    
    def calculate_error_rate(self, error_count: int, word_count: int) -> float:
        if word_count == 0:
            return 0.0
        return (error_count / word_count) * 100
    
    def calculate_grammar_score(self, error_rate: float) -> float:

        max_error_rate = settings.max_grammar_errors_per_100_words
        
        if error_rate == 0:
            return 100.0
        elif error_rate <= 2:
            return 100 - (error_rate * 5)
        elif error_rate <= max_error_rate:
            return 90 - ((error_rate - 2) * 6.67)
        else:
            return max(0, 70 - ((error_rate - max_error_rate) * 10))
    
    def __del__(self):
        if self.tool:
            try:
                self.tool.close()
            except:
                pass
