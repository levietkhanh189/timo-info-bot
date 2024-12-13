from transformers import pipeline
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

logger.info("Initializing QA pipeline...")
qa_pipeline = pipeline("question-answering")
logger.info("QA pipeline initialized successfully.")

def answer_question(question: str, context: str) -> str:
    try:
        logger.info(f"Processing question: {question}")
        result = qa_pipeline(question=question, context=context)
        logger.info(f"Answer extracted: {result['answer']}")
        return result['answer']
    except Exception as e:
        logger.error(f"Error in answer_question: {e}")
        raise Exception(f"Error in answer_question: {e}")
