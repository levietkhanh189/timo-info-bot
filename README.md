# Chatbot CV Portfolio

## Description
A chatbot that answers recruiters' questions based on information from a CV and portfolio.

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/levietkhanh189/timo-info-bot
    cd chatbot_cv_portfolio
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    - Create a `.env` file in the project's root directory and add the following variables:
        ```
        CV_PATH=path/to/your/cv.pdf
        PORTFOLIO_PATH=path/to/your/portfolio.pdf
        ```

5. **Run the application:**
    ```bash
    uvicorn app.main:app --reload
    ```

## Usage

- **Endpoint `/ask`:**
    - **Method:** POST
    - **Body:** JSON `{ "question": "Your question?" }`
    - **Response:** JSON `{ "answer": "Chatbot's answer." }`

**Example:**

```bash
curl -X POST "http://127.0.0.1:8000/ask" -H "Content-Type: application/json" -d '{"question": "What skills do you have?"}'
```