from pydantic import BaseModel
from typing import List, Optional


class Turtle(BaseModel):
    name: str
    full_name: str
    color: str
    weapon: str
    personality: str
    favorite_pizza: str
    catchphrase: str
    image_url: Optional[str] = None


class Villain(BaseModel):
    name: str
    real_name: Optional[str] = None
    description: str
    abilities: List[str]
    first_appearance: str
    threat_level: str
    arch_enemy_of: Optional[str] = None
    image_url: Optional[str] = None


class CastMember(BaseModel):
    character_name: str
    voice_actor: str
    role: str  # "main", "guest", "recurring"

class Episode(BaseModel):
    id: int
    title: str
    season: int
    episode_number: int
    air_date: Optional[str] = None
    synopsis: str
    villains_featured: List[str] = []
    cast: List[CastMember] = []
    writer: Optional[str] = None
    director: Optional[str] = None
    notes: Optional[str] = None


class Quote(BaseModel):
    id: Optional[int] = None
    text: str
    character: str
    episode: Optional[str] = None
    context: Optional[str] = None


class Weapon(BaseModel):
    name: str
    type: str
    wielder: str
    description: str
    special_moves: List[str] = []