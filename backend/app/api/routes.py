
from fastapi import APIRouter, HTTPException, status
from app.models import TranscriptRequest, EvaluationResponse, HealthResponse
from app.scoring.scorer import SpeechScorer
from app import __version__
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

scorer = SpeechScorer()


@router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="healthy",
        version=__version__,
        models_loaded=True
    )


@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate_transcript(request: TranscriptRequest):

    try:
        logger.info(f"Evaluating transcript with {len(request.transcript)} characters")
        
        result = scorer.evaluate(request.transcript)
        
        logger.info(f"Evaluation complete. Overall score: {result.overall_score}")
        
        return result
    
    except Exception as e:
        logger.error(f"Evaluation error: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error evaluating transcript: {str(e)}"
        )
