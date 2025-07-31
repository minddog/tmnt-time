# This is the entry point for Vercel
# Import the FastAPI app from main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import turtles, villains, episodes

# Create the FastAPI app instance here for Vercel
app = FastAPI(
    title="TMNT API",
    description="API for Teenage Mutant Ninja Turtles information",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(turtles.router, prefix="/api/v1", tags=["turtles"])
app.include_router(villains.router, prefix="/api/v1", tags=["villains"])
app.include_router(episodes.router, prefix="/api/v1", tags=["episodes"])


@app.get("/api")
async def api_root():
    """API root endpoint with documentation"""
    return {
        "message": "Welcome to the TMNT API!",
        "version": "1.0.0",
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
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "TMNT API"}