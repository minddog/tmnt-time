# Setting Up Vercel Edge Config for TMNT Hub

This guide will help you set up Edge Config to serve TMNT data from Vercel's edge network, eliminating API function calls for static data.

## Benefits

- **Ultra-low latency**: Data served from edge locations
- **No cold starts**: No function invocations
- **Reduced costs**: No compute time for static data
- **Better caching**: Automatic CDN caching

## Automated Setup (Recommended)

### Option 1: Interactive Setup Wizard

```bash
npm run edge-config-wizard
```

This will guide you through:
1. Getting your Vercel API token
2. Creating or using existing Edge Config
3. Automatically hydrating with TMNT data

### Option 2: Direct Hydration

If you already have an Edge Config:

```bash
# Set environment variables
export VERCEL_TOKEN="your-vercel-token"
export EDGE_CONFIG_ID="ecfg_xxxx"
export VERCEL_TEAM_ID="team_xxxx"  # Optional, for team accounts

# Run hydration
npm run hydrate-edge-config
```

## Manual Setup Steps

### 1. Create Edge Config Store

1. Go to [Vercel Dashboard > Storage](https://vercel.com/dashboard/stores)
2. Click "Create Database"
3. Select "Edge Config"
4. Name it (e.g., `tmnt-data`)
5. Click "Create"

### 2. Add TMNT Data Automatically

Use the hydration script instead of manual entry:

**Key: `turtles`**
```json
{
  "leonardo": {
    "name": "leonardo",
    "full_name": "Leonardo",
    "color": "blue",
    "weapon": "Katana",
    "personality": "Leader, disciplined, responsible",
    "favorite_pizza": "Pepperoni",
    "catchphrase": "We strike hard and fade away into the night",
    "image_url": "/images/leonardo.png"
  },
  // ... add all turtles
}
```

**Key: `villains`**
```json
{
  "shredder": {
    "name": "shredder",
    "real_name": "Oroku Saki",
    "description": "The leader of the Foot Clan and arch-nemesis of the Turtles",
    "abilities": ["Master martial artist", "Strategic genius", "Bladed armor"],
    "first_appearance": "Episode 1: Turtle Tracks",
    "arch_enemy_of": "Splinter",
    "image_url": "/images/shredder.png"
  },
  // ... add all villains
}
```

**Key: `weapons`**
```json
[
  {
    "name": "Katana",
    "type": "Sword",
    "wielder": "Leonardo",
    "description": "Twin katana swords, symbols of leadership and honor",
    "special_moves": ["Double slice", "Spinning blade shield", "Precision strike"]
  },
  // ... add all weapons
]
```

**Key: `quotes`**
```json
[
  {
    "id": 1,
    "text": "Cowabunga!",
    "character": "Michelangelo",
    "context": "Battle cry"
  },
  // ... add all quotes
]
```

### 3. Connect to Your Project

1. In the Edge Config dashboard, click "Projects" tab
2. Click "Connect Project"
3. Select your `vercel-python` project
4. The `EDGE_CONFIG` environment variable will be automatically added

### 4. Use the Setup Script

Run the setup script to see all the data formatted correctly:

```bash
npm run setup-edge-config
```

Copy the output and add it to your Edge Config store.

### 5. Verify Connection

After deployment, check the health endpoint:
```bash
curl https://your-domain.vercel.app/api/health
```

Look for `"edge_config": "connected"` in the response.

## How It Works

1. **API reads from Edge Config** instead of local files
2. **Fallback mechanism** uses local data if Edge Config is unavailable
3. **Cache headers** ensure responses are cached at CDN edge
4. **No function calls** for cached responses

## Cache Strategy

- **Static data** (turtles, villains, weapons): 1 hour cache
- **Paginated data** (episodes): 1 minute cache
- **Random data** (random quotes): No cache
- **Search results**: 1 minute cache

## Monitoring

View Edge Config reads in your Vercel dashboard:
- Go to project > Functions tab
- Look for reduced invocations
- Check Edge Config metrics

## Cost Savings

With Edge Config:
- Static data requests: **0 function invocations**
- Only search and random quotes trigger functions
- Significant reduction in compute time