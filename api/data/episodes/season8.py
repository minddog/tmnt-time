"""
TMNT 1987 Series - Season 8 Episodes (1994)
Total Episodes: 8
The "Red Sky" seasons begin - darker tone and connected storylines
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 8
SEASON8_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "Dorian Harewood", "role": "recurring"},  # New voice actor
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Lord Dregg": {"character_name": "Lord Dregg", "voice_actor": "Tony Jay", "role": "main_villain"},
    "Mung": {"character_name": "Mung", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Carter": {"character_name": "Carter", "voice_actor": "Michael Dorn", "role": "main"},
}

SEASON8_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 161,
        "title": "Get Shredder!",
        "season": 8,
        "episode_number": 1,
        "air_date": "1994-09-17",
        "synopsis": "The Turtles and Shredder are transported to Dimension X where they must work together to survive. The sky turns red permanently.",
        "cast": MAIN_CAST + [
            SEASON8_RECURRING_CAST["Shredder"], 
            SEASON8_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Season 8 premiere - Beginning of Red Sky era"
    },
    {
        "episode_id": 162,
        "title": "Wrath of the Rat King",
        "season": 8,
        "episode_number": 2,
        "air_date": "1994-09-24",
        "synopsis": "The Rat King returns more powerful than ever, controlling an army of rats to take over the city.",
        "cast": MAIN_CAST + [
            {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Rat King"],
        "notes": "Darker Rat King episode"
    },
    {
        "episode_id": 163,
        "title": "State of Shock",
        "season": 8,
        "episode_number": 3,
        "air_date": "1994-10-01",
        "synopsis": "A mysterious alien warlord named Lord Dregg arrives on Earth, promising to solve the city's problems while secretly planning conquest.",
        "cast": MAIN_CAST + [
            SEASON8_RECURRING_CAST["Lord Dregg"], 
            SEASON8_RECURRING_CAST["Mung"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Introduction of Lord Dregg - new main villain"
    },
    {
        "episode_id": 164,
        "title": "Cry H.A.V.O.C.!",
        "season": 8,
        "episode_number": 4,
        "air_date": "1994-10-08",
        "synopsis": "Lord Dregg creates mutant soldiers called H.A.V.O.C. mutants to enforce his rule over the city.",
        "cast": MAIN_CAST + [
            SEASON8_RECURRING_CAST["Lord Dregg"], 
            SEASON8_RECURRING_CAST["Mung"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung", "H.A.V.O.C. mutants"],
        "notes": "Introduction of H.A.V.O.C. mutants"
    },
    {
        "episode_id": 165,
        "title": "H.A.V.O.C. in the Streets",
        "season": 8,
        "episode_number": 5,
        "air_date": "1994-10-15",
        "synopsis": "The H.A.V.O.C. mutants rebel against Dregg and rampage through the city, forcing the Turtles to stop them.",
        "cast": MAIN_CAST + [
            SEASON8_RECURRING_CAST["Lord Dregg"], 
            SEASON8_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["H.A.V.O.C. mutants", "Lord Dregg"],
        "notes": "Introduction of Carter"
    },
    {
        "episode_id": 166,
        "title": "Enter: Krakus",
        "season": 8,
        "episode_number": 6,
        "air_date": "1994-10-22",
        "synopsis": "A mutant sea creature named Krakus emerges from the ocean depths to challenge both the Turtles and Dregg.",
        "cast": MAIN_CAST + [
            {"character_name": "Krakus", "voice_actor": "Jim Cummings", "role": "guest"},
            SEASON8_RECURRING_CAST["Lord Dregg"],
            SEASON8_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Krakus", "Lord Dregg"],
        "notes": "Sea monster episode"
    },
    {
        "episode_id": 167,
        "title": "Shredder Triumphant!",
        "season": 8,
        "episode_number": 7,
        "air_date": "1994-10-29",
        "synopsis": "Shredder and Krang escape from Dimension X and launch one final assault on the Turtles with the rebuilt Technodrome.",
        "cast": MAIN_CAST + [
            SEASON8_RECURRING_CAST["Shredder"], 
            SEASON8_RECURRING_CAST["Krang"],
            {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
            {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Return of classic villains"
    },
    {
        "episode_id": 168,
        "title": "Turtle Trek",
        "season": 8,
        "episode_number": 8,
        "air_date": "1994-11-05",
        "synopsis": "Lord Dregg captures the Turtles and transports them across the galaxy to fight in alien gladiator games.",
        "cast": MAIN_CAST + [
            SEASON8_RECURRING_CAST["Lord Dregg"], 
            SEASON8_RECURRING_CAST["Mung"],
            SEASON8_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Season 8 finale - Space adventure"
    }
]