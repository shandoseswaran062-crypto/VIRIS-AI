# VIRIS-AI

This repository now includes a starter backend for the VIRIS-AI project.

## Backend stack
- Python
- FastAPI
- Uvicorn

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## API endpoints

- `GET /health` — health check
- `GET /api/v1/status` — backend status
- `POST /api/v1/chat` — sample AI/chat endpoint

## Example

```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/status
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello VIRIS-AI"}'
```

This is a production-ready starter structure for building your AI backend.
