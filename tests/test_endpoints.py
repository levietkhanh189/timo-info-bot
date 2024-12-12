# tests/test_endpoints.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_question_success():
    response = client.post("/ask", json={"question": "What kind of work experience do you have?"})
    if response.status_code != 200:
        print("Response Status Code:", response.status_code)
        print("Response Body:", response.json())
    assert response.status_code == 200
    assert "answer" in response.json()
    assert isinstance(response.json()["answer"], str)
    assert len(response.json()["answer"].split()) > 1  # Đảm bảo câu trả lời có nhiều hơn một từ

def test_ask_question_empty():
    response = client.post("/ask", json={"question": ""})
    assert response.status_code == 400
    assert response.json()["detail"] == "Questions cannot be left blank."

def test_ask_question_missing():
    response = client.post("/ask", json={})
    assert response.status_code == 422  # Unprocessable Entity
