# CI/CD Documentation

This project uses GitHub Actions for continuous integration and continuous deployment.

## Workflows

### Main CI Pipeline (`.github/workflows/ci.yml`)

The main CI pipeline runs on every push and pull request to `main` and `develop` branches.

#### Jobs

1. **Lint** - Lints frontend and library code
2. **Test Frontend** - Runs Angular unit tests with coverage
3. **Test Backend** - Runs FastAPI/Python tests with coverage
4. **Build Frontend** - Builds Angular application for production
5. **Build Backend** - Validates backend code quality
6. **Docker Build** - Builds Docker images (only on push to main/develop)
7. **Integration Tests** - Runs integration tests with MongoDB
8. **E2E Tests** - Runs Playwright end-to-end tests
9. **Security Scan** - Scans code for vulnerabilities using Trivy
10. **Deploy** - Deploys to production (only on push to main)

### Docker Publish (`.github/workflows/docker-publish.yml`)

Publishes Docker images to GitHub Container Registry on:
- Push to `main` branch
- Tagged releases (v*)
- Manual workflow dispatch

### CodeQL Analysis (`.github/workflows/codeql.yml`)

Performs static code analysis for security vulnerabilities:
- Runs on push to main/develop
- Runs on pull requests
- Scheduled weekly

### Dependabot (`.github/dependabot.yml`)

Automatically creates pull requests for dependency updates:
- npm packages (weekly)
- Python packages (weekly)
- GitHub Actions (weekly)
- Docker images (weekly)

## Running CI Locally

### Frontend Tests

```bash
npm ci
npx nx test frontend
npx nx lint frontend
npx nx build frontend
```

### Backend Tests

```bash
cd apps/backend/api
uv sync
uv run pytest tests/ -v
```

### E2E Tests

```bash
npm ci
npx playwright install --with-deps
npx nx e2e frontend-e2e
```

## Coverage Reports

Coverage reports are uploaded to Codecov:
- Frontend coverage: `coverage/frontend/coverage-final.json`
- Backend coverage: `apps/backend/api/coverage.xml`

View coverage at: https://codecov.io/gh/imaniha/tmp

## Deployment

The deployment job runs only on pushes to the `main` branch. Update the deployment steps in `.github/workflows/ci.yml` to match your deployment strategy:

- **Static hosting**: Upload to S3/CloudFront, Vercel, Netlify
- **Container**: Push to registry and deploy to Kubernetes
- **Server**: SSH deployment or use deployment tools

## Secrets

Required secrets (set in GitHub repository settings):

- `GITHUB_TOKEN` - Automatically provided by GitHub Actions
- Additional secrets for deployment (if needed):
  - `AWS_ACCESS_KEY_ID`
  - `AWS_SECRET_ACCESS_KEY`
  - `DEPLOY_KEY`
  - etc.

## Status Badges

Add these badges to your README:

```markdown
![CI](https://github.com/imaniha/tmp/workflows/CI%2FCD%20Pipeline/badge.svg)
![CodeQL](https://github.com/imaniha/tmp/workflows/CodeQL%20Analysis/badge.svg)
[![codecov](https://codecov.io/gh/imaniha/tmp/branch/main/graph/badge.svg)](https://codecov.io/gh/imaniha/tmp)
```

## Troubleshooting

### CI Fails Locally but Passes in GitHub

- Ensure you're using the same Node.js and Python versions
- Clear caches: `npm ci` and `uv sync`
- Check for environment-specific issues

### Docker Build Fails

- Verify Dockerfile syntax
- Check build context paths
- Ensure all dependencies are included

### Tests Timeout

- Increase timeout in test configuration
- Check for hanging processes
- Review test complexity

## Best Practices

1. **Keep workflows fast**: Use caching and parallel jobs
2. **Fail fast**: Run quick checks first (lint, type check)
3. **Use matrix builds**: Test on multiple versions if needed
4. **Cache dependencies**: Use GitHub Actions cache
5. **Security**: Scan for vulnerabilities regularly
6. **Documentation**: Keep CI/CD docs up to date

