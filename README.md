# chaos - PDD AI Agent MVP

本仓库为拼多多售后/客服 AI Agent 的 MVP 示例（包含 FastAPI 后端骨架、数据库模型、Webhook 接收 stub 以及 Docker 配置）。

快速启动（开发环境）：
1. 使用 docker-compose 启动 Postgres 与 web：
   docker-compose up --build -d
2. 访问健康检查：
   http://localhost:8000/health
3. 本地不使用容器时（示例）：
   cd backend
   python -m pip install -r requirements.txt
   uvicorn backend.app.main:app --reload --host 0.0.0.0 --port 8000

说明：
- database 配置通过环境变量 DATABASE_URL 控制（见 docker-compose.yml）
- webhook endpoint: POST /api/webhook/pdd （示例）
