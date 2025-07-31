from fastapi import FastAPI

# Create the FastAPI app
app = FastAPI()

@app.get("/api")
async def root():
    return {"message": "Hello from TMNT API", "status": "working"}

@app.get("/api/health")
async def health():
    return {"status": "healthy"}

# This is the line Vercel needs
handler = app