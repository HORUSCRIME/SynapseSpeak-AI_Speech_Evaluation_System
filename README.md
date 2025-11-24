# AI Speech Evaluation System

A full-stack AI-powered speech evaluation tool that analyzes student self-introduction transcripts and provides rubric-based scoring with detailed feedback.

![AI Speech Evaluation](https://img.shields.io/badge/AI-Speech%20Evaluation-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![React](https://img.shields.io/badge/React-18.2-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-5.2-blue)

## 🌟 Features

- **🎯 Rubric-Based Scoring**: Comprehensive evaluation across 5 major categories
  - Content & Structure (40%)
  - Speech Rate (10%)
  - Language & Grammar (20%)
  - Clarity (15%)
  - Engagement (15%)

- **🤖 AI-Powered Analysis**:
  - Semantic similarity using Sentence Transformers
  - Grammar checking with LanguageTool
  - Sentiment analysis with VADER
  - Vocabulary richness calculation (TTR)
  - Filler word detection

- **📊 Detailed Feedback**:
  - Overall score and letter grade
  - Criterion-level breakdown
  - Actionable improvement suggestions
  - Advanced metrics and analytics

- **💻 Modern UI**:
  - Responsive design with Tailwind CSS
  - Real-time word count
  - Animated score reveals
  - Color-coded performance indicators

## 🏗️ Architecture

```
┌─────────────────┐         ┌──────────────────┐
│  React Frontend │ ◄─────► │  FastAPI Backend │
│  (TypeScript)   │  REST   │     (Python)     │
└─────────────────┘   API   └──────────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
              ┌─────▼─────┐   ┌──────▼──────┐   ┌─────▼─────┐
              │    NLP    │   │   Scoring   │   │    API    │
              │  Pipeline │   │   Engine    │   │  Routes   │
              └───────────┘   └─────────────┘   └───────────┘
```

## 🚀 Quick Start

### Prerequisites

- **Backend**: Python 3.9+, pip
- **Frontend**: Node.js 18+, npm

### Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Download NLTK data**
   ```bash
   python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"
   ```

6. **Create .env file**
   ```bash
   cp .env.example .env
   ```

7. **Start the server**
   ```bash
   uvicorn app.main:app --reload
   ```

   Backend will run at: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Frontend Setup

1. **Navigate to frontend directory**
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create .env file**
   ```bash
   cp .env.example .env
   ```

4. **Start development server**
   ```bash
   npm run dev
   ```

   Frontend will run at: http://localhost:5173

## 📖 Usage

1. **Start both backend and frontend servers**
2. **Open http://localhost:5173 in your browser**
3. **Enter a self-introduction transcript** (e.g., "Hello everyone! My name is Sarah...")
4. **Click "Evaluate Speech"**
5. **Review your detailed results and feedback**

### Example Transcript

```
Hello everyone! My name is Sarah Johnson. I am 15 years old and I study at 
Lincoln High School in grade 10. I live with my parents and my younger brother. 
I love reading books, especially mystery novels, and I enjoy playing basketball 
on weekends. I'm also interested in learning new languages. Thank you for 
listening to my introduction!
```

## 🎯 Scoring Rubric

### Content & Structure (40%)
- **Salutation Level (5%)**: Appropriate greeting
- **Personal Information (10%)**: Name, age, school, grade, family
- **Hobbies/Interests (10%)**: Mentioned activities
- **Flow & Coherence (15%)**: Logical structure and transitions

### Speech Rate (10%)
- Optimal: 120-150 WPM
- Acceptable: 100-120 or 150-180 WPM
- Needs improvement: <100 or >180 WPM

### Language & Grammar (20%)
- **Grammar Accuracy (10%)**: Error detection and scoring
- **Vocabulary Richness (10%)**: Type-Token Ratio (TTR)

### Clarity (15%)
- Filler word detection (um, uh, like, etc.)
- Filler word rate calculation

### Engagement (15%)
- Sentiment analysis
- Positivity and enthusiasm scoring

## 📁 Project Structure

```
NirmannAI/
├── backend/
│   ├── app/
│   │   ├── nlp/              # NLP processing modules
│   │   ├── scoring/          # Scoring engine
│   │   ├── api/              # API routes
│   │   ├── main.py           # FastAPI app
│   │   ├── models.py         # Pydantic models
│   │   └── config.py         # Configuration
│   ├── requirements.txt
│   └── README.md
├── frontend/
│   ├── src/
│   │   ├── components/       # React components
│   │   ├── services/         # API client
│   │   ├── types/            # TypeScript types
│   │   ├── App.tsx           # Main app
│   │   └── main.tsx          # Entry point
│   ├── package.json
│   └── README.md
└── README.md
```

## 🔧 API Endpoints

### POST /api/evaluate
Evaluate a speech transcript.

**Request:**
```json
{
  "transcript": "Hello everyone! My name is..."
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

## 🚢 Deployment

### Backend (Railway/Render)

1. Create `Procfile`:
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

2. Set environment variables in platform dashboard

3. Deploy from GitHub repository

### Frontend (Vercel)

1. Connect GitHub repository to Vercel

2. Set build settings:
   - Build Command: `npm run build`
   - Output Directory: `dist`

3. Add environment variable:
   - `VITE_API_BASE_URL`: Your backend URL

4. Deploy

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern Python web framework
- **Sentence Transformers**: Semantic similarity analysis
- **LanguageTool**: Grammar checking
- **VADER Sentiment**: Sentiment analysis
- **NLTK**: Natural language processing
- **Pydantic**: Data validation

### Frontend
- **React 18**: UI library
- **TypeScript**: Type safety
- **Vite**: Build tool
- **Tailwind CSS**: Styling
- **Axios**: HTTP client
- **Lucide React**: Icons

## 📊 Performance

- **Response Time**: < 5 seconds for typical transcripts
- **Model Loading**: Cached for subsequent requests
- **Concurrent Requests**: Supported via FastAPI async

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 👥 Authors

Built with ❤️ for educators and students

## 🙏 Acknowledgments

- Sentence Transformers by UKPLab
- VADER Sentiment Analysis
- LanguageTool
- FastAPI and React communities

## 📞 Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation
- Review API docs at `/docs`

---

**Made with AI, NLP, and Machine Learning** 🚀
