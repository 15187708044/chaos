
# 最简 Dockerfile：复制代码并用 uvicorn 启动
FROM python:3.11-slim

WORKDIR /app

# 先拷贝 requirements 并安装，加速镜像构建
COPY backend/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# 拷贝后端代码到镜像
COPY backend /app/backend

# 默认启动命令（容器运行 uvicorn）
CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
