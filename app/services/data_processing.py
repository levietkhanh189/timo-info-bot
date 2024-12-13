from PyPDF2 import PdfReader
from app.core.config import settings

def extract_text_from_pdf(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        print(f"Extracted text from {pdf_path}: {len(text)} characters")
        return text
    except Exception as e:
        raise Exception(f"Unable to extract text from {pdf_path}: {str(e)}")


def extract_text_from_cv() -> str:
    return extract_text_from_pdf(settings.CV_PATH)

def extract_text_from_portfolio() -> str:
    return extract_text_from_pdf(settings.PORTFOLIO_PATH)
