from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Numeric
from sqlalchemy.sql import func
from app.database import Base

class Server(Base):
    __tablename__ = "servers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    hostname = Column(String, unique=True, index=True)
    ip_address = Column(String, index=True)
    description = Column(String, nullable=True)
    status = Column(String, default="offline")  # online, offline, warning
    last_heartbeat = Column(DateTime(timezone=True), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class ServerMetrics(Base):
    __tablename__ = "server_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    server_id = Column(Integer, ForeignKey("servers.id"), index=True)
    cpu_percent = Column(Float)
    memory_percent = Column(Float)
    disk_percent = Column(Float)
    network_sent = Column(Numeric)
    network_recv = Column(Numeric)
    processes_count = Column(Integer)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
