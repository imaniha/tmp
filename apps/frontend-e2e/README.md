# Frontend E2E Tests

End-to-end tests for the frontend application using Playwright.

## Running Tests

### Run all E2E tests

```bash
nx e2e frontend-e2e
```

### Run tests in headed mode

```bash
nx e2e frontend-e2e --headed
```

### Run tests in specific browser

```bash
nx e2e frontend-e2e --browser=chromium
nx e2e frontend-e2e --browser=firefox
nx e2e frontend-e2e --browser=webkit
```

### Run tests with UI mode

```bash
nx e2e frontend-e2e --ui
```

### Run specific test

```bash
nx e2e frontend-e2e --grep "has title"
```

## Test Structure

Tests are located in `src/example.spec.ts` and include:

- **Title verification**: Checks that the page has the expected title
- **Application display**: Verifies the app root element is visible
- **Navigation**: Tests page loading and navigation

## Configuration

The Playwright configuration is in `playwright.config.ts`:

- Automatically starts the frontend dev server before tests
- Tests against `http://localhost:4200`
- Supports multiple browsers (Chrome, Firefox, Safari)
- Configurable timeouts and retries

## CI/CD

E2E tests run automatically in CI/CD pipeline:

- Runs on every push and pull request
- Generates test reports
- Uploads Playwright reports as artifacts

## Debugging

### Run tests in debug mode

```bash
nx e2e frontend-e2e --debug
```

### View test report

After running tests, view the HTML report:

```bash
npx playwright show-report
```

## Best Practices

1. **Keep tests fast**: E2E tests should complete quickly
2. **Test critical paths**: Focus on important user flows
3. **Use page objects**: Organize tests with page object pattern
4. **Isolate tests**: Each test should be independent
5. **Use data-testid**: Prefer test IDs over CSS selectors

