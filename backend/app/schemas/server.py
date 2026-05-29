from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ServerBase(BaseModel):
    name: str
    hostname: str
    ip_address: str
    description: Optional[str] = None

class ServerCreate(ServerBase):
    pass

class ServerUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class ServerResponse(ServerBase):
    id: int
    status: str
    last_heartbeat: Optional[datetime]
    created_at: datetime
    
    class Config:
        from_attributes = True

class ServerMetrics(BaseModel):
    cpu_percent: float
    memory_percent: float
    disk_percent: float
    network_sent: int
    network_recv: int
    processes_count: int
    timestamp: datetime
