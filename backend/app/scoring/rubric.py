"""
Rubric definitions and scoring criteria
"""

from typing import Dict, List
from dataclasses import dataclass


@dataclass
class Criterion:
    """Individual scoring criterion"""
    name: str
    weight: float  # Percentage weight (0-100)
    max_score: float = 5.0  # Maximum score for this criterion


class SpeechRubric:
    """Speech evaluation rubric with all criteria"""
    
    def __init__(self):
        # Define all criteria with their weights
        self.criteria = {
            # Content & Structure (40%)
            'salutation': Criterion('Salutation Level', 5.0),
            'personal_info': Criterion('Personal Information', 10.0),
            'hobbies': Criterion('Hobbies/Interests', 10.0),
            'flow_coherence': Criterion('Flow & Coherence', 15.0),
            
            # Speech Rate (10%)
            'speech_rate': Criterion('Speech Rate', 10.0),
            
            # Language & Grammar (20%)
            'grammar': Criterion('Grammar Accuracy', 10.0),
            'vocabulary': Criterion('Vocabulary Richness', 10.0),
            
            # Clarity (15%)
            'clarity': Criterion('Clarity (Filler Words)', 15.0),
            
            # Engagement (15%)
            'engagement': Criterion('Engagement & Positivity', 15.0),
        }
        
        # Verify total weight = 100%
        total_weight = sum(c.weight for c in self.criteria.values())
        assert abs(total_weight - 100.0) < 0.01, f"Weights must sum to 100%, got {total_weight}%"
    
    def get_criterion(self, name: str) -> Criterion:
        """Get criterion by name"""
        return self.criteria.get(name)
    
    def get_all_criteria(self) -> Dict[str, Criterion]:
        """Get all criteria"""
        return self.criteria
    
    def get_category_weight(self, category: str) -> float:
        """Get total weight for a category"""
        category_weights = {
            'content_structure': 40.0,
            'speech_rate': 10.0,
            'language_grammar': 20.0,
            'clarity': 15.0,
            'engagement': 15.0
        }
        return category_weights.get(category, 0.0)


# Scoring thresholds and ranges
SCORING_THRESHOLDS = {
    'salutation': {
        'excellent': 5.0,  # Has appropriate salutation
        'good': 3.0,       # Has basic greeting
        'poor': 0.0        # No salutation
    },
    'personal_info': {
        'excellent': 5.0,  # All 5 elements (name, age, school, grade, family)
        'good': 3.0,       # 3-4 elements
        'fair': 2.0,       # 2 elements
        'poor': 1.0        # 1 element
    },
    'hobbies': {
        'excellent': 5.0,  # Mentions hobbies with details
        'good': 3.0,       # Mentions hobbies
        'poor': 0.0        # No hobbies mentioned
    },
    'flow_coherence': {
        'excellent': 5.0,  # Coherence score >= 85
        'good': 4.0,       # Coherence score >= 70
        'fair': 3.0,       # Coherence score >= 50
        'poor': 2.0        # Coherence score < 50
    },
    'speech_rate': {
        'optimal': 5.0,    # 120-150 WPM
        'acceptable': 3.5, # 100-120 or 150-180 WPM
        'poor': 2.0        # < 100 or > 180 WPM
    },
    'grammar': {
        'excellent': 5.0,  # Grammar score >= 90
        'good': 4.0,       # Grammar score >= 75
        'fair': 3.0,       # Grammar score >= 60
        'poor': 2.0        # Grammar score < 60
    },
    'vocabulary': {
        'excellent': 5.0,  # Vocabulary score >= 85
        'good': 4.0,       # Vocabulary score >= 70
        'fair': 3.0,       # Vocabulary score >= 55
        'poor': 2.0        # Vocabulary score < 55
    },
    'clarity': {
        'excellent': 5.0,  # Clarity score >= 90
        'good': 4.0,       # Clarity score >= 75
        'fair': 3.0,       # Clarity score >= 60
        'poor': 2.0        # Clarity score < 60
    },
    'engagement': {
        'excellent': 5.0,  # Engagement score >= 80
        'good': 4.0,       # Engagement score >= 65
        'fair': 3.0,       # Engagement score >= 50
        'poor': 2.0        # Engagement score < 50
    }
}
