# VIRIS-AI

This repository includes a backend starter for the VIRIS-AI project.

## Run the backend from the root directory

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## API endpoints

- `GET /health` — health check
- `GET /api/v1/status` — backend status
- `POST /api/v1/chat` — sample AI/chat endpoint

## Example requests

```bash
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/status
curl -X POST http://localhost:8000/api/v1/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"Hello VIRIS-AI"}'
```

The backend entry file is placed in the root directory as `main.py`.
