"""
Main scoring engine - orchestrates all analysis and scoring
"""

from typing import Dict, List
from app.nlp.preprocessor import TextPreprocessor
from app.nlp.keyword_detector import KeywordDetector
from app.nlp.grammar_checker import GrammarChecker
from app.nlp.sentiment_analyzer import SentimentAnalyzer
from app.nlp.vocabulary_analyzer import VocabularyAnalyzer
from app.nlp.semantic_analyzer import SemanticAnalyzer
from app.scoring.rubric import SpeechRubric, SCORING_THRESHOLDS
from app.scoring.feedback_generator import FeedbackGenerator
from app.models import CriterionScore, DetailedAnalysis, EvaluationResponse
from app.config import settings


class SpeechScorer:
    """Main scoring orchestrator"""
    
    def __init__(self):
        # Initialize all analyzers
        self.preprocessor = TextPreprocessor()
        self.keyword_detector = KeywordDetector()
        self.grammar_checker = GrammarChecker()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.vocabulary_analyzer = VocabularyAnalyzer()
        self.semantic_analyzer = SemanticAnalyzer()
        
        # Initialize rubric and feedback generator
        self.rubric = SpeechRubric()
        self.feedback_generator = FeedbackGenerator()
    
    def evaluate(self, transcript: str) -> EvaluationResponse:
        """
        Main evaluation method
        
        Args:
            transcript: Raw transcript text
            
        Returns:
            EvaluationResponse with complete scoring and feedback
        """
        # Step 1: Preprocess text
        preprocessed = self.preprocessor.process(transcript)
        
        # Step 2: Run all NLP analyses
        keyword_analysis = self.keyword_detector.get_keywords_summary(
            preprocessed['cleaned_text'],
            preprocessed['words']
        )
        
        grammar_analysis = self.grammar_checker.check_grammar(preprocessed['cleaned_text'])
        grammar_error_rate = self.grammar_checker.calculate_error_rate(
            grammar_analysis['error_count'],
            preprocessed['word_count']
        )
        grammar_score = self.grammar_checker.calculate_grammar_score(grammar_error_rate)
        
        sentiment_analysis = self.sentiment_analyzer.analyze_sentiment(preprocessed['cleaned_text'])
        
        vocabulary_analysis = self.vocabulary_analyzer.analyze(
            preprocessed['cleaned_text'],
            preprocessed['words']
        )
        
        semantic_analysis = self.semantic_analyzer.analyze_coherence(preprocessed['sentences'])
        
        # Step 3: Score each criterion
        criteria_scores = self._score_all_criteria(
            preprocessed,
            keyword_analysis,
            grammar_analysis,
            grammar_error_rate,
            grammar_score,
            sentiment_analysis,
            vocabulary_analysis,
            semantic_analysis
        )
        
        # Step 4: Calculate overall score
        overall_score = self._calculate_overall_score(criteria_scores)
        
        # Step 5: Create detailed analysis
        detailed_analysis = DetailedAnalysis(
            keywords_found=keyword_analysis['keywords_found'],
            keywords_missing=keyword_analysis['keywords_missing'],
            grammar_errors=grammar_analysis['error_count'],
            grammar_error_rate=round(grammar_error_rate, 2),
            filler_words_count=vocabulary_analysis['filler_count'],
            filler_word_rate=vocabulary_analysis['filler_rate'],
            sentiment_score=sentiment_analysis['compound'],
            vocabulary_richness=vocabulary_analysis['ttr'],
            speech_rate_wpm=preprocessed['wpm'],
            salutation_detected=keyword_analysis.get('salutation_text')
        )
        
        # Step 6: Generate overall summary
        grade = self._calculate_grade(overall_score)
        summary = self.feedback_generator.generate_overall_summary(overall_score, grade)
        
        # Step 7: Create response
        return EvaluationResponse(
            overall_score=round(overall_score, 2),
            grade=grade,
            word_count=preprocessed['word_count'],
            sentence_count=preprocessed['sentence_count'],
            criteria_scores=criteria_scores,
            detailed_analysis=detailed_analysis,
            summary=summary
        )
    
    def _score_all_criteria(
        self,
        preprocessed: Dict,
        keyword_analysis: Dict,
        grammar_analysis: Dict,
        grammar_error_rate: float,
        grammar_score: float,
        sentiment_analysis: Dict,
        vocabulary_analysis: Dict,
        semantic_analysis: Dict
    ) -> List[CriterionScore]:
        """Score all criteria and generate feedback"""
        
        scores = []
        
        # 1. Salutation (5%)
        salutation_score = 5.0 if keyword_analysis['salutation_found'] else 0.0
        scores.append(CriterionScore(
            criterion="Salutation Level",
            score=salutation_score,
            max_score=5.0,
            weight=5.0,
            feedback=self.feedback_generator.generate_salutation_feedback(
                keyword_analysis['salutation_found'],
                keyword_analysis.get('salutation_text', '')
            )
        ))
        
        # 2. Personal Information (10%)
        personal_info = keyword_analysis['personal_info']
        personal_info_count = sum(1 for found in personal_info.values() if found)
        personal_info_score = self._score_personal_info(personal_info_count)
        scores.append(CriterionScore(
            criterion="Personal Information",
            score=personal_info_score,
            max_score=5.0,
            weight=10.0,
            feedback=self.feedback_generator.generate_personal_info_feedback(
                personal_info,
                personal_info_count
            )
        ))
        
        # 3. Hobbies/Interests (10%)
        hobbies_score = 5.0 if keyword_analysis['hobbies_found'] else 0.0
        scores.append(CriterionScore(
            criterion="Hobbies/Interests",
            score=hobbies_score,
            max_score=5.0,
            weight=10.0,
            feedback=self.feedback_generator.generate_hobbies_feedback(
                keyword_analysis['hobbies_found']
            )
        ))
        
        # 4. Flow & Coherence (15%)
        coherence_score = self._score_coherence(semantic_analysis['coherence_score'])
        scores.append(CriterionScore(
            criterion="Flow & Coherence",
            score=coherence_score,
            max_score=5.0,
            weight=15.0,
            feedback=self.feedback_generator.generate_flow_feedback(
                semantic_analysis['coherence_score'],
                semantic_analysis['flow_quality']
            )
        ))
        
        # 5. Speech Rate (10%)
        speech_rate_score = self._score_speech_rate(preprocessed['wpm'])
        scores.append(CriterionScore(
            criterion="Speech Rate",
            score=speech_rate_score,
            max_score=5.0,
            weight=10.0,
            feedback=self.feedback_generator.generate_speech_rate_feedback(
                preprocessed['wpm']
            )
        ))
        
        # 6. Grammar Accuracy (10%)
        grammar_criterion_score = self._score_grammar(grammar_score)
        scores.append(CriterionScore(
            criterion="Grammar Accuracy",
            score=grammar_criterion_score,
            max_score=5.0,
            weight=10.0,
            feedback=self.feedback_generator.generate_grammar_feedback(
                grammar_analysis['error_count'],
                grammar_error_rate,
                grammar_score
            )
        ))
        
        # 7. Vocabulary Richness (10%)
        vocabulary_criterion_score = self._score_vocabulary(vocabulary_analysis['vocabulary_score'])
        scores.append(CriterionScore(
            criterion="Vocabulary Richness",
            score=vocabulary_criterion_score,
            max_score=5.0,
            weight=10.0,
            feedback=self.feedback_generator.generate_vocabulary_feedback(
                vocabulary_analysis['ttr'],
                vocabulary_analysis['vocabulary_score']
            )
        ))
        
        # 8. Clarity (15%)
        clarity_criterion_score = self._score_clarity(vocabulary_analysis['clarity_score'])
        scores.append(CriterionScore(
            criterion="Clarity (Filler Words)",
            score=clarity_criterion_score,
            max_score=5.0,
            weight=15.0,
            feedback=self.feedback_generator.generate_clarity_feedback(
                vocabulary_analysis['filler_count'],
                vocabulary_analysis['filler_rate'],
                vocabulary_analysis['clarity_score']
            )
        ))
        
        # 9. Engagement (15%)
        engagement_criterion_score = self._score_engagement(sentiment_analysis['engagement_score'])
        scores.append(CriterionScore(
            criterion="Engagement & Positivity",
            score=engagement_criterion_score,
            max_score=5.0,
            weight=15.0,
            feedback=self.feedback_generator.generate_engagement_feedback(
                sentiment_analysis['engagement_score'],
                sentiment_analysis['sentiment_label']
            )
        ))
        
        return scores
    
    def _score_personal_info(self, count: int) -> float:
        """Score personal information based on count"""
        if count >= 5:
            return 5.0
        elif count >= 3:
            return 3.5
        elif count >= 2:
            return 2.5
        elif count >= 1:
            return 1.5
        else:
            return 0.0
    
    def _score_coherence(self, coherence_score: float) -> float:
        """Convert coherence score (0-100) to criterion score (0-5)"""
        if coherence_score >= 85:
            return 5.0
        elif coherence_score >= 70:
            return 4.0
        elif coherence_score >= 50:
            return 3.0
        else:
            return 2.0
    
    def _score_speech_rate(self, wpm: float) -> float:
        """Score speech rate based on WPM"""
        if settings.optimal_wpm_min <= wpm <= settings.optimal_wpm_max:
            return 5.0
        elif 100 <= wpm < settings.optimal_wpm_min or settings.optimal_wpm_max < wpm <= 180:
            return 3.5
        else:
            return 2.0
    
    def _score_grammar(self, grammar_score: float) -> float:
        """Convert grammar score (0-100) to criterion score (0-5)"""
        if grammar_score >= 90:
            return 5.0
        elif grammar_score >= 75:
            return 4.0
        elif grammar_score >= 60:
            return 3.0
        else:
            return 2.0
    
    def _score_vocabulary(self, vocab_score: float) -> float:
        """Convert vocabulary score (0-100) to criterion score (0-5)"""
        if vocab_score >= 85:
            return 5.0
        elif vocab_score >= 70:
            return 4.0
        elif vocab_score >= 55:
            return 3.0
        else:
            return 2.0
    
    def _score_clarity(self, clarity_score: float) -> float:
        """Convert clarity score (0-100) to criterion score (0-5)"""
        if clarity_score >= 90:
            return 5.0
        elif clarity_score >= 75:
            return 4.0
        elif clarity_score >= 60:
            return 3.0
        else:
            return 2.0
    
    def _score_engagement(self, engagement_score: float) -> float:
        """Convert engagement score (0-100) to criterion score (0-5)"""
        if engagement_score >= 80:
            return 5.0
        elif engagement_score >= 65:
            return 4.0
        elif engagement_score >= 50:
            return 3.0
        else:
            return 2.0
    
    def _calculate_overall_score(self, criteria_scores: List[CriterionScore]) -> float:
        """Calculate weighted overall score (0-100)"""
        total_score = 0.0
        
        for criterion in criteria_scores:
            # Convert criterion score (0-5) to percentage (0-100)
            percentage = (criterion.score / criterion.max_score) * 100
            # Apply weight
            weighted_score = percentage * (criterion.weight / 100)
            total_score += weighted_score
        
        return total_score
    
    def _calculate_grade(self, overall_score: float) -> str:
        """Calculate letter grade"""
        if overall_score >= 90:
            return 'A+'
        elif overall_score >= 85:
            return 'A'
        elif overall_score >= 80:
            return 'B+'
        elif overall_score >= 75:
            return 'B'
        elif overall_score >= 70:
            return 'C+'
        elif overall_score >= 65:
            return 'C'
        elif overall_score >= 60:
            return 'D'
        else:
            return 'F'
