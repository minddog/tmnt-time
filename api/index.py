# This is the entry point for Vercel
# Import the FastAPI app from main.py
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from api.routes.turtles_cached import router as turtles_router
from api.routes.villains_cached import router as villains_router
from api.routes.episodes_cached import router as episodes_router
from api.edge_config_client import edge_config

# Create the FastAPI app instance here for Vercel
app = FastAPI(
    title="TMNT API",
    description="API for Teenage Mutant Ninja Turtles information - Powered by Vercel Edge Config",
    version="2.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers with caching
app.include_router(turtles_router, prefix="/api/v1", tags=["turtles"])
app.include_router(villains_router, prefix="/api/v1", tags=["villains"])
app.include_router(episodes_router, prefix="/api/v1", tags=["episodes"])


@app.get("/api")
async def api_root(response: Response):
    """API root endpoint with documentation"""
    # Cache API info for 1 hour
    response.headers["Cache-Control"] = "public, s-maxage=3600"
    
    return {
        "message": "Welcome to the TMNT API!",
        "version": "2.0.0",
        "features": {
            "edge_config": "Data served from Vercel Edge Config",
            "caching": "Responses cached at CDN edge",
            "performance": "Ultra-low latency"
        },
        "endpoints": {
            "turtles": "/api/v1/turtles",
            "villains": "/api/v1/villains",
            "episodes": "/api/v1/episodes",
            "quotes": "/api/v1/quotes/random",
            "weapons": "/api/v1/weapons",
            "search": "/api/v1/search?q=query",
            "docs": "/docs"
        }
    }


@app.get("/api/health")
async def health_check(response: Response):
    """Health check endpoint"""
    # Don't cache health checks
    response.headers["Cache-Control"] = "no-cache"
    
    # Check Edge Config connection
    edge_status = "connected" if edge_config.edge_config_url else "fallback"
    
    return {
        "status": "healthy",
        "service": "TMNT API",
        "edge_config": edge_status,
        "version": "2.0.0"
    }


@app.get("/api/debug")
async def debug_endpoint(response: Response):
    """Debug endpoint to check Edge Config and data"""
    import os
    import sys
    response.headers["Cache-Control"] = "no-cache"
    
    # Get Edge Config URL (without token for security)
    edge_url = os.environ.get('EDGE_CONFIG', 'Not set')
    if edge_url != 'Not set':
        edge_url = edge_url.split('?')[0] + '?token=***'
    
    # Try to get turtles data
    turtles_data = None
    all_data = None
    error = None
    try:
        turtles_data = edge_config.get('turtles')
        if turtles_data:
            turtles_data = f"Loaded {len(turtles_data)} turtles"
        
        # Try to get all data to see what's available
        all_data = edge_config.get_all()
        if all_data:
            all_data = list(all_data.keys()) if isinstance(all_data, dict) else "Not a dict"
    except Exception as e:
        error = str(e)
    
    return {
        "edge_config_url": edge_url,
        "edge_config_available": bool(edge_config.edge_config_url),
        "turtles_data": turtles_data,
        "all_data_keys": all_data,
        "error": error,
        "python_version": sys.version
    }