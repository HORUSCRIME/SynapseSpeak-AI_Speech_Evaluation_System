/**
 * Score Display Component
 */

import React from 'react';
import { Award, TrendingUp, TrendingDown, Minus } from 'lucide-react';

interface ScoreDisplayProps {
    score: number;
    grade: string;
    wordCount: number;
    sentenceCount: number;
}

const ScoreDisplay: React.FC<ScoreDisplayProps> = ({ score, grade, wordCount, sentenceCount }) => {
    // Determine color based on score
    const getScoreColor = (score: number) => {
        if (score >= 85) return 'text-success-600';
        if (score >= 70) return 'text-primary-600';
        if (score >= 60) return 'text-warning-600';
        return 'text-danger-600';
    };

    const getScoreBgColor = (score: number) => {
        if (score >= 85) return 'bg-success-50 border-success-200';
        if (score >= 70) return 'bg-primary-50 border-primary-200';
        if (score >= 60) return 'bg-warning-50 border-warning-200';
        return 'bg-danger-50 border-danger-200';
    };

    const getScoreIcon = (score: number) => {
        if (score >= 85) return <TrendingUp className="w-8 h-8" />;
        if (score >= 60) return <Minus className="w-8 h-8" />;
        return <TrendingDown className="w-8 h-8" />;
    };

    const scoreColor = getScoreColor(score);
    const scoreBgColor = getScoreBgColor(score);

    return (
        <div className="w-full max-w-4xl mx-auto animate-fade-in">
            <div className={`relative p-8 rounded-2xl border-2 ${scoreBgColor} shadow-xl`}>
                {/* Decorative background pattern */}
                <div className="absolute top-0 right-0 w-32 h-32 opacity-10">
                    <Award className="w-full h-full" />
                </div>

                <div className="relative z-10">
                    <div className="flex flex-col md:flex-row items-center justify-between gap-6">
                        {/* Overall Score */}
                        <div className="flex items-center gap-6">
                            <div className={`${scoreColor}`}>
                                {getScoreIcon(score)}
                            </div>
                            <div>
                                <p className="text-sm font-medium text-gray-600 uppercase tracking-wide">
                                    Overall Score
                                </p>
                                <div className="flex items-baseline gap-2">
                                    <span className={`text-6xl font-bold ${scoreColor}`}>
                                        {score.toFixed(1)}
                                    </span>
                                    <span className="text-2xl text-gray-500">/100</span>
                                </div>
                                <p className={`text-xl font-semibold mt-1 ${scoreColor}`}>
                                    Grade: {grade}
                                </p>
                            </div>
                        </div>

                        {/* Stats */}
                        <div className="flex gap-8">
                            <div className="text-center">
                                <p className="text-3xl font-bold text-gray-800">{wordCount}</p>
                                <p className="text-sm text-gray-600 mt-1">Words</p>
                            </div>
                            <div className="w-px bg-gray-300" />
                            <div className="text-center">
                                <p className="text-3xl font-bold text-gray-800">{sentenceCount}</p>
                                <p className="text-sm text-gray-600 mt-1">Sentences</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ScoreDisplay;
