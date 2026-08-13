
# 最小化 ORM 模型：Order / Aftersale / Message / ActionLog
from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base
from datetime import datetime

# 订单模型（用于关联售后)
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    pdd_order_id = Column(String, unique=True, index=True, nullable=False)  # 平台订单号
    user_id = Column(String, index=True)
    product_id = Column(String)
    sku_id = Column(String)
    price = Column(Float)
    shipping_fee = Column(Float)
    cogs = Column(Float)
    status = Column(String, default="created")
    created_at = Column(DateTime, default=datetime.utcnow)


# 售后案件模型
class Aftersale(Base):
    __tablename__ = "aftersales"
    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(String, unique=True, index=True, nullable=False)  # 售后案件编号
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    type = Column(String)  # 退款/退货/换货等
    reason_code = Column(String)
    status = Column(String, default="open")
    requested_amount = Column(Float)
    images = Column(JSON)  # 存储图片 URL 列表
    assigned_agent = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)

    # ORM 关系，方便查询 order
    order = relationship("Order")


# 会话/消息记录（用户与客服交互）
class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    aftersale_id = Column(Integer, ForeignKey("aftersales.id"), nullable=True)
    sender = Column(String)  # user/system/agent
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)


# 操作日志/审计表，用于记录所有自动或人工决策
class ActionLog(Base):
    __tablename__ = "action_logs"
    id = Column(Integer, primary_key=True, index=True)
    ref_type = Column(String)  # e.g., 'order' / 'aftersale'
    ref_id = Column(Integer)
    user = Column(String)  # 执行者（system / agent id）
    action = Column(String)  # 操作类型
    payload = Column(JSON)  # 变更详情或凭证
    timestamp = Column(DateTime, default=datetime.utcnow)
