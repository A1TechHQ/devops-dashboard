from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Alert
from app.api.dependencies import authenticate_user
from app.models import User

router = APIRouter()

@router.get("/")
async def list_alerts(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    alerts = db.query(Alert).all()
    return alerts

@router.get("/active")
async def get_active_alerts(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    alerts = db.query(Alert).filter(Alert.is_active == True).all()
    return alerts

@router.get("/{alert_id}")
async def get_alert(
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@router.post("/{alert_id}/acknowledge")
async def acknowledge_alert(
    alert_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    
    from datetime import datetime
    alert.acknowledged_at = datetime.utcnow()
    db.commit()
    
    return {"detail": "Alert acknowledged", "alert_id": alert_id}
