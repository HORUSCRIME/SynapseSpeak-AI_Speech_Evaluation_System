/**
 * Main App Component
 */

import React, { useState } from 'react';
import { Sparkles, AlertCircle } from 'lucide-react';
import TranscriptInput from './components/TranscriptInput';
import ScoreDisplay from './components/ScoreDisplay';
import CriteriaBreakdown from './components/CriteriaBreakdown';
import { evaluateTranscript } from './services/api';
import type { EvaluationResponse } from './types/evaluation';

function App() {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const [result, setResult] = useState<EvaluationResponse | null>(null);

    const handleSubmit = async (transcript: string) => {
        setIsLoading(true);
        setError(null);
        setResult(null);

        try {
            const response = await evaluateTranscript(transcript);
            setResult(response);

            // Scroll to results
            setTimeout(() => {
                document.getElementById('results')?.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }, 100);
        } catch (err) {
            setError(err instanceof Error ? err.message : 'An error occurred');
        } finally {
            setIsLoading(false);
        }
    };

    const handleReset = () => {
        setResult(null);
        setError(null);
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
            {/* Header */}
            <header className="bg-white shadow-sm border-b border-gray-200">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
                    <div className="flex items-center gap-3">
                        <div className="p-2 bg-gradient-to-br from-primary-500 to-purple-600 rounded-xl">
                            <Sparkles className="w-8 h-8 text-white" />
                        </div>
                        <div>
                            <h1 className="text-3xl font-bold bg-gradient-to-r from-primary-600 to-purple-600 bg-clip-text text-transparent">
                                AI Speech Evaluation System
                            </h1>
                            <p className="text-sm text-gray-600 mt-1">
                                Get instant feedback on your self-introduction with AI-powered analysis
                            </p>
                        </div>
                    </div>
                </div>
            </header>

            {/* Main Content */}
            <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
                <div className="space-y-12">
                    {/* Input Section */}
                    <section>
                        <div className="text-center mb-8">
                            <h2 className="text-2xl font-bold text-gray-800 mb-2">
                                Submit Your Self-Introduction
                            </h2>
                            <p className="text-gray-600">
                                Enter your speech transcript below and receive detailed AI-powered feedback
                            </p>
                        </div>
                        <TranscriptInput onSubmit={handleSubmit} isLoading={isLoading} />
                    </section>

                    {/* Error Message */}
                    {error && (
                        <div className="max-w-4xl mx-auto animate-fade-in">
                            <div className="p-4 bg-danger-50 border-2 border-danger-200 rounded-xl flex items-start gap-3">
                                <AlertCircle className="w-6 h-6 text-danger-600 flex-shrink-0 mt-0.5" />
                                <div>
                                    <h3 className="font-semibold text-danger-800 mb-1">Error</h3>
                                    <p className="text-danger-700">{error}</p>
                                    <button
                                        onClick={() => setError(null)}
                                        className="mt-2 text-sm text-danger-600 hover:text-danger-800 font-medium"
                                    >
                                        Dismiss
                                    </button>
                                </div>
                            </div>
                        </div>
                    )}

                    {/* Results Section */}
                    {result && (
                        <section id="results" className="space-y-8">
                            <div className="text-center">
                                <h2 className="text-2xl font-bold text-gray-800 mb-2">
                                    Your Evaluation Results
                                </h2>
                                <p className="text-gray-600">
                                    Review your scores and detailed feedback below
                                </p>
                            </div>

                            <ScoreDisplay
                                score={result.overall_score}
                                grade={result.grade}
                                wordCount={result.word_count}
                                sentenceCount={result.sentence_count}
                            />

                            <CriteriaBreakdown
                                criteriaScores={result.criteria_scores}
                                detailedAnalysis={result.detailed_analysis}
                                summary={result.summary}
                            />

                            <div className="text-center">
                                <button
                                    onClick={handleReset}
                                    className="px-6 py-3 bg-gray-600 text-white font-semibold rounded-xl
                           hover:bg-gray-700 focus:outline-none focus:ring-4 focus:ring-gray-200
                           transform transition-all duration-200 hover:scale-105 active:scale-95
                           shadow-lg hover:shadow-xl"
                                >
                                    Evaluate Another Speech
                                </button>
                            </div>
                        </section>
                    )}
                </div>
            </main>

            {/* Footer */}
            <footer className="bg-white border-t border-gray-200 mt-20">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                    <div className="text-center text-gray-600">
                        <p className="text-sm">
                            AI Speech Evaluation System • Powered by NLP & Machine Learning
                        </p>
                        <p className="text-xs mt-2 text-gray-500">
                            Built with FastAPI, React, and Sentence Transformers
                        </p>
                    </div>
                </div>
            </footer>
        </div>
    );
}

export default App;
