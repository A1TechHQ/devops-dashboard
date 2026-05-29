from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Deployment
from app.api.dependencies import authenticate_user
from app.models import User

router = APIRouter()

@router.get("/")
async def list_deployments(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    deployments = db.query(Deployment).order_by(Deployment.created_at.desc()).all()
    return deployments

@router.get("/{deployment_id}")
async def get_deployment(
    deployment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    deployment = db.query(Deployment).filter(Deployment.id == deployment_id).first()
    if not deployment:
        raise HTTPException(status_code=404, detail="Deployment not found")
    return deployment

@router.post("/{deployment_id}/rollback")
async def rollback_deployment(
    deployment_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    deployment = db.query(Deployment).filter(Deployment.id == deployment_id).first()
    if not deployment:
        raise HTTPException(status_code=404, detail="Deployment not found")
    
    return {"detail": "Rollback initiated", "previous_version": deployment.previous_version}
