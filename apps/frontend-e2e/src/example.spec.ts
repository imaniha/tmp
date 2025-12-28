import { test, expect } from '@playwright/test';

test.describe('Frontend E2E Tests', () => {
  test('has title', async ({ page }) => {
    await page.goto('/');

    // Expect h1 to contain a substring.
    expect(await page.locator('h1').innerText()).toContain('Welcome');
  });

  test('should display frontend application', async ({ page }) => {
    await page.goto('/');

    // Check that the app root element exists
    await expect(page.locator('app-root')).toBeVisible();

    // Check that the page title is correct
    await expect(page).toHaveTitle(/frontend/);
  });

  test('should navigate and load correctly', async ({ page }) => {
    await page.goto('/');

    // Wait for the app to be fully loaded
    await page.waitForLoadState('networkidle');

    // Verify the page loaded successfully
    await expect(page.locator('body')).toBeVisible();
  });
});
