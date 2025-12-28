# Backend API

FastAPI backend application using uv for package management.

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Run the development server:
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Project Structure

- `main.py` - FastAPI application entry point
- `app/` - Application code (routers, models, services, etc.)
- `pyproject.toml` - Python project configuration with uv

