# Backend API

FastAPI backend application using uv for package management.

## Structure

```
api/
├── src/
│   └── app/
│       ├── api/          # Routers / controllers
│       ├── core/          # Settings, logging
│       ├── models/        # ORM / Pydantic models
│       ├── services/      # Domain logic
│       ├── db/           # DB session, migrations
│       └── main.py        # ASGI entrypoint
├── tests/                # Test files
└── pyproject.toml        # Python project configuration
```

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Run the development server:
```bash
nx serve backend
# Or manually:
cd apps/backend/api
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3. Run tests:
```bash
nx test backend
# Or manually:
cd apps/backend/api
uv run pytest
```

## Environment Variables

Create a `.env` file in `apps/backend/api/` with:

```env
PROJECT_NAME=Backend API
CORS_ORIGINS=["http://localhost:4200"]
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/health` - API v1 health check

