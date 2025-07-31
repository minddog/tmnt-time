from fastapi import APIRouter, HTTPException, Response
from typing import List
from api.models import Villain
from api.edge_config_client import edge_config

router = APIRouter()

# Cache for 1 hour for static villain data
CACHE_HEADERS = {
    "Cache-Control": "public, s-maxage=3600, stale-while-revalidate=86400",
    "CDN-Cache-Control": "max-age=3600",
    "Vercel-CDN-Cache-Control": "max-age=3600"
}


@router.get("/villains", response_model=List[Villain])
async def get_all_villains(response: Response):
    """Get all TMNT villains from Edge Config"""
    # Set cache headers
    for key, value in CACHE_HEADERS.items():
        response.headers[key] = value
    
    # Get data from Edge Config
    villains_data = edge_config.get('villains')
    if not villains_data:
        raise HTTPException(status_code=500, detail="Failed to load villain data")
    
    return list(villains_data.values())


@router.get("/villains/{name}", response_model=Villain)
async def get_villain_by_name(name: str, response: Response):
    """Get a specific villain by name from Edge Config"""
    # Set cache headers
    for key, value in CACHE_HEADERS.items():
        response.headers[key] = value
    
    # Get data from Edge Config
    villains_data = edge_config.get('villains')
    if not villains_data:
        raise HTTPException(status_code=500, detail="Failed to load villain data")
    
    villain_name = name.lower().replace(" ", "_")
    if villain_name not in villains_data:
        raise HTTPException(status_code=404, detail=f"Villain '{name}' not found")
    
    return villains_data[villain_name]