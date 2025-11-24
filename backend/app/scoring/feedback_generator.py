"""
Feedback generation based on scores
"""

from typing import Dict


class FeedbackGenerator:
    """Generate actionable feedback based on scores"""
    
    def generate_salutation_feedback(self, found: bool, salutation_text: str) -> str:
        """Generate feedback for salutation"""
        if found:
            return f"Great! Used '{salutation_text}' as a greeting. This creates a positive first impression."
        else:
            return "Consider starting with a greeting like 'Hello', 'Hi', or 'Good morning' to make your introduction more engaging."
    
    def generate_personal_info_feedback(self, personal_info: Dict[str, bool], count: int) -> str:
        """Generate feedback for personal information"""
        missing = [key for key, found in personal_info.items() if not found]
        
        if count == 5:
            return "Excellent! You included all key personal information (name, age, school, grade, family)."
        elif count >= 3:
            return f"Good coverage of personal information. Consider adding: {', '.join(missing)}."
        else:
            return f"Include more personal details to make your introduction complete. Missing: {', '.join(missing)}."
    
    def generate_hobbies_feedback(self, found: bool) -> str:
        """Generate feedback for hobbies"""
        if found:
            return "Great! You mentioned your hobbies and interests, which makes your introduction more personal."
        else:
            return "Consider mentioning your hobbies or interests to help others get to know you better."
    
    def generate_flow_feedback(self, coherence_score: float, flow_quality: str) -> str:
        """Generate feedback for flow and coherence"""
        if coherence_score >= 85:
            return f"Excellent flow! Your ideas connect smoothly. ({flow_quality})"
        elif coherence_score >= 70:
            return f"Good flow between ideas. ({flow_quality})"
        elif coherence_score >= 50:
            return f"Fair flow. Try using transition words to connect your ideas better. ({flow_quality})"
        else:
            return f"Work on connecting your ideas more smoothly. Use transition words like 'also', 'moreover', 'furthermore'. ({flow_quality})"
    
    def generate_speech_rate_feedback(self, wpm: float) -> str:
        """Generate feedback for speech rate"""
        if 120 <= wpm <= 150:
            return f"Perfect speech rate at {wpm} WPM! This is ideal for clear communication."
        elif 100 <= wpm < 120:
            return f"Speech rate is {wpm} WPM. Try speaking a bit faster to sound more confident."
        elif 150 < wpm <= 180:
            return f"Speech rate is {wpm} WPM. Try slowing down slightly to ensure clarity."
        elif wpm < 100:
            return f"Speech rate is {wpm} WPM. This is quite slow. Try to speak more fluently."
        else:
            return f"Speech rate is {wpm} WPM. This is very fast. Slow down to ensure your audience can follow."
    
    def generate_grammar_feedback(self, error_count: int, error_rate: float, grammar_score: float) -> str:
        """Generate feedback for grammar"""
        if error_count == 0:
            return "Perfect! No grammar errors detected."
        elif error_rate <= 2:
            return f"Very good! Only {error_count} minor grammar error(s) detected."
        elif error_rate <= 5:
            return f"Good effort! Found {error_count} grammar error(s). Review basic grammar rules to improve."
        else:
            return f"Found {error_count} grammar error(s). Focus on improving grammar through practice and review."
    
    def generate_vocabulary_feedback(self, ttr: float, vocab_score: float) -> str:
        """Generate feedback for vocabulary"""
        if vocab_score >= 85:
            return f"Excellent vocabulary richness! (TTR: {ttr}%)"
        elif vocab_score >= 70:
            return f"Good vocabulary variety. (TTR: {ttr}%)"
        elif vocab_score >= 55:
            return f"Fair vocabulary. Try using more varied words to enhance your speech. (TTR: {ttr}%)"
        else:
            return f"Work on expanding your vocabulary. Avoid repeating the same words. (TTR: {ttr}%)"
    
    def generate_clarity_feedback(self, filler_count: int, filler_rate: float, clarity_score: float) -> str:
        """Generate feedback for clarity"""
        if filler_count == 0:
            return "Excellent clarity! No filler words detected."
        elif filler_rate <= 2:
            return f"Very clear! Only {filler_count} filler word(s) detected."
        elif filler_rate <= 5:
            return f"Good clarity. Found {filler_count} filler word(s). Try to reduce 'um', 'uh', 'like', etc."
        else:
            return f"Found {filler_count} filler word(s). Practice speaking more deliberately to reduce fillers."
    
    def generate_engagement_feedback(self, engagement_score: float, sentiment_label: str) -> str:
        """Generate feedback for engagement"""
        if engagement_score >= 80:
            return f"Excellent enthusiasm and positivity! ({sentiment_label})"
        elif engagement_score >= 65:
            return f"Good positive tone. ({sentiment_label})"
        elif engagement_score >= 50:
            return f"Fair engagement. Try to sound more enthusiastic and positive. ({sentiment_label})"
        else:
            return f"Work on sounding more positive and engaged. Smile while speaking! ({sentiment_label})"
    
    def generate_overall_summary(self, overall_score: float, grade: str) -> str:
        """Generate overall summary feedback"""
        if overall_score >= 90:
            return f"Outstanding performance! (Grade: {grade}) Your self-introduction is excellent with strong content, delivery, and engagement."
        elif overall_score >= 80:
            return f"Great job! (Grade: {grade}) Your introduction is well-structured with good delivery. Minor improvements will make it perfect."
        elif overall_score >= 70:
            return f"Good effort! (Grade: {grade}) Your introduction covers the basics well. Focus on the areas marked for improvement."
        elif overall_score >= 60:
            return f"Fair performance. (Grade: {grade}) Work on including more details and improving your delivery."
        else:
            return f"Needs improvement. (Grade: {grade}) Review the feedback carefully and practice your introduction."
