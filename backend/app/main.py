
# FastAPI 应用入口，包含路由挂载和一个健康检查 endpoint
from fastapi import FastAPI
from .api.webhook import router as webhook_router

# 创建 FastAPI app，并设置应用名称
app = FastAPI(title="chaos - PDD AI Agent MVP")

# 挂载 webhook 子路由，前缀 /api
app.include_router(webhook_router, prefix="/api")


@app.get("/health")
async def health():
    """
    健康检查接口，用于容器/负载均衡/监控探活
    返回 JSON: {"status": "ok"}
    """
    return {"status": "ok"}
