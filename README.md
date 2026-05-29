# DevOps Dashboard - Enterprise Monitoring & Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://react.dev/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive, production-ready DevOps monitoring and analytics dashboard for real-time infrastructure monitoring, application health tracking, and deployment management.

## 🚀 Features

### Server Monitoring
✅ Real-time CPU, Memory, Disk, and Network monitoring
✅ Process monitoring and management
✅ System health status
✅ Performance metrics
✅ Alert thresholds and notifications

### Application Health
✅ Application status tracking
✅ Response time monitoring
✅ Error rate tracking
✅ Request throughput analysis
✅ Dependency health checks

### Deployment Management
✅ Deployment history tracking
✅ Version management
✅ One-click rollback capability
✅ Deployment status notifications
✅ Release notes integration

### Alert System
✅ Custom alert rules
✅ Slack/Email notifications
✅ Alert history and analytics
✅ Escalation policies
✅ Alert acknowledgment

### Log Management
✅ Real-time log streaming
✅ Advanced search and filtering
✅ Log aggregation
✅ Error tracking
✅ Log analytics

### Analytics & Reporting
✅ Historical metrics analysis
✅ Performance trends
✅ Uptime reports
✅ Resource utilization reports
✅ Custom report generation

### User Management
✅ JWT authentication
✅ Role-based access control (RBAC)
✅ Multi-user support
✅ Audit logging
✅ Team management

## 📋 Tech Stack

### Backend
- **Framework**: FastAPI 0.104+
- **Server**: Uvicorn
- **Database**: PostgreSQL
- **Time Series**: InfluxDB
- **Cache**: Redis
- **Task Queue**: Celery
- **Auth**: JWT + Passlib
- **Monitoring**: Prometheus client + psutil

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **UI Library**: Material-UI (MUI)
- **State Management**: Redux Toolkit
- **Charts**: Recharts
- **HTTP Client**: Axios

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **WebServer**: Nginx
- **Reverse Proxy**: Uvicorn

## 🏗️ Project Structure

```
devops-dashboard/
├── backend/                    # Python FastAPI application
│   ├── app/
│   │   ├── main.py            # FastAPI app entry point
│   │   ├── config.py          # Configuration settings
│   │   ├── database.py        # Database connection
│   │   ├── api/
│   │   │   ├── routes/        # API endpoints
│   │   │   │   ├── servers.py
│   │   │   │   ├── applications.py
│   │   │   │   ├── deployments.py
│   │   │   │   ├── alerts.py
│   │   │   │   ├── logs.py
│   │   │   │   ├── metrics.py
│   │   │   │   └── auth.py
│   │   │   └── dependencies.py
│   │   ├── models/            # Database models
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # Business logic
│   │   ├── collectors/        # Metrics collectors
│   │   ├── middleware/        # Custom middleware
│   │   └── tasks/             # Background tasks
│   ├── tests/                 # Unit tests
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile
│   └── .env.example
├── frontend/                  # React application
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   ├── services/          # API services
│   │   ├── store/             # Redux store
│   │   ├── types/             # TypeScript types
│   │   └── App.tsx
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yaml        # Full stack setup
├── nginx.conf                 # Nginx configuration
├── LICENSE
└── docs/
    ├── API.md
    ├── INSTALLATION.md
    ├── USER_GUIDE.md
    └── DEPLOYMENT.md
```

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/A1TechHQ/devops-dashboard.git
cd devops-dashboard

# Start all services
docker-compose up -d

# Wait for services to initialize (about 30 seconds)
sleep 30

# Access the dashboard
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Documentation: http://localhost:8000/docs
# Redis Commander: http://localhost:8081
```

### Default Credentials
- **Username**: `admin@example.com`
- **Password**: `admin123`

### Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn app.main:app --reload
```

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## 📊 API Documentation

### Authentication Endpoints
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration
- `POST /api/auth/logout` - User logout
- `GET /api/auth/me` - Get current user
- `POST /api/auth/refresh` - Refresh token

