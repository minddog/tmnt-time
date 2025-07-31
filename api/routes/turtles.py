from fastapi import APIRouter, HTTPException
from typing import List
from api.models import Turtle
from api.data.tmnt_data import TURTLES

router = APIRouter()


@router.get("/turtles", response_model=List[Turtle])
async def get_all_turtles():
    """Get all ninja turtles"""
    return list(TURTLES.values())


@router.get("/turtles/{name}", response_model=Turtle)
async def get_turtle_by_name(name: str):
    """Get a specific turtle by name"""
    turtle_name = name.lower()
    if turtle_name not in TURTLES:
        raise HTTPException(status_code=404, detail=f"Turtle '{name}' not found")
    return TURTLES[turtle_name]