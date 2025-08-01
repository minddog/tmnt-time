# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a full-stack TMNT (Teenage Mutant Ninja Turtles) themed web application with a FastAPI backend and vanilla JavaScript frontend, deployed on Vercel with Convex database and Edge Config caching.

## Essential Commands

### Development
```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies (for Convex and Edge Config)
npm install

# Run local development server
uvicorn api.main:app --reload

# The application uses api/index.py as the Vercel entry point
```

### Testing
```bash
# Run Python unit tests
pytest tests/ -v

# Run comprehensive test suites
./scripts/run-all-tests.sh           # All tests
./scripts/regression-test-suite.sh   # Functional tests
./scripts/performance-test-suite.sh  # Load and cache tests
./scripts/security-test-suite.sh     # Security tests
./scripts/quick-validation.sh        # Quick endpoint validation

# Run a single test
pytest tests/test_api.py::test_get_all_turtles -v
```

### Database Setup (Convex)
```bash
# Populate Convex database with TMNT data
python scripts/populate_convex.py

# Clear Convex database
python scripts/clear_convex.py

# Add new episodes to database
python scripts/add_all_episodes.py
```

### Edge Config Setup
```bash
# Interactive setup wizard
npm run edge-config-wizard

# Manual hydration
node scripts/hydrate-edge-config.js

# Setup Edge Config
npm run setup-edge-config
```

### Deployment
```bash
# Deploy to Vercel
vercel --prod

# The deployment uses GitHub Actions CI/CD pipeline (.github/workflows/deploy.yml)
```

## Architecture

### Data Layer Architecture
- **Primary Database**: Convex serverless database (convex/schema.ts defines tables for turtles, villains, episodes, quotes, weapons)
- **Caching Layer**: Vercel Edge Config for ultra-low latency responses
- **Fallback Data**: Static data in api/data/tmnt_data.py

### API Structure
- **Entry Point**: api/index.py (Vercel serverless function entry)
- **Framework**: FastAPI with automatic OpenAPI documentation at /docs
- **Routes**: Organized in api/routes/ with cached versions (*_cached.py)
- **Models**: Pydantic models in api/models.py
- **Clients**: 
  - api/convex_client.py for database operations
  - api/edge_config_client.py for cache operations

### Frontend Structure
- **Development**: frontend/ directory (source files)
- **Production**: public/ directory (deployed files)
- **Approach**: Vanilla JavaScript with no framework dependencies
- **Assets**: SVG character images in public/images/

### Caching Strategy
- **Edge Config**: Sub-100ms responses for frequently accessed data
- **CDN Caching**: Appropriate cache headers for static content
- **No-Cache**: Random quotes endpoint to ensure freshness

### Testing Infrastructure
- Comprehensive test suites in scripts/ directory
- API tests in tests/test_api.py
- Test documentation in TEST-SUITE-README.md and test-plan-tmnt-api.md

## Key Architectural Decisions

1. **Dual Frontend Directories**: frontend/ for development, public/ for production to optimize deployment
2. **Cached Route Pattern**: Separate *_cached.py route files for Edge Config integration
3. **Multi-Layer Data Access**: Convex → Edge Config → Static fallback for resilience
4. **Serverless Functions**: Using Vercel's serverless architecture for scalability
5. **No Frontend Framework**: Vanilla JavaScript for minimal dependencies and faster load times

## Environment Variables

Required for local development (create .env file):
```
VERCEL_TOKEN=your_vercel_api_token
EDGE_CONFIG_ID=your_edge_config_id
VERCEL_TEAM_ID=your_team_id_if_applicable (optional)
```

## API Endpoints

All endpoints are prefixed with `/api/v1/`:
- `/turtles` - List all turtles
- `/turtles/{name}` - Get specific turtle
- `/villains` - List all villains  
- `/villains/{name}` - Get specific villain
- `/episodes` - List episodes (paginated)
- `/episodes/{id}` - Get specific episode with cast details
- `/quotes/random` - Get random quote (no-cache)
- `/weapons` - List all weapons
- `/search?q={query}` - Search across all collections

Additional endpoints:
- `/api/health` - Health check
- `/api/debug/edge-config` - Edge Config status