

import React, { useState } from 'react';
import { ChevronDown, ChevronUp, CheckCircle, AlertCircle, Info } from 'lucide-react';
import type { CriterionScore, DetailedAnalysis } from '../types/evaluation';

interface CriteriaBreakdownProps {
    criteriaScores: CriterionScore[];
    detailedAnalysis: DetailedAnalysis;
    summary: string;
}

const CriteriaBreakdown: React.FC<CriteriaBreakdownProps> = ({
    criteriaScores,
    detailedAnalysis,
    summary
}) => {
    const [showDetails, setShowDetails] = useState(false);

    const getScoreColor = (percentage: number) => {
        if (percentage >= 85) return 'bg-success-500';
        if (percentage >= 70) return 'bg-primary-500';
        if (percentage >= 60) return 'bg-warning-500';
        return 'bg-danger-500';
    };

    const getScoreIcon = (percentage: number) => {
        if (percentage >= 70) return <CheckCircle className="w-5 h-5 text-success-600" />;
        return <AlertCircle className="w-5 h-5 text-warning-600" />;
    };

    return (
        <div className="w-full max-w-4xl mx-auto space-y-6 animate-slide-up">
            {/* Summary */}
            <div className="p-6 bg-gradient-to-r from-primary-50 to-primary-100 rounded-xl border border-primary-200">
                <div className="flex items-start gap-3">
                    <Info className="w-6 h-6 text-primary-600 flex-shrink-0 mt-1" />
                    <div>
                        <h3 className="text-lg font-semibold text-gray-800 mb-2">Summary</h3>
                        <p className="text-gray-700 leading-relaxed">{summary}</p>
                    </div>
                </div>
            </div>

            {/* Criteria Scores */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
                <div className="px-6 py-4 bg-gradient-to-r from-gray-50 to-gray-100 border-b border-gray-200">
                    <h3 className="text-xl font-bold text-gray-800">Detailed Breakdown</h3>
                </div>

                <div className="divide-y divide-gray-200">
                    {criteriaScores.map((criterion, index) => (
                        <div key={index} className="p-6 hover:bg-gray-50 transition-colors">
                            <div className="flex items-start justify-between gap-4 mb-3">
                                <div className="flex items-start gap-3 flex-1">
                                    {getScoreIcon(criterion.percentage)}
                                    <div className="flex-1">
                                        <div className="flex items-center justify-between mb-2">
                                            <h4 className="text-lg font-semibold text-gray-800">
                                                {criterion.criterion}
                                            </h4>
                                            <span className="text-sm font-medium text-gray-600">
                                                Weight: {criterion.weight}%
                                            </span>
                                        </div>
                                        <p className="text-sm text-gray-600 mb-3">{criterion.feedback}</p>
                                    </div>
                                </div>
                            </div>

                            {/* Progress Bar */}
                            <div className="space-y-2">
                                <div className="flex items-center justify-between text-sm">
                                    <span className="text-gray-600">
                                        Score: {criterion.score.toFixed(1)} / {criterion.max_score}
                                    </span>
                                    <span className="font-semibold text-gray-800">
                                        {criterion.percentage.toFixed(1)}%
                                    </span>
                                </div>
                                <div className="w-full h-3 bg-gray-200 rounded-full overflow-hidden">
                                    <div
                                        className={`h-full ${getScoreColor(criterion.percentage)} transition-all duration-1000 ease-out rounded-full`}
                                        style={{ width: `${criterion.percentage}%` }}
                                    />
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Detailed Analysis Toggle */}
            <div className="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
                <button
                    onClick={() => setShowDetails(!showDetails)}
                    className="w-full px-6 py-4 flex items-center justify-between hover:bg-gray-50 transition-colors"
                >
                    <h3 className="text-lg font-semibold text-gray-800">Advanced Metrics</h3>
                    {showDetails ? (
                        <ChevronUp className="w-5 h-5 text-gray-600" />
                    ) : (
                        <ChevronDown className="w-5 h-5 text-gray-600" />
                    )}
                </button>

                {showDetails && (
                    <div className="px-6 py-4 border-t border-gray-200 bg-gray-50">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <MetricItem
                                label="Speech Rate"
                                value={`${detailedAnalysis.speech_rate_wpm} WPM`}
                            />
                            <MetricItem
                                label="Vocabulary Richness (TTR)"
                                value={`${detailedAnalysis.vocabulary_richness.toFixed(1)}%`}
                            />
                            <MetricItem
                                label="Grammar Errors"
                                value={detailedAnalysis.grammar_errors.toString()}
                            />
                            <MetricItem
                                label="Grammar Error Rate"
                                value={`${detailedAnalysis.grammar_error_rate.toFixed(2)} per 100 words`}
                            />
                            <MetricItem
                                label="Filler Words"
                                value={detailedAnalysis.filler_words_count.toString()}
                            />
                            <MetricItem
                                label="Filler Word Rate"
                                value={`${detailedAnalysis.filler_word_rate.toFixed(2)}%`}
                            />
                            <MetricItem
                                label="Sentiment Score"
                                value={detailedAnalysis.sentiment_score.toFixed(3)}
                            />
                            <MetricItem
                                label="Salutation"
                                value={detailedAnalysis.salutation_detected || 'None detected'}
                            />
                        </div>

                        <div className="mt-4 pt-4 border-t border-gray-200">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div>
                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">
                                        Keywords Found ({detailedAnalysis.keywords_found.length})
                                    </h4>
                                    <div className="flex flex-wrap gap-2">
                                        {detailedAnalysis.keywords_found.map((keyword, idx) => (
                                            <span
                                                key={idx}
                                                className="px-3 py-1 bg-success-100 text-success-700 text-sm rounded-full"
                                            >
                                                {keyword}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                                <div>
                                    <h4 className="text-sm font-semibold text-gray-700 mb-2">
                                        Keywords Missing ({detailedAnalysis.keywords_missing.length})
                                    </h4>
                                    <div className="flex flex-wrap gap-2">
                                        {detailedAnalysis.keywords_missing.map((keyword, idx) => (
                                            <span
                                                key={idx}
                                                className="px-3 py-1 bg-danger-100 text-danger-700 text-sm rounded-full"
                                            >
                                                {keyword}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

const MetricItem: React.FC<{ label: string; value: string }> = ({ label, value }) => (
    <div className="flex justify-between items-center p-3 bg-white rounded-lg border border-gray-200">
        <span className="text-sm text-gray-600">{label}</span>
        <span className="text-sm font-semibold text-gray-800">{value}</span>
    </div>
);

export default CriteriaBreakdown;
