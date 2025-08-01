# TMNT Data Migration Scripts

These scripts help you populate and manage data in your Convex database.

## Prerequisites

1. A Convex account and project set up
2. Your Convex deployment URL (from the Convex dashboard)
3. Python 3.7+ with the required dependencies installed

## Setup

1. Copy `.env.local.example` to `.env.local` in the project root:
   ```bash
   cp .env.local.example .env.local
   ```

2. Edit `.env.local` and add your Convex deployment URL:
   ```
   CONVEX_URL=https://your-project-name.convex.cloud
   ```

## Scripts

### populate_convex.py

Populates your Convex database with all TMNT data (turtles, villains, episodes, quotes, and weapons).

```bash
# Using environment variable
python scripts/populate_convex.py

# Or with explicit URL
python scripts/populate_convex.py --convex-url https://your-project.convex.cloud
```

### clear_convex.py

Clears all data from your Convex database. Use with caution!

```bash
# Using environment variable
python scripts/clear_convex.py

# Or with explicit URL
python scripts/clear_convex.py --convex-url https://your-project.convex.cloud
```

## Vercel Deployment

To use Convex with your Vercel deployment:

1. Go to your Vercel project settings
2. Navigate to Environment Variables
3. Add `CONVEX_URL` with your Convex deployment URL
4. Redeploy your application

The API will automatically use Convex when the `CONVEX_URL` environment variable is set, otherwise it falls back to local data.