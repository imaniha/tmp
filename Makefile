.PHONY: dev-web dev-api test-web help

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Available targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

dev-web: ## Serve the frontend application
	@echo "Starting frontend development server..."
	nx serve frontend

dev-api: ## Serve the backend API
	@echo "Starting backend API server..."
	nx serve backend

test-web: ## Run tests for frontend and backend
	@echo "Running frontend tests..."
	nx test frontend
	@echo "Running backend tests..."
	nx test backend

