# Monorepo Workspace

An Nx-style monorepo with Angular frontend applications and a FastAPI backend.

## Structure

```
monorepo/
├── apps/
│   ├── backend/          # FastAPI backend (Python with uv)
│   └── [Angular apps]    # Angular applications (to be created)
├── libs/
│   ├── ui/               # Shared UI components
│   ├── domain/           # Domain models and business logic
│   └── api-client/       # API client libraries
└── [config files]
```

## Prerequisites

- Node.js (v18 or higher)
- Python 3.11+
- uv package manager ([installation guide](https://github.com/astral-sh/uv))

## Getting Started

### Install Dependencies

```bash
# Install Node.js dependencies
npm install

# Install Python dependencies for backend
cd apps/backend
uv sync
cd ../..
```

### Development

#### Backend (FastAPI)

```bash
# Run backend server
nx serve backend

# Or manually:
cd apps/backend
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The backend API will be available at `http://localhost:8000`

#### Frontend (Angular)

To create a new Angular application:

```bash
nx generate @nx/angular:application my-app
```

Then serve it:

```bash
nx serve my-app
```

### Building

```bash
# Build all projects
nx build

# Build specific project
nx build <project-name>
```

### Testing

```bash
# Run all tests
nx test

# Run tests for specific project
nx test <project-name>
```

### Linting

```bash
# Lint all projects
nx lint

# Lint specific project
nx lint <project-name>
```

## Shared Libraries

### @workspace/ui

Shared Angular UI components library.

```typescript
import { UiModule } from '@workspace/ui';
```

### @workspace/domain

Shared domain models and TypeScript interfaces.

```typescript
import { User, ApiResponse } from '@workspace/domain';
```

### @workspace/api-client

API client library for backend communication.

```typescript
import { ApiClient } from '@workspace/api-client';

const client = new ApiClient({ baseUrl: 'http://localhost:8000' });
```

## Project Graph

View the project dependency graph:

```bash
nx graph
```

## Learn More

- [Nx Documentation](https://nx.dev)
- [Angular Documentation](https://angular.io)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [uv Documentation](https://github.com/astral-sh/uv)

