"""
TMNT 1987 Series - Season 7 Episodes (1993)
Total Episodes: 27
European Vacation Tour & Channel 6 focused episodes
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 7
SEASON7_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Irma": {"character_name": "Irma Langinstein", "voice_actor": "Jennifer Darling", "role": "recurring"},
    "Vernon": {"character_name": "Vernon Fenwick", "voice_actor": "Peter Renaday", "role": "recurring"},
    "Burne Thompson": {"character_name": "Burne Thompson", "voice_actor": "Pat Fraley", "role": "recurring"},
}

SEASON7_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 134,
        "title": "Tower of Power",
        "season": 7,
        "episode_number": 1,
        "air_date": "1993-09-18",
        "synopsis": "The Turtles travel to Paris where Shredder plans to steal the Eiffel Tower with a shrinking ray.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Bebop"], 
            SEASON7_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Season 7 premiere - European vacation begins"
    },
    {
        "episode_id": 135,
        "title": "Rust Never Sleeps",
        "season": 7,
        "episode_number": 2,
        "air_date": "1993-09-25",
        "synopsis": "In Paris, Shredder unleashes metal-eating termites that threaten to destroy the city's infrastructure.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Paris adventure continues"
    },
    {
        "episode_id": 136,
        "title": "A Real Snow Job",
        "season": 7,
        "episode_number": 3,
        "air_date": "1993-10-02",
        "synopsis": "The Turtles travel to the Austrian Alps where Krang plans to use a weather device to create a new ice age.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Krang"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Austrian Alps adventure"
    },
    {
        "episode_id": 137,
        "title": "Venice on the Half Shell",
        "season": 7,
        "episode_number": 4,
        "air_date": "1993-10-09",
        "synopsis": "In Venice, Italy, Shredder attempts to steal priceless Renaissance art using robotic gondoliers.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Bebop"], 
            SEASON7_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Venice, Italy adventure"
    },
    {
        "episode_id": 138,
        "title": "Artless",
        "season": 7,
        "episode_number": 5,
        "air_date": "1993-10-16",
        "synopsis": "In Florence, two art thieves bring Renaissance statues to life to aid in their criminal activities.",
        "cast": MAIN_CAST + [
            {"character_name": "Art Thieves", "voice_actor": "Various", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Art Thieves"],
        "notes": "Florence art adventure"
    },
    {
        "episode_id": 139,
        "title": "Ring of Fire",
        "season": 7,
        "episode_number": 6,
        "air_date": "1993-10-23",
        "synopsis": "The Turtles visit Athens, Greece, where Shredder plans to use an ancient fire ring to control Mount Olympus.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Krang"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Greek mythology adventure"
    },
    {
        "episode_id": 140,
        "title": "The Irish Jig is Up",
        "season": 7,
        "episode_number": 7,
        "air_date": "1993-10-30",
        "synopsis": "In Dublin, Ireland, Shredder seeks to capture a leprechaun to steal his gold and magical powers.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Bebop"], 
            SEASON7_RECURRING_CAST["Rocksteady"],
            {"character_name": "Rainbow", "voice_actor": "Rob Paulsen", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Irish folklore adventure"
    },
    {
        "episode_id": 141,
        "title": "Shredder's New Sword",
        "season": 7,
        "episode_number": 8,
        "air_date": "1993-11-06",
        "synopsis": "In England, Shredder seeks Excalibur to gain ultimate power, but the sword has its own plans.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Arthurian legend adventure"
    },
    {
        "episode_id": 142,
        "title": "The Lost Queen of Atlantis",
        "season": 7,
        "episode_number": 9,
        "air_date": "1993-11-13",
        "synopsis": "The Turtles discover the lost city of Atlantis and must protect it from Shredder's exploitation.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Bebop"], 
            SEASON7_RECURRING_CAST["Rocksteady"],
            {"character_name": "Queen of Atlantis", "voice_actor": "B.J. Ward", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Atlantis adventure"
    },
    {
        "episode_id": 143,
        "title": "Turtles on the Orient Express",
        "season": 7,
        "episode_number": 10,
        "air_date": "1993-11-20",
        "synopsis": "Aboard the Orient Express, the Turtles must solve a mystery involving stolen diamonds and international spies.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"],
            {"character_name": "International Spies", "voice_actor": "Various", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "International Spies"],
        "notes": "Orient Express mystery"
    },
    {
        "episode_id": 144,
        "title": "April Gets in Dutch",
        "season": 7,
        "episode_number": 11,
        "air_date": "1993-11-27",
        "synopsis": "In Amsterdam, April is kidnapped by diamond thieves who mistake her for someone else.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Irma"],
            {"character_name": "Diamond Thieves", "voice_actor": "Various", "role": "guest"}
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Diamond Thieves"],
        "notes": "Amsterdam adventure"
    },
    {
        "episode_id": 145,
        "title": "Northern Lights Out",
        "season": 7,
        "episode_number": 12,
        "air_date": "1993-12-04",
        "synopsis": "In Norway, aliens attempt to steal Earth's magnetic field using the Aurora Borealis.",
        "cast": MAIN_CAST + [
            {"character_name": "Aurora Aliens", "voice_actor": "Various", "role": "guest"},
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Aurora Aliens", "Shredder"],
        "notes": "Scandinavian adventure"
    },
    {
        "episode_id": 146,
        "title": "Elementary, My Dear Turtle",
        "season": 7,
        "episode_number": 13,
        "air_date": "1993-12-11",
        "synopsis": "In London, the Turtles team up with a descendant of Sherlock Holmes to solve a mystery involving stolen crown jewels.",
        "cast": MAIN_CAST + [
            {"character_name": "Sherlock Holmes III", "voice_actor": "Townsend Coleman", "role": "guest"},
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Sherlock Holmes homage"
    },
    {
        "episode_id": 147,
        "title": "Night of the Dark Turtle",
        "season": 7,
        "episode_number": 14,
        "air_date": "1993-10-30",
        "synopsis": "Donatello becomes a dark vigilante after an accident, taking justice into his own hands.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Bebop"], 
            SEASON7_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Dark Knight parody"
    },
    {
        "episode_id": 148,
        "title": "The Starchild",
        "season": 7,
        "episode_number": 15,
        "air_date": "1993-11-06",
        "synopsis": "An alien child with incredible powers arrives on Earth, pursued by intergalactic hunters.",
        "cast": MAIN_CAST + [
            {"character_name": "Starchild", "voice_actor": "Cree Summer", "role": "guest"},
            {"character_name": "Alien Hunters", "voice_actor": "Various", "role": "guest"}
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Alien Hunters"],
        "notes": "Alien child protection episode"
    },
    {
        "episode_id": 149,
        "title": "The Legend of Koji",
        "season": 7,
        "episode_number": 16,
        "air_date": "1993-11-13",
        "synopsis": "An ancient Japanese spirit warrior is awakened and challenges the Turtles to prove their ninja worthiness.",
        "cast": MAIN_CAST + [
            {"character_name": "Koji", "voice_actor": "Robert Ito", "role": "guest"},
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Koji", "Shredder"],
        "notes": "Japanese mythology episode"
    },
    {
        "episode_id": 150,
        "title": "Convicts from Dimension X",
        "season": 7,
        "episode_number": 17,
        "air_date": "1993-11-20",
        "synopsis": "Two dangerous convicts escape from Dimension X prison and hide on Earth, causing chaos.",
        "cast": MAIN_CAST + [
            {"character_name": "Skarg", "voice_actor": "Michael Dorn", "role": "guest"},
            {"character_name": "Dementor", "voice_actor": "Jim Cummings", "role": "guest"},
            SEASON7_RECURRING_CAST["Krang"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Skarg", "Dementor", "Krang"],
        "notes": "Dimension X convicts episode"
    },
    {
        "episode_id": 151,
        "title": "White Belt, Black Heart",
        "season": 7,
        "episode_number": 18,
        "air_date": "1993-11-27",
        "synopsis": "A young martial arts student is corrupted by an evil sensei who plans to use him against the Turtles.",
        "cast": MAIN_CAST + [
            {"character_name": "Evil Sensei", "voice_actor": "Keone Young", "role": "guest"},
            {"character_name": "Young Student", "voice_actor": "Cam Clarke", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Evil Sensei"],
        "notes": "Martial arts morality tale"
    },
    {
        "episode_id": 152,
        "title": "Night of the Rogues",
        "season": 7,
        "episode_number": 19,
        "air_date": "1993-12-04",
        "synopsis": "Shredder assembles a team of the Turtles' past enemies for one final assault.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"},
            {"character_name": "Leatherhead", "voice_actor": "Jim Cummings", "role": "guest"},
            {"character_name": "Slash", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Tempestra", "voice_actor": "Tress MacNeille", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Rat King", "Leatherhead", "Slash", "Tempestra"],
        "notes": "Villain team-up episode"
    },
    {
        "episode_id": 153,
        "title": "Attack of the Neutrinos",
        "season": 7,
        "episode_number": 20,
        "air_date": "1993-12-11",
        "synopsis": "The Neutrinos return with news that Dimension X is collapsing and needs the Turtles' help.",
        "cast": MAIN_CAST + [
            {"character_name": "Kala", "voice_actor": "Tress MacNeille", "role": "guest"},
            {"character_name": "Dask", "voice_actor": "Rob Paulsen", "role": "guest"},
            {"character_name": "Zak", "voice_actor": "Pat Fraley", "role": "guest"},
            SEASON7_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Krang"],
        "notes": "Neutrinos return"
    },
    {
        "episode_id": 154,
        "title": "Escape from the Planet of the Turtleloids",
        "season": 7,
        "episode_number": 21,
        "air_date": "1993-12-18",
        "synopsis": "The Turtles travel to the Turtleloid homeworld to help defend it from invasion.",
        "cast": MAIN_CAST + [
            {"character_name": "Turtleloid", "voice_actor": "Rob Paulsen", "role": "guest"},
            {"character_name": "Chrome Dome", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Chrome Dome"],
        "notes": "Turtleloid planet adventure"
    },
    {
        "episode_id": 155,
        "title": "Revenge of the Fly",
        "season": 7,
        "episode_number": 22,
        "air_date": "1993-09-25",
        "synopsis": "Baxter Stockman returns with a new scheme to regain his human form by stealing life energy.",
        "cast": MAIN_CAST + [
            {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Baxter Stockman", "Shredder"],
        "notes": "Baxter Stockman returns"
    },
    {
        "episode_id": 156,
        "title": "Atlantis Awakes",
        "season": 7,
        "episode_number": 23,
        "air_date": "1993-10-02",
        "synopsis": "The lost city of Atlantis rises from the ocean, and its inhabitants declare war on the surface world.",
        "cast": MAIN_CAST + [
            {"character_name": "King Alim", "voice_actor": "Michael Bell", "role": "guest"},
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["King Alim", "Shredder"],
        "notes": "Atlantis rises"
    },
    {
        "episode_id": 157,
        "title": "Dirk Savage: Mutant Hunter",
        "season": 7,
        "episode_number": 24,
        "air_date": "1993-10-09",
        "synopsis": "A professional mutant hunter arrives in New York targeting the Turtles and all other mutants.",
        "cast": MAIN_CAST + [
            {"character_name": "Dirk Savage", "voice_actor": "Peter Cullen", "role": "guest"},
            {"character_name": "Napoleon Bonafrog", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Genghis Frog", "voice_actor": "Jim Cummings", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Dirk Savage"],
        "notes": "Mutant hunter antagonist"
    },
    {
        "episode_id": 158,
        "title": "Invasion of the Krangazoids",
        "season": 7,
        "episode_number": 25,
        "air_date": "1993-10-16",
        "synopsis": "Krang clones himself multiple times, creating an army of Krangs to conquer Earth.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Krang"], 
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Krang", "Krangazoids", "Shredder"],
        "notes": "Multiple Krangs episode"
    },
    {
        "episode_id": 159,
        "title": "Combat Land",
        "season": 7,
        "episode_number": 26,
        "air_date": "1993-10-23",
        "synopsis": "A mysterious amusement park appears overnight, but it's actually a trap designed to capture mutants.",
        "cast": MAIN_CAST + [
            {"character_name": "Combat Land Owner", "voice_actor": "Cam Clarke", "role": "guest"},
            SEASON7_RECURRING_CAST["Shredder"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Combat Land Owner", "Shredder"],
        "notes": "Deadly amusement park"
    },
    {
        "episode_id": 160,
        "title": "Shredder Triumphant",
        "season": 7,
        "episode_number": 27,
        "air_date": "1993-12-18",
        "synopsis": "Shredder and Krang finally succeed in bringing the Technodrome back to Earth for a climactic battle.",
        "cast": MAIN_CAST + [
            SEASON7_RECURRING_CAST["Shredder"], 
            SEASON7_RECURRING_CAST["Krang"], 
            SEASON7_RECURRING_CAST["Bebop"], 
            SEASON7_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Season 7 finale - Technodrome returns"
    }
]