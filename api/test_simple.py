from fastapi import FastAPI, Response, Query
from typing import Optional

app = FastAPI()

@app.get("/api/test/simple")
async def test_simple():
    return {"status": "ok"}

@app.get("/api/test/with_response")
async def test_with_response(response: Response):
    response.headers["X-Test"] = "working"
    return {"status": "ok with response"}

@app.get("/api/test/with_params")
async def test_with_params(response: Response, q: str = Query("default")):
    return {"status": "ok", "query": q}

@app.get("/api/test/optional_param")  
async def test_optional(response: Response, opt: Optional[str] = None):
    return {"status": "ok", "optional": opt}