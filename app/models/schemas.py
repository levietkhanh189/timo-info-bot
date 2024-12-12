# app/models/schemas.py

from pydantic import BaseModel

class Query(BaseModel):
    question: str

class Answer(BaseModel):
    answer: str
