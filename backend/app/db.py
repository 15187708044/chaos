
# SQLAlchemy 数据库连接与 Session 工厂
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 从环境变量读取 DATABASE_URL，默认指向 docker-compose 中的 postgres 服务
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/chaos")

# 创建 engine（echo=False 生产/测试时可改为 False）
engine = create_engine(DATABASE_URL, echo=False)

# SessionLocal 用于依赖注入（FastAPI）中获取 DB session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# declarative base，用于声明 ORM model
Base = declarative_base()
