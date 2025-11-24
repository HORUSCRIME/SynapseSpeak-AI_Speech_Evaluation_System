from sentence_transformers import SentenceTransformer
from typing import Dict, List
import numpy as np
from app.config import settings


class SemanticAnalyzer:
    
    _instance = None
    _model = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SemanticAnalyzer, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if self._model is None:
            try:
                print(f"Loading sentence transformer model: {settings.sentence_transformer_model}")
                self._model = SentenceTransformer(settings.sentence_transformer_model)
                print("Model loaded successfully")
            except Exception as e:
                print(f"Error loading sentence transformer: {e}")
                self._model = None
    
    def analyze_coherence(self, sentences: List[str]) -> Dict:

        if not self._model or len(sentences) < 2:
            return {
                'coherence_score': 75.0,  
                'avg_similarity': 0.0,
                'flow_quality': 'Good'
            }
        
        try:
            embeddings = self._model.encode(sentences)
            
            similarities = []
            for i in range(len(embeddings) - 1):
                sim = self._cosine_similarity(embeddings[i], embeddings[i + 1])
                similarities.append(sim)
            
            avg_similarity = np.mean(similarities) if similarities else 0.0
            

            coherence_score = self._calculate_coherence_score(avg_similarity)
            
            flow_quality = self._get_flow_quality(coherence_score)
            
            return {
                'coherence_score': round(coherence_score, 2),
                'avg_similarity': round(float(avg_similarity), 3),
                'flow_quality': flow_quality
            }
        
        except Exception as e:
            print(f"Semantic analysis error: {e}")
            return {
                'coherence_score': 75.0,
                'avg_similarity': 0.0,
                'flow_quality': 'Good'
            }
    
    def _cosine_similarity(self, vec1, vec2):
        dot_product = np.dot(vec1, vec2)
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot_product / (norm1 * norm2)
    
    def _calculate_coherence_score(self, avg_similarity: float) -> float:

        if avg_similarity >= 0.6:
            return 85 + ((avg_similarity - 0.6) / 0.4) * 15
        elif avg_similarity >= 0.4:
            return 70 + ((avg_similarity - 0.4) / 0.2) * 15
        elif avg_similarity >= 0.2:
            return 50 + ((avg_similarity - 0.2) / 0.2) * 20
        else:
            return (avg_similarity / 0.2) * 50
    
    def _get_flow_quality(self, coherence_score: float) -> str:
        if coherence_score >= 85:
            return "Excellent"
        elif coherence_score >= 70:
            return "Good"
        elif coherence_score >= 50:
            return "Fair"
        else:
            return "Needs Improvement"
