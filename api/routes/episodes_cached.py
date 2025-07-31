from fastapi import APIRouter, Query, HTTPException, Response
from typing import List, Optional
from api.models import Episode, Quote, Weapon
from api.convex_client import convex_client
import random

router = APIRouter()

# Different cache strategies for different endpoints
STATIC_CACHE = {
    "Cache-Control": "public, s-maxage=3600, stale-while-revalidate=86400",
    "CDN-Cache-Control": "max-age=3600"
}

DYNAMIC_CACHE = {
    "Cache-Control": "public, s-maxage=60, stale-while-revalidate=300",
    "CDN-Cache-Control": "max-age=60"
}


@router.get("/episodes", response_model=List[Episode])
async def get_episodes(
    response: Response,
    season: Optional[int] = Query(None, ge=1, le=10),
    limit: Optional[int] = Query(10, ge=1, le=100),
    offset: Optional[int] = Query(0, ge=0)
):
    """Get episodes with optional filtering and pagination"""
    # Use shorter cache for paginated results
    for key, value in DYNAMIC_CACHE.items():
        response.headers[key] = value
    
    episodes_data = convex_client.get_episodes(season=season, limit=limit, offset=offset)
    return episodes_data


@router.get("/episodes/{episode_id}", response_model=Episode)
async def get_episode_by_id(episode_id: int, response: Response):
    """Get a specific episode by ID"""
    for key, value in STATIC_CACHE.items():
        response.headers[key] = value
    
    episode_data = convex_client.get_episode(episode_id)
    if not episode_data:
        raise HTTPException(status_code=404, detail=f"Episode {episode_id} not found")
    
    return episode_data


@router.get("/quotes/random", response_model=Quote)
async def get_random_quote(response: Response):
    """Get a random TMNT quote - no cache for randomness"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    
    quote_data = convex_client.get_random_quote()
    if not quote_data:
        raise HTTPException(status_code=500, detail="Failed to get random quote")
    
    return quote_data


@router.get("/quotes", response_model=List[Quote])
async def get_all_quotes(response: Response, character: Optional[str] = None):
    """Get all quotes, optionally filtered by character"""
    for key, value in STATIC_CACHE.items():
        response.headers[key] = value
    
    quotes_data = convex_client.get_quotes(character=character)
    return quotes_data


@router.get("/weapons", response_model=List[Weapon])
async def get_all_weapons(response: Response):
    """Get all turtle weapons"""
    for key, value in STATIC_CACHE.items():
        response.headers[key] = value
    
    weapons_data = convex_client.get_weapons()
    return weapons_data


