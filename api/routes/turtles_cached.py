from fastapi import APIRouter, HTTPException, Response
from typing import List, Dict
from api.models import Turtle
from api.edge_config_client import edge_config
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
    """Get all ninja turtles from Edge Config"""
    try:
        # Set cache headers
        for key, value in CACHE_HEADERS.items():
            response.headers[key] = value
        
        # Get data from Edge Config
        turtles_data = edge_config.get('turtles')
        if not turtles_data:
            # Log the issue
            print(f"ERROR: No turtles data found in Edge Config", file=sys.stderr)
            print(f"Edge Config URL: {edge_config.edge_config_url}", file=sys.stderr)
            raise HTTPException(status_code=500, detail="Failed to load turtle data")
        
        # Convert dict to list
        return list(turtles_data.values())
    except Exception as e:
        # Log full traceback
        print(f"ERROR in get_all_turtles: {str(e)}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        if isinstance(e, HTTPException):
            raise
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")


@router.get("/turtles/{name}", response_model=Turtle)
async def get_turtle_by_name(name: str, response: Response):
    """Get a specific turtle by name from Edge Config"""
    # Set cache headers
    for key, value in CACHE_HEADERS.items():
        response.headers[key] = value
    
    # Get data from Edge Config
    turtles_data = edge_config.get('turtles')
    if not turtles_data:
        raise HTTPException(status_code=500, detail="Failed to load turtle data")
    
    turtle_name = name.lower()
    if turtle_name not in turtles_data:
        raise HTTPException(status_code=404, detail=f"Turtle '{name}' not found")
    
    return turtles_data[turtle_name]