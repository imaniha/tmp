# Enabling GitHub Actions

GitHub Actions are typically **enabled by default** for all repositories. However, if you need to verify or enable them, follow these steps:

## Verify Actions are Enabled

1. Go to your repository: https://github.com/imaniha/tmp
2. Click on **Settings** (top menu)
3. Click on **Actions** in the left sidebar
4. Under **Actions permissions**, verify that:
   - "Allow all actions and reusable workflows" is selected, OR
   - "Allow local actions and reusable workflows" is selected

## Enable Actions (if disabled)

If Actions are disabled:

1. Go to **Settings** → **Actions**
2. Under **Actions permissions**, select:
   - **"Allow all actions and reusable workflows"** (recommended for CI/CD)
   - OR **"Allow local actions and reusable workflows"** (more restrictive)

3. Click **Save**

## Verify Workflows are Running

After enabling, you can verify workflows are working:

1. Go to the **Actions** tab in your repository
2. You should see workflow runs listed
3. Push a commit or create a PR to trigger the workflows

## Quick Verification via Command Line

```bash
# Check if Actions are enabled
gh api repos/imaniha/tmp/actions/permissions

# View workflow runs
gh run list --repo imaniha/tmp

# View a specific workflow
gh workflow view ci.yml --repo imaniha/tmp
```

## Troubleshooting

### Actions Tab Not Visible

- Ensure you have admin access to the repository
- Check if the repository is archived (Actions are disabled for archived repos)

### Workflows Not Running

- Verify `.github/workflows/` directory exists with workflow files
- Check that workflow files have valid YAML syntax
- Ensure workflows are triggered by the correct events (push, PR, etc.)

### Permission Errors

- Check repository settings → Actions → Actions permissions
- Verify branch protection rules allow Actions to run
- Check if organization policies restrict Actions

## Next Steps

Once Actions are enabled:

1. **Push your code** - This will trigger the CI pipeline
2. **Check the Actions tab** - View workflow runs and results
3. **Set up secrets** (if needed) - Go to Settings → Secrets and variables → Actions
4. **Configure branch protection** - Require status checks to pass before merging

## Required Secrets (Optional)

If you plan to deploy or use external services, you may need to add secrets:

- Go to **Settings** → **Secrets and variables** → **Actions**
- Click **New repository secret**
- Add secrets like:
  - `AWS_ACCESS_KEY_ID` (for AWS deployments)
  - `AWS_SECRET_ACCESS_KEY` (for AWS deployments)
  - `DEPLOY_KEY` (for SSH deployments)
  - etc.

## Status

✅ GitHub Actions should be **enabled by default** for your repository.

To verify, simply push a commit and check the **Actions** tab in your repository.

