from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import Log
from app.api.dependencies import authenticate_user
from app.models import User

router = APIRouter()

@router.get("/")
async def search_logs(
    level: str = Query(None),
    source: str = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    query = db.query(Log)
    
    if level:
        query = query.filter(Log.level == level)
    if source:
        query = query.filter(Log.source == source)
    
    logs = query.order_by(Log.timestamp.desc()).offset(skip).limit(limit).all()
    return logs

@router.get("/stats")
async def get_log_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    from sqlalchemy import func
    
    stats = db.query(
        Log.level,
        func.count(Log.id).label("count")
    ).group_by(Log.level).all()
    
    return {item[0]: item[1] for item in stats}
