from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from api.models import Episode, Quote, Weapon
from api.data.tmnt_data import EPISODES, QUOTES, WEAPONS
import random

router = APIRouter()


@router.get("/episodes", response_model=List[Episode])
async def get_episodes(
    season: Optional[int] = Query(None, ge=1, le=10),
    limit: Optional[int] = Query(10, ge=1, le=100),
    offset: Optional[int] = Query(0, ge=0)
):
    """Get episodes with optional filtering and pagination"""
    filtered_episodes = EPISODES
    
    if season:
        filtered_episodes = [ep for ep in filtered_episodes if ep.season == season]
    
    # Apply pagination
    start = offset
    end = offset + limit
    return filtered_episodes[start:end]


@router.get("/episodes/{episode_id}", response_model=Episode)
async def get_episode_by_id(episode_id: int):
    """Get a specific episode by ID"""
    for episode in EPISODES:
        if episode.id == episode_id:
            return episode
    raise HTTPException(status_code=404, detail=f"Episode {episode_id} not found")


@router.get("/quotes/random", response_model=Quote)
async def get_random_quote():
    """Get a random TMNT quote"""
    return random.choice(QUOTES)


@router.get("/quotes", response_model=List[Quote])
async def get_all_quotes(character: Optional[str] = None):
    """Get all quotes, optionally filtered by character"""
    if character:
        return [q for q in QUOTES if q.character.lower() == character.lower()]
    return QUOTES


@router.get("/weapons", response_model=List[Weapon])
async def get_all_weapons():
    """Get all turtle weapons"""
    return WEAPONS


@router.get("/search")
async def search_tmnt(q: str = Query(..., min_length=2)):
    """Search across all TMNT data"""
    query = q.lower()
    results = {
        "turtles": [],
        "villains": [],
        "episodes": [],
        "quotes": []
    }
    
    # Search turtles
    from api.data.tmnt_data import TURTLES
    for turtle in TURTLES.values():
        if (query in turtle.name.lower() or 
            query in turtle.weapon.lower() or 
            query in turtle.personality.lower()):
            results["turtles"].append(turtle)
    
    # Search villains
    from api.data.tmnt_data import VILLAINS
    for villain in VILLAINS.values():
        if (query in villain.name.lower() or 
            query in villain.description.lower()):
            results["villains"].append(villain)
    
    # Search episodes
    for episode in EPISODES:
        if query in episode.title.lower() or query in episode.synopsis.lower():
            results["episodes"].append(episode)
    
    # Search quotes
    for quote in QUOTES:
        if query in quote.text.lower() or query in quote.character.lower():
            results["quotes"].append(quote)
    
    return results