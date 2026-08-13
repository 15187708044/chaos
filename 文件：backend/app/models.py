from sqlalchemy import Column, Integer, String, DateTime, JSON, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base
from datetime import datetime

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    pdd_order_id = Column(String, unique=True, index=True, nullable=False)
    user_id = Column(String, index=True)
    product_id = Column(String)
    sku_id = Column(String)
    price = Column(Float)
    shipping_fee = Column(Float)
    cogs = Column(Float)
    status = Column(String, default="created")
    created_at = Column(DateTime, default=datetime.utcnow)

class Aftersale(Base):
    __tablename__ = "aftersales"
    id = Column(Integer, primary_key=True, index=True)
    case_id = Column(String, unique=True, index=True, nullable=False)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    type = Column(String)
    reason_code = Column(String)
    status = Column(String, default="open")
    requested_amount = Column(Float)
    images = Column(JSON)
    assigned_agent = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime)

    order = relationship("Order")

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    aftersale_id = Column(Integer, ForeignKey("aftersales.id"), nullable=True)
    sender = Column(String)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class ActionLog(Base):
    __tablename__ = "action_logs"
    id = Column(Integer, primary_key=True, index=True)
    ref_type = Column(String)
    ref_id = Column(Integer)
    user = Column(String)
    action = Column(String)
    payload = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)
