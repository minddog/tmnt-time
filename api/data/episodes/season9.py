"""
TMNT 1987 Series - Season 9 Episodes (1995)
Total Episodes: 8
Continuation of the "Red Sky" era with Lord Dregg as main villain
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 9
SEASON9_RECURRING_CAST = {
    "Lord Dregg": {"character_name": "Lord Dregg", "voice_actor": "Tony Jay", "role": "main_villain"},
    "Mung": {"character_name": "Mung", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Carter": {"character_name": "Carter", "voice_actor": "Michael Dorn", "role": "main"},
    "Shredder": {"character_name": "Shredder", "voice_actor": "Dorian Harewood", "role": "guest"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "guest"},
}

SEASON9_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 169,
        "title": "The Unknown Ninja",
        "season": 9,
        "episode_number": 1,
        "air_date": "1995-09-16",
        "synopsis": "A mysterious ninja appears in New York, and the Turtles must determine if they are friend or foe while battling Dregg's forces.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Lord Dregg"], 
            SEASON9_RECURRING_CAST["Carter"],
            {"character_name": "Unknown Ninja", "voice_actor": "Jennifer Darling", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg"],
        "notes": "Season 9 premiere"
    },
    {
        "episode_id": 170,
        "title": "Dregg of the Earth",
        "season": 9,
        "episode_number": 2,
        "air_date": "1995-09-23",
        "synopsis": "Lord Dregg unleashes a virus that begins transforming humans into insect drones under his control.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Lord Dregg"], 
            SEASON9_RECURRING_CAST["Mung"],
            SEASON9_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Viral transformation episode"
    },
    {
        "episode_id": 171,
        "title": "The Wrath of Medusa",
        "season": 9,
        "episode_number": 3,
        "air_date": "1995-09-30",
        "synopsis": "Dregg awakens Medusa, who can turn anyone who looks at her into stone, to eliminate the Turtles.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Lord Dregg"],
            {"character_name": "Medusa", "voice_actor": "B.J. Ward", "role": "guest"},
            SEASON9_RECURRING_CAST["Carter"]
        ],
        "writer": "Jeffrey Scott",
        "director": "Fred Wolf",
        "villains_featured": ["Medusa", "Lord Dregg"],
        "notes": "Mythological villain"
    },
    {
        "episode_id": 172,
        "title": "The New Mutation",
        "season": 9,
        "episode_number": 4,
        "air_date": "1995-10-07",
        "synopsis": "Carter's mutations become unstable, and he struggles to control his transformations while the Turtles search for a cure.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Carter"],
            SEASON9_RECURRING_CAST["Lord Dregg"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg"],
        "notes": "Carter mutation focus"
    },
    {
        "episode_id": 173,
        "title": "The Showdown",
        "season": 9,
        "episode_number": 5,
        "air_date": "1995-10-14",
        "synopsis": "Dregg challenges the Turtles to a final showdown, but it's a trap to steal their life force energy.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Lord Dregg"], 
            SEASON9_RECURRING_CAST["Mung"],
            SEASON9_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Trap episode"
    },
    {
        "episode_id": 174,
        "title": "Split-Second",
        "season": 9,
        "episode_number": 6,
        "air_date": "1995-10-21",
        "synopsis": "Carter gains super-speed abilities but struggles to control them, causing chaos throughout the city.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Carter"],
            SEASON9_RECURRING_CAST["Lord Dregg"]
        ],
        "writer": "Jeffrey Scott",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg"],
        "notes": "Super-speed episode"
    },
    {
        "episode_id": 175,
        "title": "Carter, the Enforcer",
        "season": 9,
        "episode_number": 7,
        "air_date": "1995-10-28",
        "synopsis": "Dregg brainwashes Carter into becoming his enforcer, forcing the Turtles to fight their friend.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Carter"],
            SEASON9_RECURRING_CAST["Lord Dregg"], 
            SEASON9_RECURRING_CAST["Mung"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung", "Carter (brainwashed)"],
        "notes": "Brainwashed ally episode"
    },
    {
        "episode_id": 176,
        "title": "Doomquest",
        "season": 9,
        "episode_number": 8,
        "air_date": "1995-11-04",
        "synopsis": "Lord Dregg opens a portal to the Apocalypse Dimension, threatening to merge it with Earth and end all life.",
        "cast": MAIN_CAST + [
            SEASON9_RECURRING_CAST["Lord Dregg"], 
            SEASON9_RECURRING_CAST["Mung"],
            SEASON9_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Season 9 finale - Apocalyptic threat"
    }
]