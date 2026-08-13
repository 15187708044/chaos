from fastapi import APIRouter, Request, Depends, HTTPException
from ..db import SessionLocal
from ..models import Order, Aftersale, ActionLog
from sqlalchemy.orm import Session
import hmac
import hashlib
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/webhook/pdd")
async def pdd_webhook(request: Request, db: Session = Depends(get_db)):
    secret = os.getenv("PDD_WEBHOOK_SECRET")
    body = await request.body()
    if secret:
        signature = request.headers.get("X-PDD-Signature")
        if signature:
            mac = hmac.new(secret.encode(), body, hashlib.sha256).hexdigest()
            if not hmac.compare_digest(mac, signature):
                raise HTTPException(status_code=400, detail="invalid signature")
    payload = await request.json()
    event_type = payload.get("type") or payload.get("event") or "unknown"
    if event_type in ("aftersale", "refund_request"):
        case_id = payload.get("case_id") or payload.get("after_sale_id") or "unknown"
        af = Aftersale(case_id=case_id, order_id=None, type=payload.get("type"), reason_code=payload.get("reason"), status="open", requested_amount=payload.get("amount"), images=payload.get("images"))
        db.add(af)
        db.commit()
        db.refresh(af)
        log = ActionLog(ref_type="aftersale", ref_id=af.id, user="system", action="created_from_webhook", payload=payload)
        db.add(log)
        db.commit()
        return {"status": "ok", "aftersale_id": af.id}
    elif event_type in ("order.created", "order"):
        pdd_order_id = payload.get("order_id") or payload.get("pdd_order_id") or "unknown"
        order = Order(pdd_order_id=pdd_order_id, user_id=payload.get("user_id"), product_id=payload.get("product_id"), sku_id=payload.get("sku_id"), price=payload.get("price"), shipping_fee=payload.get("shipping_fee"), cogs=payload.get("cogs", 0.0))
        db.add(order)
        db.commit()
        db.refresh(order)
        log = ActionLog(ref_type="order", ref_id=order.id, user="system", action="created_from_webhook", payload=payload)
        db.add(log)
        db.commit()
        return {"status": "ok", "order_id": order.id}
    else:
        log = ActionLog(ref_type="event", ref_id=0, user="system", action="received_unknown_event", payload=payload)
        db.add(log)
        db.commit()
        return {"status": "ignored"}
