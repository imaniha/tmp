FROM python:3.11-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml .python-version ./

# Install dependencies
RUN uv sync

# Copy application code
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Set Python path
ENV PYTHONPATH=/app/src

# Run the application
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

