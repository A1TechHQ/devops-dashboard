from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.sql import func
from app.database import Base

class Log(Base):
    __tablename__ = "logs"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)  # application, system, deployment
    level = Column(String, index=True)  # ERROR, WARNING, INFO, DEBUG
    message = Column(Text)
    resource_id = Column(Integer, nullable=True)
    resource_type = Column(String, nullable=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
