"""
TMNT 1987 Series - Season 5 Episodes (1991)
Total Episodes: 13
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 5
SEASON5_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Rat King": {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"},
    "Casey Jones": {"character_name": "Casey Jones", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Irma": {"character_name": "Irma Langinstein", "voice_actor": "Jennifer Darling", "role": "recurring"},
    "Vernon": {"character_name": "Vernon Fenwick", "voice_actor": "Peter Renaday", "role": "recurring"},
}

SEASON5_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 105,
        "title": "The Turtles and the Hare",
        "season": 5,
        "episode_number": 1,
        "air_date": "1991-09-14",
        "synopsis": "The Turtles compete in a race across the city while dealing with Shredder's interference and a speedy mutant rabbit.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Bebop"], 
            SEASON5_RECURRING_CAST["Rocksteady"],
            {"character_name": "Hokum Hare", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Season 5 premiere - Racing episode"
    },
    {
        "episode_id": 106,
        "title": "Once Upon a Time Machine",
        "season": 5,
        "episode_number": 2,
        "air_date": "1991-09-21",
        "synopsis": "Hokum Hare uses a time machine to travel back and prevent the Turtles from being mutated, threatening their existence.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"],
            {"character_name": "Hokum Hare", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Hokum Hare", "Shredder", "Krang"],
        "notes": "Time travel paradox episode"
    },
    {
        "episode_id": 107,
        "title": "My Brother, the Bad Guy",
        "season": 5,
        "episode_number": 3,
        "air_date": "1991-09-28",
        "synopsis": "Shredder's brother Kazuo Saki arrives, claiming to be a reformed ninja who wants to stop his evil sibling.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"],
            {"character_name": "Kazuo Saki", "voice_actor": "Jim Cummings", "role": "guest"}
        ],
        "writer": "David Wise & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Introduction of Shredder's brother"
    },
    {
        "episode_id": 108,
        "title": "Michelangelo Meets Mondo Gecko",
        "season": 5,
        "episode_number": 4,
        "air_date": "1991-10-05",
        "synopsis": "Michelangelo befriends Mondo Gecko, a skateboarding mutant gecko who's being exploited by a criminal promoter.",
        "cast": MAIN_CAST + [
            {"character_name": "Mondo Gecko", "voice_actor": "John Mariano", "role": "guest"},
            {"character_name": "Mr. X", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Mr. X"],
        "notes": "Introduction of Mondo Gecko"
    },
    {
        "episode_id": 109,
        "title": "Enter: Mutagen Man",
        "season": 5,
        "episode_number": 5,
        "air_date": "1991-10-12",
        "synopsis": "A delivery man is transformed into Mutagen Man, a tragic villain made of living ooze who seeks revenge on the world.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"],
            {"character_name": "Mutagen Man", "voice_actor": "Rob Paulsen", "role": "guest"}
        ],
        "writer": "Jack Mendelsohn & David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Mutagen Man", "Shredder", "Krang"],
        "notes": "Introduction of Mutagen Man"
    },
    {
        "episode_id": 110,
        "title": "Donatello's Badd Time",
        "season": 5,
        "episode_number": 6,
        "air_date": "1991-10-19",
        "synopsis": "Donatello encounters the Dude, a time-traveling outlaw from the future who wants to change history.",
        "cast": MAIN_CAST + [
            {"character_name": "The Dude", "voice_actor": "Dan Gilvezan", "role": "guest"},
            SEASON5_RECURRING_CAST["Shredder"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["The Dude", "Shredder"],
        "notes": "Future time travel episode"
    },
    {
        "episode_id": 111,
        "title": "Muckman Messes Up",
        "season": 5,
        "episode_number": 7,
        "air_date": "1991-10-26",
        "synopsis": "Two garbage men are transformed into Muckman and Joe Eyeball, who initially blame the Turtles for their mutation.",
        "cast": MAIN_CAST + [
            {"character_name": "Muckman", "voice_actor": "Townsend Coleman", "role": "guest"},
            {"character_name": "Joe Eyeball", "voice_actor": "Rob Paulsen", "role": "guest"},
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Bebop"], 
            SEASON5_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Francis Moss & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Introduction of Muckman and Joe Eyeball"
    },
    {
        "episode_id": 112,
        "title": "Napoleon Bonafrog: Colossus of the Swamps",
        "season": 5,
        "episode_number": 8,
        "air_date": "1991-11-02",
        "synopsis": "Napoleon Bonafrog seeks the Turtles' help when Shredder threatens his swamp home with a new drilling operation.",
        "cast": MAIN_CAST + [
            {"character_name": "Napoleon Bonafrog", "voice_actor": "Pat Fraley", "role": "guest"},
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"]
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Napoleon Bonafrog returns"
    },
    {
        "episode_id": 113,
        "title": "Raphael Versus the Volcano",
        "season": 5,
        "episode_number": 9,
        "air_date": "1991-11-09",
        "synopsis": "A mysterious volcanic island appears near New York, and Raphael must overcome his fears to save his friends.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Bebop"], 
            SEASON5_RECURRING_CAST["Rocksteady"],
            {"character_name": "Professor Sopho", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Raphael character development"
    },
    {
        "episode_id": 114,
        "title": "Landlord of the Flies",
        "season": 5,
        "episode_number": 10,
        "air_date": "1991-11-16",
        "synopsis": "Baxter Stockman returns with an army of mutant insects and takes over the Turtles' neighborhood.",
        "cast": MAIN_CAST + [
            {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
            SEASON5_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Baxter Stockman", "Shredder"],
        "notes": "Baxter Stockman's return with insect army"
    },
    {
        "episode_id": 115,
        "title": "Donatello's Duplicate",
        "season": 5,
        "episode_number": 11,
        "air_date": "1991-11-23",
        "synopsis": "Donatello creates a clone of himself to help with his workload, but the duplicate develops its own agenda.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"]
        ],
        "writer": "Jack Mendelsohn & Carole Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Clone episode"
    },
    {
        "episode_id": 116,
        "title": "The Ice Creature Cometh",
        "season": 5,
        "episode_number": 12,
        "air_date": "1991-11-30",
        "synopsis": "Bebop and Rocksteady accidentally unleash an ancient ice creature that threatens to freeze the entire city.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"], 
            SEASON5_RECURRING_CAST["Bebop"], 
            SEASON5_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Ice Creature", "Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Ice monster episode"
    },
    {
        "episode_id": 117,
        "title": "Leonardo Cuts Loose",
        "season": 5,
        "episode_number": 13,
        "air_date": "1991-12-07",
        "synopsis": "Leonardo decides to quit being so serious and have fun, but his timing couldn't be worse as Shredder launches a major attack.",
        "cast": MAIN_CAST + [
            SEASON5_RECURRING_CAST["Shredder"], 
            SEASON5_RECURRING_CAST["Krang"], 
            SEASON5_RECURRING_CAST["Bebop"], 
            SEASON5_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Season 5 finale - Leonardo character episode"
    }
]