from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class TopicInput(BaseModel):
    input: dict

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"  # or 'mistral', 'llama3', etc.

def query_ollama(prompt: str) -> str:
    response = requests.post(OLLAMA_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

@app.post("/essay/invoke")
async def generate_essay(data: TopicInput):
    topic = data.input.get("topic", "")
    prompt = f"Write an informative essay of about 100 words on the topic: {topic}"
    content = query_ollama(prompt)
    return {"output": {"content": content}}

@app.post("/poem/invoke")
async def generate_poem(data: TopicInput):
    topic = data.input.get("topic", "")
    prompt = f"Write a creative 8-line poem about: {topic}"
    content = query_ollama(prompt)
    return {"output": content}
