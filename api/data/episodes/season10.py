"""
TMNT 1987 Series - Season 10 Episodes (1996)
Total Episodes: 8
Final season of the original series
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 10
SEASON10_RECURRING_CAST = {
    "Lord Dregg": {"character_name": "Lord Dregg", "voice_actor": "Tony Jay", "role": "main_villain"},
    "Mung": {"character_name": "Mung", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Carter": {"character_name": "Carter", "voice_actor": "Michael Dorn", "role": "main"},
    "Shredder": {"character_name": "Shredder", "voice_actor": "Dorian Harewood", "role": "special_guest"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "special_guest"},
}

SEASON10_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 177,
        "title": "The Return of Dregg",
        "season": 10,
        "episode_number": 1,
        "air_date": "1996-09-14",
        "synopsis": "Lord Dregg returns from his defeat with enhanced powers and a new army of TechnoGangs to conquer Earth.",
        "cast": MAIN_CAST + [
            SEASON10_RECURRING_CAST["Lord Dregg"], 
            SEASON10_RECURRING_CAST["Mung"],
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "Jeffrey Scott",
        "director": "Tony Love",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Final season premiere"
    },
    {
        "episode_id": 178,
        "title": "The Beginning of the End",
        "season": 10,
        "episode_number": 2,
        "air_date": "1996-09-21",
        "synopsis": "Dregg's micro-bots begin infecting technology worldwide, turning machines against humanity.",
        "cast": MAIN_CAST + [
            SEASON10_RECURRING_CAST["Lord Dregg"], 
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "Jeffrey Scott",
        "director": "Tony Love",
        "villains_featured": ["Lord Dregg"],
        "notes": "Technology takeover"
    },
    {
        "episode_id": 179,
        "title": "The Power of Three",
        "season": 10,
        "episode_number": 3,
        "air_date": "1996-09-28",
        "synopsis": "Three alien bounty hunters arrive on Earth to capture the Turtles for Dregg's intergalactic zoo.",
        "cast": MAIN_CAST + [
            {"character_name": "Alien Bounty Hunters", "voice_actor": "Various", "role": "guest"},
            SEASON10_RECURRING_CAST["Lord Dregg"],
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Tony Love",
        "villains_featured": ["Alien Bounty Hunters", "Lord Dregg"],
        "notes": "Bounty hunter episode"
    },
    {
        "episode_id": 180,
        "title": "A Turtle in Time",
        "season": 10,
        "episode_number": 4,
        "air_date": "1996-10-05",
        "synopsis": "The Turtles are scattered through time by Dregg's temporal disruptor, each landing in a different era.",
        "cast": MAIN_CAST + [
            SEASON10_RECURRING_CAST["Lord Dregg"], 
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "Jeffrey Scott",
        "director": "Tony Love",
        "villains_featured": ["Lord Dregg"],
        "notes": "Time travel episode"
    },
    {
        "episode_id": 181,
        "title": "Turtles to the Second Power",
        "season": 10,
        "episode_number": 5,
        "air_date": "1996-10-12",
        "synopsis": "Dregg creates evil clones of the Turtles with all their skills but none of their morals.",
        "cast": MAIN_CAST + [
            SEASON10_RECURRING_CAST["Lord Dregg"], 
            SEASON10_RECURRING_CAST["Mung"],
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Tony Love",
        "villains_featured": ["Lord Dregg", "Mung", "Evil Turtle Clones"],
        "notes": "Evil clone episode"
    },
    {
        "episode_id": 182,
        "title": "Mobster from Dimension X",
        "season": 10,
        "episode_number": 6,
        "air_date": "1996-10-19",
        "synopsis": "A 1920s-style gangster from Dimension X arrives and tries to take over New York's underworld.",
        "cast": MAIN_CAST + [
            {"character_name": "Big Louie", "voice_actor": "Peter Renaday", "role": "guest"},
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "Jeffrey Scott",
        "director": "Tony Love",
        "villains_featured": ["Big Louie"],
        "notes": "Gangster episode"
    },
    {
        "episode_id": 183,
        "title": "The Day the Earth Disappeared",
        "season": 10,
        "episode_number": 7,
        "air_date": "1996-10-26",
        "synopsis": "Dregg begins transporting pieces of Earth to Dimension X to rebuild it as his personal empire.",
        "cast": MAIN_CAST + [
            SEASON10_RECURRING_CAST["Lord Dregg"], 
            SEASON10_RECURRING_CAST["Mung"],
            SEASON10_RECURRING_CAST["Carter"]
        ],
        "writer": "David Wise",
        "director": "Tony Love",
        "villains_featured": ["Lord Dregg", "Mung"],
        "notes": "Earth disappearing crisis"
    },
    {
        "episode_id": 184,
        "title": "Divide and Conquer",
        "season": 10,
        "episode_number": 8,
        "air_date": "1996-11-02",
        "synopsis": "In the series finale, Lord Dregg teams up with Shredder and Krang for one final assault. The Turtles must overcome their greatest challenge to save Earth once and for all.",
        "cast": MAIN_CAST + [
            SEASON10_RECURRING_CAST["Lord Dregg"], 
            SEASON10_RECURRING_CAST["Mung"],
            SEASON10_RECURRING_CAST["Carter"],
            SEASON10_RECURRING_CAST["Shredder"],
            SEASON10_RECURRING_CAST["Krang"],
            {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "special_guest"},
            {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "special_guest"}
        ],
        "writer": "Jeffrey Scott",
        "director": "Tony Love",
        "villains_featured": ["Lord Dregg", "Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Series finale - All villains return for final battle"
    }
]