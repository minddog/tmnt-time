"""
TMNT 1987 Series - Season 2 Episodes (1988)
Total Episodes: 13
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 2
SEASON2_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Baxter Stockman": {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Irma": {"character_name": "Irma Langinstein", "voice_actor": "Jennifer Darling", "role": "recurring"},
    "Vernon": {"character_name": "Vernon Fenwick", "voice_actor": "Peter Renaday", "role": "recurring"},
}

SEASON2_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 6,
        "title": "Return of the Shredder",
        "season": 2,
        "episode_number": 1,
        "air_date": "1988-10-01",
        "synopsis": "Shredder returns with a new plan involving fake turtle costumes to frame the heroes. The Turtles must clear their names while stopping Shredder's scheme.",
        "cast": MAIN_CAST + [SEASON2_RECURRING_CAST["Shredder"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Season 2 premiere"
    },
    {
        "episode_id": 7,
        "title": "The Incredible Shrinking Turtles",
        "season": 2,
        "episode_number": 2,
        "air_date": "1988-10-08",
        "synopsis": "The Turtles are shrunk by alien technology and must navigate the dangers of being miniaturized while stopping Shredder's latest plot.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Baxter Stockman"]
        ],
        "writer": "Larry Parr",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Baxter Stockman"],
        "notes": "Features miniaturized action sequences"
    },
    {
        "episode_id": 8,
        "title": "It Came from Beneath the Sewers",
        "season": 2,
        "episode_number": 3,
        "air_date": "1988-10-15",
        "synopsis": "A giant plant creature threatens the city after being mutated by toxic waste. The Turtles must stop it before it destroys New York.",
        "cast": MAIN_CAST + [SEASON2_RECURRING_CAST["Shredder"]],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Environmental theme episode"
    },
    {
        "episode_id": 9,
        "title": "The Mean Machines",
        "season": 2,
        "episode_number": 4,
        "air_date": "1988-10-22",
        "synopsis": "Shredder creates robot duplicates of vehicles that wreak havoc across the city. The Turtles must destroy these mechanical menaces.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Bebop"], 
            SEASON2_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Features sentient vehicle antagonists"
    },
    {
        "episode_id": 10,
        "title": "Curse of the Evil Eye",
        "season": 2,
        "episode_number": 5,
        "air_date": "1988-10-29",
        "synopsis": "Shredder seeks an ancient helmet with mystical powers. The Turtles race to prevent him from obtaining this dangerous artifact.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Baxter Stockman"]
        ],
        "writer": "Reed Shelly & Bruce Shelly",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Baxter Stockman"],
        "notes": "Mystical artifact episode"
    },
    {
        "episode_id": 11,
        "title": "Case of the Killer Pizzas",
        "season": 2,
        "episode_number": 6,
        "air_date": "1988-11-05",
        "synopsis": "Meatballs from Dimension X transform into dangerous creatures when exposed to Earth's atmosphere. The Turtles must stop the invasion.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Krang"]
        ],
        "writer": "Douglas Booth",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Pizza-themed alien invasion"
    },
    {
        "episode_id": 12,
        "title": "Enter: The Fly",
        "season": 2,
        "episode_number": 7,
        "air_date": "1988-11-12",
        "synopsis": "Baxter Stockman is transformed into a mutant fly after a transporter accident. He seeks revenge on both Shredder and the Turtles.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Baxter Stockman"],
            SEASON2_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Baxter Stockman", "Krang"],
        "notes": "Major character transformation - Baxter becomes mutant fly"
    },
    {
        "episode_id": 13,
        "title": "Invasion of the Punk Frogs",
        "season": 2,
        "episode_number": 8,
        "air_date": "1988-11-19",
        "synopsis": "Shredder creates mutant frogs to fight the Turtles, but the amphibians have their own ideas about good and evil.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"],
            {"character_name": "Napoleon Bonafrog", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Genghis Frog", "voice_actor": "Jim Cummings", "role": "guest"},
            {"character_name": "Attila the Frog", "voice_actor": "Cam Clarke", "role": "guest"},
            {"character_name": "Rasputin the Mad Frog", "voice_actor": "Rob Paulsen", "role": "guest"}
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Introduction of the Punk Frogs"
    },
    {
        "episode_id": 14,
        "title": "Splinter No More",
        "season": 2,
        "episode_number": 9,
        "air_date": "1988-11-26",
        "synopsis": "Donatello creates a formula to turn Splinter human again, but the transformation has unexpected consequences.",
        "cast": MAIN_CAST + [SEASON2_RECURRING_CAST["Shredder"]],
        "writer": "Larry Parr",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Splinter transformation episode"
    },
    {
        "episode_id": 15,
        "title": "New York's Shiniest",
        "season": 2,
        "episode_number": 10,
        "air_date": "1988-12-03",
        "synopsis": "Robot police officers frame the Turtles for crimes they didn't commit. The heroes must clear their names and stop the real criminals.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Bebop"], 
            SEASON2_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Robot police antagonists"
    },
    {
        "episode_id": 16,
        "title": "Teenagers from Dimension X",
        "season": 2,
        "episode_number": 11,
        "air_date": "1988-12-10",
        "synopsis": "The Neutrinos return and need the Turtles' help to save their dimension from Krang's tyranny.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Krang"],
            {"character_name": "Kala", "voice_actor": "Tress MacNeille", "role": "guest"},
            {"character_name": "Dask", "voice_actor": "Rob Paulsen", "role": "guest"},
            {"character_name": "Zak", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Return of the Neutrinos"
    },
    {
        "episode_id": 17,
        "title": "The Cat Woman from Channel Six",
        "season": 2,
        "episode_number": 12,
        "air_date": "1988-12-17",
        "synopsis": "April is mutated into a cat woman and struggles with her new feline instincts while the Turtles search for a cure.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Irma"], 
            SEASON2_RECURRING_CAST["Vernon"]
        ],
        "writer": "Richard Merwin",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "April transformation episode"
    },
    {
        "episode_id": 18,
        "title": "Return of the Technodrome",
        "season": 2,
        "episode_number": 13,
        "air_date": "1988-12-24",
        "synopsis": "The Technodrome resurfaces with upgraded weapons and Shredder launches his most ambitious attack on New York City yet.",
        "cast": MAIN_CAST + [
            SEASON2_RECURRING_CAST["Shredder"], 
            SEASON2_RECURRING_CAST["Krang"], 
            SEASON2_RECURRING_CAST["Bebop"], 
            SEASON2_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Season 2 finale featuring upgraded Technodrome"
    }
]