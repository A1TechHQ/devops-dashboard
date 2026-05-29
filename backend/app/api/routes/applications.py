from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Application
from app.api.dependencies import authenticate_user
from app.models import User

router = APIRouter()

@router.get("/")
async def list_applications(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    apps = db.query(Application).all()
    return apps

@router.get("/{app_id}")
async def get_application(
    app_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    app = db.query(Application).filter(Application.id == app_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    return app

@router.get("/{app_id}/health")
async def get_app_health(
    app_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    app = db.query(Application).filter(Application.id == app_id).first()
    if not app:
        raise HTTPException(status_code=404, detail="Application not found")
    
    return {
        "app_id": app.id,
        "name": app.name,
        "status": app.status,
        "health_status": app.health_status,
        "last_health_check": app.last_health_check
    }
