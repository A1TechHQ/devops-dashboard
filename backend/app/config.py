from pydantic_settings import BaseSettings
from typing import List
from datetime import timedelta

class Settings(BaseSettings):
    # App
    APP_NAME: str = "DevOps Dashboard"
    APP_VERSION: str = "1.0.0"
    
    # Server
    SERVER_HOST: str = "0.0.0.0"
    SERVER_PORT: int = 8000
    
    # Database
    DATABASE_URL: str = "postgresql://user:password@db:5432/devops_db"
    SQLALCHEMY_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = "redis://redis:6379"
    
    # InfluxDB
    INFLUXDB_URL: str = "http://influxdb:8086"
    INFLUXDB_TOKEN: str = "your-token"
    INFLUXDB_ORG: str = "your-org"
    INFLUXDB_BUCKET: str = "metrics"
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    
    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    
    # Email
    SMTP_SERVER: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "your-email@gmail.com"
    SMTP_PASSWORD: str = "your-password"
    SMTP_FROM: str = "noreply@devops-dashboard.com"
    
    # Slack
    SLACK_WEBHOOK_URL: str = ""
    
    # Monitoring
    METRICS_COLLECTION_INTERVAL: int = 60  # seconds
    METRICS_RETENTION_DAYS: int = 30
    
    # Logging
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
