"""
TMNT 1987 Series - Season 1 Episodes (1987)
Total Episodes: 5
"""

from typing import List, Dict, Any

# Main cast members (appear in most episodes)
MAIN_CAST = [
    {"character_name": "Leonardo", "voice_actor": "Cam Clarke", "role": "main"},
    {"character_name": "Donatello", "voice_actor": "Barry Gordon", "role": "main"},
    {"character_name": "Raphael", "voice_actor": "Rob Paulsen", "role": "main"},
    {"character_name": "Michelangelo", "voice_actor": "Townsend Coleman", "role": "main"},
    {"character_name": "Master Splinter", "voice_actor": "Peter Renaday", "role": "main"},
    {"character_name": "April O'Neil", "voice_actor": "Renae Jacobs", "role": "main"},
]

# Recurring cast for Season 1
SEASON1_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Baxter Stockman": {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
}

SEASON1_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 1,
        "title": "Turtle Tracks", 
        "season": 1,
        "episode_number": 1,
        "air_date": "1987-12-14",
        "synopsis": "The Turtles make their first appearance and battle the Foot Clan for the first time. April O'Neil investigates the mysterious thefts plaguing New York City.",
        "cast": MAIN_CAST + [
            SEASON1_RECURRING_CAST["Shredder"], 
            SEASON1_RECURRING_CAST["Bebop"], 
            SEASON1_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Series premiere introducing the Turtles and their origin story"
    },
    {
        "episode_id": 2,
        "title": "Enter: The Shredder",
        "season": 1,
        "episode_number": 2,
        "air_date": "1987-12-15",
        "synopsis": "The Turtles face off against Shredder for the first time and learn about their connection to him through Master Splinter. Krang makes his debut appearance.",
        "cast": MAIN_CAST + [
            SEASON1_RECURRING_CAST["Shredder"], 
            SEASON1_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "First appearance of Krang and revelation of Splinter's backstory"
    },
    {
        "episode_id": 3,
        "title": "A Better Mousetrap",
        "season": 1,
        "episode_number": 3,
        "air_date": "1987-12-16",
        "synopsis": "Baxter Stockman unleashes his Mousers on the city, threatening to destroy the Turtles' lair. April gets her first real story covering the mechanical menace.",
        "cast": MAIN_CAST + [
            SEASON1_RECURRING_CAST["Shredder"], 
            SEASON1_RECURRING_CAST["Baxter Stockman"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Baxter Stockman", "Shredder"],
        "notes": "Introduction of Baxter Stockman and his Mouser robots"
    },
    {
        "episode_id": 4,
        "title": "Hot Rodding Teenagers from Dimension X",
        "season": 1,
        "episode_number": 4,
        "air_date": "1987-12-17",
        "synopsis": "The Neutrinos arrive from Dimension X, pursued by Stone Warriors. The Turtles must help their new friends while preventing Shredder from obtaining powerful technology.",
        "cast": MAIN_CAST + [
            SEASON1_RECURRING_CAST["Shredder"], 
            SEASON1_RECURRING_CAST["Krang"],
            {"character_name": "Kala", "voice_actor": "Tress MacNeille", "role": "guest"},
            {"character_name": "Dask", "voice_actor": "Rob Paulsen", "role": "guest"},
            {"character_name": "Zak", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "First appearance of the Neutrinos and Stone Warriors"
    },
    {
        "episode_id": 5,
        "title": "Shredder & Splintered",
        "season": 1,
        "episode_number": 5,
        "air_date": "1987-12-18",
        "synopsis": "Krang gives Shredder an ultimatum to destroy the Turtles. The Technodrome is completed and the Turtles must stop Shredder's plan to bring it to Earth's surface.",
        "cast": MAIN_CAST + [
            SEASON1_RECURRING_CAST["Shredder"], 
            SEASON1_RECURRING_CAST["Krang"],
            SEASON1_RECURRING_CAST["Bebop"],
            SEASON1_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Season 1 finale. First appearance of the completed Technodrome"
    }
]