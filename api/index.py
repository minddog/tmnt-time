# This is the entry point for Vercel
# Import the FastAPI app from main.py
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from api.routes.turtles_cached import router as turtles_router
from api.routes.villains_cached import router as villains_router
from api.routes.episodes_cached import router as episodes_router
from api.convex_client import convex_client
import json
import os
from pathlib import Path

# Create the FastAPI app instance here for Vercel
app = FastAPI(
    title="TMNT API",
    description="API for Teenage Mutant Ninja Turtles information - Powered by Convex",
    version="3.0.0"
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
        "version": "3.0.0",
        "features": {
            "convex": "Data served from Convex database",
            "caching": "Responses cached at CDN edge",
            "performance": "Ultra-low latency"
        },
        "endpoints": {
            "turtles": "/api/v1/turtles",
            "villains": "/api/v1/villains",
            "episodes": "/api/v1/episodes",
            "quotes": "/api/v1/quotes/random",
            "weapons": "/api/v1/weapons",
            "docs": "/docs"
        }
    }


@app.get("/api/health")
async def health_check(response: Response):
    """Health check endpoint"""
    # Don't cache health checks
    response.headers["Cache-Control"] = "no-cache"
    
    # Check Convex connection
    convex_status = "connected" if convex_client._connected else "fallback"
    
    return {
        "status": "healthy",
        "service": "TMNT API",
        "convex": convex_status,
        "version": "3.0.0"
    }


@app.get("/api/debug")
async def debug_endpoint(response: Response):
    """Debug endpoint to check Convex connection and data"""
    import sys
    response.headers["Cache-Control"] = "no-cache"
    
    # Get Convex URL (without sensitive data for security)
    convex_url = os.environ.get('CONVEX_URL', 'Not set')
    if convex_url != 'Not set':
        convex_url = convex_url.split('?')[0] + '?...'
    
    # Try to get data from Convex
    turtles_data = None
    villains_data = None
    episodes_count = None
    quotes_data = None
    random_quote_data = None
    error = None
    quotes_error = None
    try:
        turtles = convex_client.get_turtles()
        turtles_data = f"Loaded {len(turtles)} turtles" if turtles else "No turtles data"
        
        villains = convex_client.get_villains()
        villains_data = f"Loaded {len(villains)} villains" if villains else "No villains data"
        
        episodes = convex_client.get_episodes()
        episodes_count = f"Loaded {len(episodes)} episodes" if episodes else "No episodes data"
        
        quotes = convex_client.get_quotes()
        quotes_data = f"Loaded {len(quotes)} quotes" if quotes else "No quotes data"
        
        # Try to get a random quote
        try:
            random_quote = convex_client.get_random_quote()
            random_quote_data = f"Random quote: {random_quote}" if random_quote else "No random quote"
        except Exception as e:
            quotes_error = f"Random quote error: {type(e).__name__}: {str(e)}"
            import traceback
            quotes_error += "\n" + traceback.format_exc()
            
    except Exception as e:
        error = f"{type(e).__name__}: {str(e)}"
        import traceback
        error += "\n" + traceback.format_exc()
    
    return {
        "convex_url": convex_url,
        "convex_connected": convex_client._connected,
        "turtles_data": turtles_data,
        "villains_data": villains_data,
        "episodes_count": episodes_count,
        "quotes_data": quotes_data,
        "random_quote_data": random_quote_data,
        "error": error,
        "quotes_error": quotes_error,
        "python_version": sys.version
    }


# Serve static files and homepage
# Get the public directory path
base_dir = Path(__file__).parent.parent
public_dir = base_dir / "public"

# Mount static files for CSS, JS, images
app.mount("/css", StaticFiles(directory=public_dir / "css"), name="css")
app.mount("/js", StaticFiles(directory=public_dir / "js"), name="js")
app.mount("/images", StaticFiles(directory=public_dir / "images"), name="images")
app.mount("/pages", StaticFiles(directory=public_dir / "pages"), name="pages")

# Serve index.html at root
@app.get("/")
async def serve_homepage():
    """Serve the homepage"""
    return FileResponse(public_dir / "index.html")

# Serve favicon
@app.get("/favicon.svg")
async def serve_favicon():
    """Serve the favicon"""
    return FileResponse(public_dir / "favicon.svg")




