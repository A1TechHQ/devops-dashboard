# DevOps Dashboard API Documentation

## Base URL

```
http://localhost:8000
```

## Authentication

All endpoints (except login) require JWT Bearer token authentication.

### Header Format

```
Authorization: Bearer <token>
```

## Endpoints

### Authentication

#### Login
```
POST /api/auth/login
Query Parameters:
  - email: string (required)
  - password: string (required)

Response:
{
  "access_token": "string",
  "token_type": "bearer",
  "expires_in": 1800
}
```

#### Register
```
POST /api/auth/register
Body:
{
  "email": "user@example.com",
  "password": "password123",
  "full_name": "John Doe",
  "role": "viewer"
}
```

#### Get Current User
```
GET /api/auth/me
```

### Servers

#### List Servers
```
GET /api/servers?skip=0&limit=10
```

#### Get Server
```
GET /api/servers/{server_id}
```

#### Create Server
```
POST /api/servers
Body:
{
  "name": "Server 1",
  "hostname": "server1.example.com",
  "ip_address": "192.168.1.1",
  "description": "Production server"
}
```

#### Get Server Metrics
```
GET /api/servers/{server_id}/metrics
```

#### Get Server History
```
GET /api/servers/{server_id}/history?hours=24
```

### Applications

#### List Applications
```
GET /api/applications
```

#### Get Application Health
```
GET /api/applications/{app_id}/health
```

### Deployments

#### List Deployments
```
GET /api/deployments
```

#### Rollback Deployment
```
POST /api/deployments/{deployment_id}/rollback
```

### Alerts

#### List Alerts
```
GET /api/alerts
```

#### Get Active Alerts
```
GET /api/alerts/active
```

#### Acknowledge Alert
```
POST /api/alerts/{alert_id}/acknowledge
```

### Logs

#### Search Logs
```
GET /api/logs?level=ERROR&source=application&skip=0&limit=100
```

#### Get Log Statistics
```
GET /api/logs/stats
```

### Metrics

#### Dashboard Metrics
```
GET /api/metrics/dashboard
```

#### System Metrics
```
GET /api/metrics/system
```
