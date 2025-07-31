from fastapi import APIRouter, HTTPException
from typing import List
from api.models import Villain
from api.data.tmnt_data import VILLAINS

router = APIRouter()


@router.get("/villains", response_model=List[Villain])
async def get_all_villains():
    """Get all TMNT villains"""
    return list(VILLAINS.values())


@router.get("/villains/{name}", response_model=Villain)
async def get_villain_by_name(name: str):
    """Get a specific villain by name"""
    villain_name = name.lower().replace(" ", "_")
    if villain_name not in VILLAINS:
        raise HTTPException(status_code=404, detail=f"Villain '{name}' not found")
    return VILLAINS[villain_name]