from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.database import get_db
from app.models import Server, ServerMetrics as ServerMetricsModel
from app.api.dependencies import authenticate_user
from app.models import User

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_metrics(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    # Get latest metrics
    total_servers = db.query(Server).count()
    online_servers = db.query(Server).filter(Server.status == "online").count()
    offline_servers = db.query(Server).filter(Server.status == "offline").count()
    
    return {
        "total_servers": total_servers,
        "online_servers": online_servers,
        "offline_servers": offline_servers,
        "uptime_percent": (online_servers / total_servers * 100) if total_servers > 0 else 0
    }

@router.get("/system")
async def get_system_metrics(
    db: Session = Depends(get_db),
    current_user: User = Depends(authenticate_user)
):
    # Get average system metrics
    latest_metrics = db.query(ServerMetricsModel).order_by(
        ServerMetricsModel.timestamp.desc()
    ).limit(10).all()
    
    if not latest_metrics:
        return {"error": "No metrics available"}
    
    avg_cpu = sum(m.cpu_percent for m in latest_metrics) / len(latest_metrics)
    avg_memory = sum(m.memory_percent for m in latest_metrics) / len(latest_metrics)
    avg_disk = sum(m.disk_percent for m in latest_metrics) / len(latest_metrics)
    
    return {
        "average_cpu": avg_cpu,
        "average_memory": avg_memory,
        "average_disk": avg_disk
    }
