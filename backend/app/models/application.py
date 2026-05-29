from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(String, default="offline")  # running, stopped, error
    health_status = Column(String, default="unknown")  # healthy, warning, critical
    server_id = Column(Integer, ForeignKey("servers.id"), nullable=True)
    url = Column(String, nullable=True)
    port = Column(Integer, nullable=True)
    health_check_url = Column(String, nullable=True)
    last_health_check = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ApplicationMetrics(Base):
    __tablename__ = "application_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    app_id = Column(Integer, ForeignKey("applications.id"), index=True)
    response_time_ms = Column(Float)
    error_rate = Column(Float)
    request_count = Column(Integer)
    success_count = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
