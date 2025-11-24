/**
 * Transcript Input Component
 */

import React, { useState } from 'react';
import { Send } from 'lucide-react';

interface TranscriptInputProps {
    onSubmit: (transcript: string) => void;
    isLoading: boolean;
}

const TranscriptInput: React.FC<TranscriptInputProps> = ({ onSubmit, isLoading }) => {
    const [transcript, setTranscript] = useState('');
    const [wordCount, setWordCount] = useState(0);

    const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
        const text = e.target.value;
        setTranscript(text);

        // Calculate word count
        const words = text.trim().split(/\s+/).filter(word => word.length > 0);
        setWordCount(words.length);
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (transcript.trim() && !isLoading) {
            onSubmit(transcript);
        }
    };

    const isValid = transcript.trim().length >= 10;

    return (
        <div className="w-full max-w-4xl mx-auto">
            <form onSubmit={handleSubmit} className="space-y-4">
                <div className="relative">
                    <label htmlFor="transcript" className="block text-sm font-semibold text-gray-700 mb-2">
                        Enter Your Self-Introduction
                    </label>
                    <textarea
                        id="transcript"
                        value={transcript}
                        onChange={handleChange}
                        placeholder="Hello everyone! My name is..."
                        disabled={isLoading}
                        className="w-full h-64 px-4 py-3 text-gray-900 bg-white border-2 border-gray-300 rounded-xl 
                     focus:border-primary-500 focus:ring-4 focus:ring-primary-100 
                     disabled:bg-gray-100 disabled:cursor-not-allowed
                     transition-all duration-200 resize-none
                     placeholder:text-gray-400"
                        maxLength={5000}
                    />
                    <div className="absolute bottom-3 right-3 text-sm text-gray-500">
                        {wordCount} words
                    </div>
                </div>

                {!isValid && transcript.length > 0 && (
                    <p className="text-sm text-warning-600">
                        Please enter at least 10 characters
                    </p>
                )}

                <button
                    type="submit"
                    disabled={!isValid || isLoading}
                    className="w-full sm:w-auto px-8 py-3 bg-gradient-to-r from-primary-600 to-primary-700 
                   text-white font-semibold rounded-xl
                   hover:from-primary-700 hover:to-primary-800
                   focus:outline-none focus:ring-4 focus:ring-primary-200
                   disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed
                   transform transition-all duration-200 hover:scale-105 active:scale-95
                   flex items-center justify-center gap-2 shadow-lg hover:shadow-xl"
                >
                    {isLoading ? (
                        <>
                            <div className="w-5 h-5 border-2 border-white border-t-transparent rounded-full animate-spin" />
                            Analyzing...
                        </>
                    ) : (
                        <>
                            <Send className="w-5 h-5" />
                            Evaluate Speech
                        </>
                    )}
                </button>
            </form>
        </div>
    );
};

export default TranscriptInput;
