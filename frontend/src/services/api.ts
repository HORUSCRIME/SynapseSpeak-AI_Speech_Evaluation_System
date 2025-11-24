/**
 * API service for speech evaluation
 */

import axios from 'axios';
import type { TranscriptRequest, EvaluationResponse } from '../types/evaluation';

// Get API base URL from environment or use default
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000';

// Create axios instance
const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
    timeout: 30000, // 30 seconds
});

/**
 * Evaluate a transcript
 */
export const evaluateTranscript = async (transcript: string): Promise<EvaluationResponse> => {
    const request: TranscriptRequest = { transcript };

    try {
        console.log(`Sending request to: ${apiClient.defaults.baseURL}/api/evaluate`);
        const response = await apiClient.post<EvaluationResponse>('/api/evaluate', request);
        return response.data;
    } catch (error) {
        console.error('API Error:', error);
        if (axios.isAxiosError(error)) {
            const errorMessage = error.response?.data?.detail ||
                error.message ||
                'Failed to evaluate transcript';

            // Add hint for network errors
            if (error.code === 'ERR_NETWORK') {
                throw new Error(`Network Error: Cannot connect to backend at ${apiClient.defaults.baseURL}. Please ensure the backend server is running.`);
            }

            throw new Error(errorMessage);
        }
        throw error;
    }
};

/**
 * Health check
 */
export const healthCheck = async (): Promise<boolean> => {
    try {
        const response = await apiClient.get('/api/health');
        return response.data.status === 'healthy';
    } catch {
        return false;
    }
};

export default apiClient;
