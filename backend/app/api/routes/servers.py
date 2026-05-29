from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.server import ServerCreate, ServerUpdate, ServerResponse, ServerMetrics
from app.models import Server, ServerMetrics as ServerMetricsModel
from app.api.dependencies import authenticate_user
from app.models import User
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/", response_model=List[ServerResponse])
async def list_servers(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    servers = db.query(Server).offset(skip).limit(limit).all()
    return servers

@router.get("/{server_id}", response_model=ServerResponse)
async def get_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    server = db.query(Server).filter(Server.id == server_id).first()
    if not server:
        raise HTTPException(status_code=404, detail="Server not found")
    return server

@router.post("/", response_model=ServerResponse)
async def create_server(
    server: ServerCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_server = Server(**server.dict())
    db.add(db_server)
    db.commit()
    db.refresh(db_server)
    return db_server

@router.put("/{server_id}", response_model=ServerResponse)
async def update_server(
    server_id: int,
    server_update: ServerUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    if current_user.role not in ["admin", "manager"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_server = db.query(Server).filter(Server.id == server_id).first()
    if not db_server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    for field, value in server_update.dict(exclude_unset=True).items():
        setattr(db_server, field, value)
    
    db.commit()
    db.refresh(db_server)
    return db_server

@router.delete("/{server_id}")
async def delete_server(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_server = db.query(Server).filter(Server.id == server_id).first()
    if not db_server:
        raise HTTPException(status_code=404, detail="Server not found")
    
    db.delete(db_server)
    db.commit()
    return {"detail": "Server deleted"}

@router.get("/{server_id}/metrics", response_model=ServerMetrics)
async def get_server_metrics(
    server_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    metrics = db.query(ServerMetricsModel)\
        .filter(ServerMetricsModel.server_id == server_id)\
        .order_by(ServerMetricsModel.timestamp.desc())\
        .first()
    
    if not metrics:
        raise HTTPException(status_code=404, detail="Metrics not found")
    
    return metrics

@router.get("/{server_id}/history")
async def get_server_history(
    server_id: int,
    hours: int = Query(24, ge=1, le=720),
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    since = datetime.utcnow() - timedelta(hours=hours)
    metrics = db.query(ServerMetricsModel)\
        .filter(ServerMetricsModel.server_id == server_id)\
        .filter(ServerMetricsModel.timestamp >= since)\
        .order_by(ServerMetricsModel.timestamp)\
        .all()
    
    return metrics
