from fastapi import FastAPI
from .api.webhook import router as webhook_router

app = FastAPI(title="chaos - PDD AI Agent MVP")

app.include_router(webhook_router, prefix="/api")

@app.get("/health")
async def health():
    return {"status": "ok"}
