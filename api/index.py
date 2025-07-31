# Simple test API without Edge Config
from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="TMNT API - Simple Test",
    description="Testing basic API functionality",
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

@app.get("/api")
async def api_root():
    """API root endpoint"""
    return {
        "message": "Welcome to the TMNT API!",
        "status": "simple_test",
        "version": "1.0.0"
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "mode": "simple"}