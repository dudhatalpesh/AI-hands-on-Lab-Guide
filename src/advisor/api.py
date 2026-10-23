"""Loopback teaching API: fixed identity, no production authentication."""
from fastapi import FastAPI
from pydantic import BaseModel, Field
from src.advisor.core import Model, rag

app = FastAPI(title="Local AI advisor demo")


class Question(BaseModel):
    question: str = Field(min_length=1, max_length=6000)


@app.get("/health")
def health():
    return {"status": "ok", "mode": "local-demo"}


@app.post("/ask")
def ask(body: Question):
    # No tenant supplied by the caller. Replace with verified identity middleware in production.
    return rag(body.question, "northstar", Model())
