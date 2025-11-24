/**
 * TypeScript interfaces for evaluation data
 */

export interface CriterionScore {
    criterion: string;
    score: number;
    max_score: number;
    feedback: string;
    weight: number;
    percentage: number;
}

export interface DetailedAnalysis {
    keywords_found: string[];
    keywords_missing: string[];
    grammar_errors: number;
    grammar_error_rate: number;
    filler_words_count: number;
    filler_word_rate: number;
    sentiment_score: number;
    vocabulary_richness: number;
    speech_rate_wpm: number;
    salutation_detected: string | null;
}

export interface EvaluationResponse {
    overall_score: number;
    grade: string;
    word_count: number;
    sentence_count: number;
    criteria_scores: CriterionScore[];
    detailed_analysis: DetailedAnalysis;
    summary: string;
}

export interface TranscriptRequest {
    transcript: string;
}
