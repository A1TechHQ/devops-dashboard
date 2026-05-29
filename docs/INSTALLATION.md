# Installation Guide

## Prerequisites

- Docker and Docker Compose
- Git
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)

## Quick Start with Docker Compose

### 1. Clone the Repository

```bash
git clone https://github.com/A1TechHQ/devops-dashboard.git
cd devops-dashboard
```

### 2. Start Services

```bash
docker-compose up -d
```

### 3. Wait for Services to Initialize

```bash
sleep 30
```

### 4. Access the Dashboard

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs
- Redis Commander: http://localhost:8081

## Default Credentials

- Email: `admin@example.com`
- Password: `admin123`

## Local Development

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python -m uvicorn app.main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm start
```

## Database Migration

```bash
cd backend
alembic upgrade head
```

## Troubleshooting

### Port Already in Use

If ports are already in use, modify the port mappings in `docker-compose.yaml`.

### Database Connection Error

Ensure PostgreSQL is running and accessible with the credentials specified in `.env`.

### Frontend Not Loading

Clear browser cache and restart the frontend service:

```bash
docker-compose restart frontend
```
