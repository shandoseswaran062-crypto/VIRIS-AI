from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="VIRIS-AI Backend", version="1.0.0")


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health_check():
    return {"status": "ok", "service": "VIRIS-AI backend"}


@app.get("/api/v1/status")
def get_status():
    return {
        "app": "VIRIS-AI",
        "status": "running",
        "version": "1.0.0",
    }


@app.post("/api/v1/chat")
def chat_with_ai(payload: ChatRequest):
    return {
        "reply": f"VIRIS-AI received: {payload.message}",
        "message": payload.message,
        "status": "success",
    }
