from fastapi import APIRouter, HTTPException, Response
from typing import List, Dict
from api.models import Turtle
from api.convex_client import convex_client
import json
import traceback
import sys

router = APIRouter()

# Cache for 1 hour for static turtle data
CACHE_HEADERS = {
    "Cache-Control": "public, s-maxage=3600, stale-while-revalidate=86400",
    "CDN-Cache-Control": "max-age=3600",
    "Vercel-CDN-Cache-Control": "max-age=3600"
}


@router.get("/turtles", response_model=List[Turtle])
async def get_all_turtles(response: Response):
    """Get all ninja turtles from Convex"""
    try:
        # Set cache headers
        for key, value in CACHE_HEADERS.items():
            response.headers[key] = value
        
        # Get data from Convex
        turtles_data = convex_client.get_turtles()
        if not turtles_data:
            # Log the issue
            print(f"ERROR: No turtles data found in Convex", file=sys.stderr)
            raise HTTPException(status_code=500, detail="Failed to load turtle data")
        
        return turtles_data
    except Exception as e:
        # Log full traceback
        print(f"ERROR in get_all_turtles: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        if isinstance(e, HTTPException):
            raise
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")


@router.get("/turtles/{name}", response_model=Turtle)
async def get_turtle_by_name(name: str, response: Response):
    """Get a specific turtle by name from Convex"""
    # Set cache headers
    for key, value in CACHE_HEADERS.items():
        response.headers[key] = value
    
    # Get data from Convex
    turtle_data = convex_client.get_turtle(name.lower())
    if not turtle_data:
        raise HTTPException(status_code=404, detail=f"Turtle '{name}' not found")
    
    return turtle_data