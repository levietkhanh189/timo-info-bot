# app/services/langchain_pipeline.py

from app.services.qa_model import answer_question
from app.services.data_processing import extract_text_from_cv, extract_text_from_portfolio
from transformers import AutoTokenizer

# Tải tokenizer từ pipeline để sử dụng trong việc giới hạn ngữ cảnh
tokenizer = AutoTokenizer.from_pretrained("deepset/bert-large-uncased-whole-word-masking-squad2")

# Trích xuất văn bản từ CV và portfolio
CV_TEXT = extract_text_from_cv()
PORTFOLIO_TEXT = extract_text_from_portfolio()

# Kết hợp văn bản từ CV và portfolio để tạo thành một ngữ cảnh duy nhất
CONTEXT = CV_TEXT + "\n" + PORTFOLIO_TEXT

def get_answer(question: str) -> str:
    # Tokenize ngữ cảnh để kiểm tra độ dài
    tokens = tokenizer.tokenize(CONTEXT)
    if len(tokens) > 500:  # Giữ một khoảng dư để thêm câu hỏi
        tokens = tokens[:500]
        truncated_context = tokenizer.convert_tokens_to_string(tokens)
    else:
        truncated_context = CONTEXT
    return answer_question(question, truncated_context)
