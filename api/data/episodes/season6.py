"""
TMNT 1987 Series - Season 6 Episodes (1992)
Total Episodes: 16
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 6
SEASON6_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Rat King": {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"},
    "Irma": {"character_name": "Irma Langinstein", "voice_actor": "Jennifer Darling", "role": "recurring"},
    "Vernon": {"character_name": "Vernon Fenwick", "voice_actor": "Peter Renaday", "role": "recurring"},
}

SEASON6_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 118,
        "title": "Rock Around the Block",
        "season": 6,
        "episode_number": 1,
        "air_date": "1992-09-12",
        "synopsis": "Krang summons General Traag from Dimension X to help with a new scheme involving a powerful energy device.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Krang"],
            {"character_name": "General Traag", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "General Traag"],
        "notes": "Season 6 premiere"
    },
    {
        "episode_id": 119,
        "title": "Krangenstein Lives",
        "season": 6,
        "episode_number": 2,
        "air_date": "1992-09-19",
        "synopsis": "Krang creates a giant robotic body for himself, becoming Krangenstein and terrorizing the city.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Krang", "Shredder"],
        "notes": "Frankenstein parody"
    },
    {
        "episode_id": 120,
        "title": "Super Irma",
        "season": 6,
        "episode_number": 3,
        "air_date": "1992-09-26",
        "synopsis": "Irma gains superpowers from a strange meteorite and decides to become a superhero.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Irma"], 
            SEASON6_RECURRING_CAST["Vernon"],
            SEASON6_RECURRING_CAST["Shredder"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Irma-focused episode"
    },
    {
        "episode_id": 121,
        "title": "Adventures in Turtle Sitting",
        "season": 6,
        "episode_number": 4,
        "air_date": "1992-10-03",
        "synopsis": "The Turtles are transformed into babies and must be cared for by April while finding a cure.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Bebop"], 
            SEASON6_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Baby Turtles episode"
    },
    {
        "episode_id": 122,
        "title": "The Sword of Yurikawa",
        "season": 6,
        "episode_number": 5,
        "air_date": "1992-10-10",
        "synopsis": "An ancient ninja sword with mystical powers surfaces, and both the Turtles and Shredder seek to claim it.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Mystical sword episode"
    },
    {
        "episode_id": 123,
        "title": "Return of the Turtleoid",
        "season": 6,
        "episode_number": 6,
        "air_date": "1992-10-17",
        "synopsis": "The Turtleoid returns from space needing help to save his planet from invasion.",
        "cast": MAIN_CAST + [
            {"character_name": "Turtleoid", "voice_actor": "Rob Paulsen", "role": "guest"},
            SEASON6_RECURRING_CAST["Shredder"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Return of alien turtle character"
    },
    {
        "episode_id": 124,
        "title": "Shreeka's Revenge",
        "season": 6,
        "episode_number": 7,
        "air_date": "1992-10-24",
        "synopsis": "An alien queen named Shreeka comes to Earth seeking revenge on the Turtles for foiling her plans.",
        "cast": MAIN_CAST + [
            {"character_name": "Shreeka", "voice_actor": "Pat Musick", "role": "guest"},
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shreeka", "Shredder", "Krang"],
        "notes": "Alien queen antagonist"
    },
    {
        "episode_id": 125,
        "title": "Too Hot to Handle",
        "season": 6,
        "episode_number": 8,
        "air_date": "1992-10-31",
        "synopsis": "A heat wave hits New York, and Vernon discovers it's caused by aliens planning to make Earth their new tropical home.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Vernon"], 
            SEASON6_RECURRING_CAST["Shredder"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Aliens", "Shredder"],
        "notes": "Environmental threat episode"
    },
    {
        "episode_id": 126,
        "title": "Nightmare in the Lair",
        "season": 6,
        "episode_number": 9,
        "air_date": "1992-11-07",
        "synopsis": "Donatello's new dream-recording machine malfunctions, bringing the Turtles' nightmares to life.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Nightmare creatures", "Shredder", "Krang"],
        "notes": "Halloween-themed episode"
    },
    {
        "episode_id": 127,
        "title": "Phantom of the Sewers",
        "season": 6,
        "episode_number": 10,
        "air_date": "1992-11-14",
        "synopsis": "A mysterious phantom haunts the sewers, and the Turtles investigate to uncover the truth.",
        "cast": MAIN_CAST + [
            {"character_name": "The Phantom", "voice_actor": "Townsend Coleman", "role": "guest"},
            SEASON6_RECURRING_CAST["Shredder"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["The Phantom", "Shredder"],
        "notes": "Phantom of the Opera parody"
    },
    {
        "episode_id": 128,
        "title": "Donatello Trashes Slash",
        "season": 6,
        "episode_number": 11,
        "air_date": "1992-11-21",
        "synopsis": "Slash returns more dangerous than ever, forcing Donatello to confront him alone.",
        "cast": MAIN_CAST + [
            {"character_name": "Slash", "voice_actor": "Pat Fraley", "role": "guest"},
            SEASON6_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Slash", "Shredder"],
        "notes": "Return of Slash"
    },
    {
        "episode_id": 129,
        "title": "Leonardo is Missing",
        "season": 6,
        "episode_number": 12,
        "air_date": "1992-11-28",
        "synopsis": "Leonardo disappears during a mission, and his brothers must find him before Shredder does.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Bebop"], 
            SEASON6_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Leonardo disappearance mystery"
    },
    {
        "episode_id": 130,
        "title": "Polly Wanna Pizza",
        "season": 6,
        "episode_number": 13,
        "air_date": "1992-12-05",
        "synopsis": "Michelangelo's pet parrot gains human intelligence and decides to take over the city.",
        "cast": MAIN_CAST + [
            {"character_name": "Polly", "voice_actor": "Rob Paulsen", "role": "guest"},
            SEASON6_RECURRING_CAST["Shredder"]
        ],
        "writer": "Francis Moss & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Polly", "Shredder"],
        "notes": "Intelligent parrot antagonist"
    },
    {
        "episode_id": 131,
        "title": "Mr. Nice Guy",
        "season": 6,
        "episode_number": 14,
        "air_date": "1992-12-12",
        "synopsis": "Donatello's personality-altering device accidentally makes everyone in the city extremely nice, including the villains.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Krang"], 
            SEASON6_RECURRING_CAST["Bebop"], 
            SEASON6_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Personality alteration episode"
    },
    {
        "episode_id": 132,
        "title": "Sleuth on the Loose",
        "season": 6,
        "episode_number": 15,
        "air_date": "1992-12-19",
        "synopsis": "April becomes a detective to solve a series of mysterious robberies, uncovering a plot by Shredder.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Shredder"], 
            SEASON6_RECURRING_CAST["Bebop"], 
            SEASON6_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "April detective episode"
    },
    {
        "episode_id": 133,
        "title": "Snakes Alive!",
        "season": 6,
        "episode_number": 16,
        "air_date": "1992-12-26",
        "synopsis": "The Rat King teams up with a snake charmer to take over the city using an army of serpents.",
        "cast": MAIN_CAST + [
            SEASON6_RECURRING_CAST["Rat King"],
            {"character_name": "Snake Charmer", "voice_actor": "Jim Cummings", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Rat King", "Snake Charmer"],
        "notes": "Season 6 finale - Rat King team-up"
    }
]