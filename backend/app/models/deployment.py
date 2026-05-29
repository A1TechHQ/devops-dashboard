from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Deployment(Base):
    __tablename__ = "deployments"
    
    id = Column(Integer, primary_key=True, index=True)
    app_id = Column(Integer, ForeignKey("applications.id"), index=True)
    version = Column(String, index=True)
    status = Column(String, default="pending")  # pending, in_progress, completed, failed
    deployed_by = Column(String, nullable=True)
    deployment_start = Column(DateTime(timezone=True))
    deployment_end = Column(DateTime(timezone=True), nullable=True)
    notes = Column(String, nullable=True)
    previous_version = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
