# chaos - PDD AI Agent MVP

This repository contains an MVP for a 拼多多 AI agent (客服 + 售后初判 + 人工介入).

Quickstart (development):

1. Install dependencies:
   python -m pip install -r backend/requirements.txt
2. Start services (Postgres required). Using uvicorn for local run:
   cd backend
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Files added by Copilot:
- backend/app/main.py (FastAPI app)
- backend/app/models.py (SQLAlchemy models)
- backend/requirements.txt
- backend/Dockerfile
- docker-compose.yml
- .github/workflows/ci.yml

See issues for next steps and assigned owners.
