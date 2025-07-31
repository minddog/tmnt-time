from fastapi import APIRouter, Query, HTTPException, Response
from typing import List, Optional
from api.models import Episode, Quote, Weapon
from api.edge_config_client import edge_config
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
    
    episodes_data = edge_config.get('episodes')
    if not episodes_data:
        # Fallback to original data
        from api.data.tmnt_data import EPISODES
        episodes_data = [ep.dict() for ep in EPISODES]
    
    filtered_episodes = episodes_data
    
    if season:
        filtered_episodes = [ep for ep in filtered_episodes if ep['season'] == season]
    
    # Apply pagination
    start = offset
    end = offset + limit
    return filtered_episodes[start:end]


@router.get("/episodes/{episode_id}", response_model=Episode)
async def get_episode_by_id(episode_id: int, response: Response):
    """Get a specific episode by ID"""
    for key, value in STATIC_CACHE.items():
        response.headers[key] = value
    
    episodes_data = edge_config.get('episodes')
    if not episodes_data:
        from api.data.tmnt_data import EPISODES
        episodes_data = [ep.dict() for ep in EPISODES]
    
    for episode in episodes_data:
        if episode['id'] == episode_id:
            return episode
    
    raise HTTPException(status_code=404, detail=f"Episode {episode_id} not found")


@router.get("/quotes/random", response_model=Quote)
async def get_random_quote(response: Response):
    """Get a random TMNT quote - no cache for randomness"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    
    quotes_data = edge_config.get('quotes')
    if not quotes_data:
        from api.data.tmnt_data import QUOTES
        quotes_data = [q.dict() for q in QUOTES]
    
    return random.choice(quotes_data)


@router.get("/quotes", response_model=List[Quote])
async def get_all_quotes(response: Response, character: Optional[str] = None):
    """Get all quotes, optionally filtered by character"""
    for key, value in STATIC_CACHE.items():
        response.headers[key] = value
    
    quotes_data = edge_config.get('quotes')
    if not quotes_data:
        from api.data.tmnt_data import QUOTES
        quotes_data = [q.dict() for q in QUOTES]
    
    if character:
        return [q for q in quotes_data if q['character'].lower() == character.lower()]
    return quotes_data


@router.get("/weapons", response_model=List[Weapon])
async def get_all_weapons(response: Response):
    """Get all turtle weapons"""
    for key, value in STATIC_CACHE.items():
        response.headers[key] = value
    
    weapons_data = edge_config.get('weapons')
    if not weapons_data:
        from api.data.tmnt_data import WEAPONS
        weapons_data = [w.dict() for w in WEAPONS]
    
    return weapons_data


@router.get("/search")
async def search_tmnt(response: Response, q: str = Query(..., min_length=2)):
    """Search across all TMNT data"""
    # Short cache for search results
    for key, value in DYNAMIC_CACHE.items():
        response.headers[key] = value
    
    query = q.lower()
    results = {
        "turtles": [],
        "villains": [],
        "episodes": [],
        "quotes": []
    }
    
    # Get all data from Edge Config
    config_data = edge_config.get_all()
    
    # Search turtles
    if 'turtles' in config_data:
        for turtle in config_data['turtles'].values():
            if (query in turtle['name'].lower() or 
                query in turtle['weapon'].lower() or 
                query in turtle['personality'].lower() or
                query in turtle.get('favorite_pizza', '').lower() or
                query in turtle.get('catchphrase', '').lower()):
                results["turtles"].append(turtle)
    
    # Search villains
    if 'villains' in config_data:
        for villain in config_data['villains'].values():
            if (query in villain['name'].lower() or 
                query in villain['description'].lower() or
                query in villain.get('real_name', '').lower() or
                any(query in ability.lower() for ability in villain.get('abilities', []))):
                results["villains"].append(villain)
    
    # Search episodes
    if 'episodes' in config_data:
        for episode in config_data['episodes']:
            if query in episode['title'].lower() or query in episode['synopsis'].lower():
                results["episodes"].append(episode)
    
    # Search quotes
    if 'quotes' in config_data:
        for quote in config_data['quotes']:
            if query in quote['text'].lower() or query in quote['character'].lower():
                results["quotes"].append(quote)
    
    return results