### Server Endpoints
- `GET /api/servers` - List all servers
- `GET /api/servers/{id}` - Get server details
- `POST /api/servers` - Register new server
- `PUT /api/servers/{id}` - Update server
- `DELETE /api/servers/{id}` - Delete server
- `GET /api/servers/{id}/metrics` - Get real-time metrics
- `GET /api/servers/{id}/history` - Get historical metrics

### Application Endpoints
- `GET /api/applications` - List applications
- `GET /api/applications/{id}` - Get app details
- `POST /api/applications` - Add application
- `GET /api/applications/{id}/health` - App health status
- `GET /api/applications/{id}/logs` - App logs
- `GET /api/applications/{id}/performance` - Performance metrics

### Deployment Endpoints
- `GET /api/deployments` - Deployment history
- `POST /api/deployments` - Create deployment
- `GET /api/deployments/{id}` - Deployment details
- `POST /api/deployments/{id}/rollback` - Rollback deployment
- `GET /api/deployments/{id}/status` - Deployment status

### Alert Endpoints
- `GET /api/alerts` - List all alerts
- `POST /api/alerts` - Create alert rule
- `PUT /api/alerts/{id}` - Update alert
- `DELETE /api/alerts/{id}` - Delete alert
- `GET /api/alerts/active` - Active alerts
- `POST /api/alerts/{id}/acknowledge` - Acknowledge alert

### Log Endpoints
- `GET /api/logs` - Search logs
- `GET /api/logs/stream` - WebSocket real-time logs
- `GET /api/logs/stats` - Log statistics

### Metrics Endpoints
- `GET /api/metrics/dashboard` - Dashboard metrics
- `GET /api/metrics/system` - System metrics
- `GET /api/metrics/applications` - Application metrics
- `GET /api/metrics/history` - Historical metrics

## 🔐 Security Features

✅ JWT authentication
✅ Password hashing (bcrypt)
✅ CORS protection
✅ Rate limiting
✅ SQL injection prevention
✅ XSS protection
✅ CSRF tokens
✅ Audit logging
✅ Role-based access control
✅ Encrypted sensitive data

## 📈 Performance

- Real-time updates via WebSocket
- Handles 1000+ servers
- Efficient data caching
- Optimized database queries
- Horizontal scaling support
- Load balancing ready

## 🛠 Development

### Running Tests
```bash
cd backend
pytest
pytest --cov=app tests/
```

### Code Quality
```bash
cd backend
flake8 app/
black app/
mypy app/
```

### Building Docker Images
```bash
# Backend
docker build -f backend/Dockerfile -t devops-dashboard-backend:latest ./backend

# Frontend
docker build -f frontend/Dockerfile -t devops-dashboard-frontend:latest ./frontend
```

## 📝 Configuration

Create `.env` file in the backend directory:

```env
# Database
DATABASE_URL=postgresql://user:password@db:5432/devops_db

# Redis
REDIS_URL=redis://redis:6379

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# InfluxDB
INFLUXDB_URL=http://influxdb:8086
INFLUXDB_TOKEN=your-token
INFLUXDB_ORG=your-org
INFLUXDB_BUCKET=metrics

# Email (for alerts)
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-password

# Slack (for notifications)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK
```

## 🚀 Deployment

### Production Deployment

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for:
- Kubernetes deployment
- AWS deployment
- Azure deployment
- Docker Swarm setup
- Scaling guidelines
- Monitoring setup

## 📚 Documentation

- [API Documentation](docs/API.md)
- [Installation Guide](docs/INSTALLATION.md)
- [User Guide](docs/USER_GUIDE.md)
- [Deployment Guide](docs/DEPLOYMENT.md)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Support

- Issues: [GitHub Issues](https://github.com/A1TechHQ/devops-dashboard/issues)
- Discussions: [GitHub Discussions](https://github.com/A1TechHQ/devops-dashboard/discussions)
- Email: support@a1tech.com

---

**Made with ❤️ by A1TechHQ** - Enterprise DevOps Monitoring Platform
