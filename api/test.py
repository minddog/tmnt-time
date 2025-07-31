from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/api/test")
async def test_endpoint():
    return {"status": "ok", "message": "Test endpoint working"}