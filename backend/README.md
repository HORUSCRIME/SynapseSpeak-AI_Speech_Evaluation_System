# AI Speech Evaluation System - Backend

FastAPI backend for AI-powered speech evaluation with NLP-based scoring.

## Features

- 🎯 Rubric-based scoring (Content, Speech Rate, Grammar, Clarity, Engagement)
- 🤖 NLP analysis using sentence transformers, VADER sentiment, and grammar checking
- 📊 Detailed feedback generation
- 🚀 Fast API with auto-generated documentation
- 🔄 CORS enabled for frontend integration

## Setup

### Prerequisites

- Python 3.9+
- pip

### Installation

1. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

2. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK data**
   ```python
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
   ```

5. **Create .env file**
   ```bash
   cp .env.example .env
   ```

## Running the Server

```bash
uvicorn app.main:app --reload
```

Server will start at: http://localhost:8000

- API Documentation: http://localhost:8000/docs
- Alternative Docs: http://localhost:8000/redoc

## API Endpoints

### POST /api/evaluate

Evaluate a speech transcript.

**Request:**
```json
{
  "transcript": "Hello everyone! My name is John..."
}
```

**Response:**
```json
{
  "overall_score": 85.5,
  "grade": "A",
  "word_count": 150,
  "sentence_count": 8,
  "criteria_scores": [...],
  "detailed_analysis": {...},
  "summary": "Great job! Your introduction is well-structured..."
}
```

### GET /api/health

Health check endpoint.

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app
│   ├── models.py            # Pydantic models
│   ├── config.py            # Configuration
│   ├── nlp/                 # NLP processing
│   │   ├── preprocessor.py
│   │   ├── keyword_detector.py
│   │   ├── grammar_checker.py
│   │   ├── sentiment_analyzer.py
│   │   ├── vocabulary_analyzer.py
│   │   └── semantic_analyzer.py
│   ├── scoring/             # Scoring engine
│   │   ├── rubric.py
│   │   ├── scorer.py
│   │   └── feedback_generator.py
│   └── api/                 # API routes
│       └── routes.py
├── requirements.txt
├── .env.example
└── README.md
```

## Scoring Rubric

- **Content & Structure (40%)**
  - Salutation (5%)
  - Personal Information (10%)
  - Hobbies/Interests (10%)
  - Flow & Coherence (15%)

- **Speech Rate (10%)**
  - Optimal: 120-150 WPM

- **Language & Grammar (20%)**
  - Grammar Accuracy (10%)
  - Vocabulary Richness (10%)

- **Clarity (15%)**
  - Filler word analysis

- **Engagement (15%)**
  - Sentiment positivity

## Development

### Testing the API

Use the interactive docs at `/docs` or test with curl:

```bash
curl -X POST http://localhost:8000/api/evaluate \
  -H "Content-Type: application/json" \
  -d '{"transcript": "Hello! My name is Sarah. I am 15 years old and I study at Lincoln High School in grade 10. I live with my parents and my younger brother. I love reading books and playing basketball. Thank you!"}'
```

## Deployment

### Railway/Render

1. Create `Procfile`:
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

2. Set environment variables in platform dashboard

3. Deploy from GitHub repository

## License

MIT
