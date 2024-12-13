from fastapi import APIRouter, HTTPException
from app.models.schemas import Query, Answer
from app.services.langchain_pipeline import get_answer

router = APIRouter()

@router.post("/ask", response_model=Answer)
async def ask_question(query: Query):
    if not query.question.strip():
        raise HTTPException(status_code=400, detail="Questions cannot be left blank.")
    try:
        answer = get_answer(query.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
