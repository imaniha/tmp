# Docker Compose Setup

This project includes a Docker Compose configuration for running the entire monorepo stack.

## Services

- **db**: MongoDB database (port 27017)
- **api**: FastAPI backend (port 8000)
- **web**: Angular frontend (port 4200)
- **dev**: Development orchestrator service (provides status and watches services)

## Prerequisites

- Docker
- Docker Compose

## Usage

### Start development environment (recommended)

Start all services with the dev profile for end-to-end development:

```bash
docker-compose --profile dev up
```

Or use the dev service which provides a nice status output:

```bash
docker-compose --profile dev up dev
```

### Start all services (without dev profile)

```bash
docker-compose up
```

### Start in detached mode

```bash
docker-compose --profile dev up -d
```

### Stop all services

```bash
docker-compose --profile dev down
```

### Stop and remove volumes

```bash
docker-compose down -v
```

### Rebuild services

```bash
docker-compose --profile dev build
```

## Development Workflow

For end-to-end development, use the `dev` profile:

```bash
# Start everything with dev profile
docker-compose --profile dev up

# Or start just the dev orchestrator (it will start dependencies)
docker-compose --profile dev up dev
```

The `dev` service provides:
- Status information about all services
- Service URLs and access points
- Helpful tips and commands
- Continuous monitoring of the development environment

### View logs

```bash
# All services
docker-compose --profile dev logs -f

# Specific service
docker-compose --profile dev logs -f api
docker-compose --profile dev logs -f web
docker-compose --profile dev logs -f db
docker-compose --profile dev logs -f dev
```

## Accessing Services

- **Frontend**: http://localhost:4200
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **MongoDB**: localhost:27017

## Database Connection

The backend is automatically connected to MongoDB. You can test the connection by calling:

```bash
curl http://localhost:8000/api/v1/db-test
```

## Environment Variables

You can override environment variables by creating a `.env` file or modifying the `docker-compose.yml` file.

### MongoDB Credentials

- Username: `admin`
- Password: `admin123`
- Database: `monorepo_db`

**Note**: Change these credentials in production!

## Development

For development, the services use volume mounts for hot-reloading:
- Frontend code changes are reflected immediately
- Backend code changes trigger auto-reload

## Production

For production deployment, you should:
1. Remove volume mounts
2. Use production builds
3. Set secure environment variables
4. Use proper secrets management
5. Configure proper networking and security

