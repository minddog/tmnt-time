"""
TMNT 1987 Series - Season 3 Episodes (1989)
Total Episodes: 47
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 3
SEASON3_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Baxter Stockman": {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Rat King": {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"},
    "Leatherhead": {"character_name": "Leatherhead", "voice_actor": "Jim Cummings", "role": "guest"},
    "Casey Jones": {"character_name": "Casey Jones", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Irma": {"character_name": "Irma Langinstein", "voice_actor": "Jennifer Darling", "role": "recurring"},
    "Vernon": {"character_name": "Vernon Fenwick", "voice_actor": "Peter Renaday", "role": "recurring"},
    "Burne Thompson": {"character_name": "Burne Thompson", "voice_actor": "Pat Fraley", "role": "recurring"},
}

SEASON3_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 19,
        "title": "Beneath These Streets",
        "season": 3,
        "episode_number": 1,
        "air_date": "1989-09-25",
        "synopsis": "The Turtles explore abandoned subway tunnels and discover a lost underground civilization while Shredder searches for a powerful energy source.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Season 3 premiere"
    },
    {
        "episode_id": 20,
        "title": "Turtles on Trial",
        "season": 3,
        "episode_number": 2,
        "air_date": "1989-09-26",
        "synopsis": "The Turtles are put on trial by the city of New York after being framed for a series of crimes. They must prove their innocence in court.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Vernon"]],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": [],
        "notes": "Courtroom drama episode"
    },
    {
        "episode_id": 21,
        "title": "Attack of the 50-Foot Irma",
        "season": 3,
        "episode_number": 3,
        "air_date": "1989-09-27",
        "synopsis": "Irma is enlarged to gigantic proportions by one of Krang's devices, causing chaos in the city as she tries to adjust to her new size.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"], 
            SEASON3_RECURRING_CAST["Irma"]
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Giant monster homage episode"
    },
    {
        "episode_id": 22,
        "title": "The Maltese Hamster",
        "season": 3,
        "episode_number": 4,
        "air_date": "1989-09-28",
        "synopsis": "Shredder steals a statue containing a secret formula for creating super-mutants. The Turtles must recover it before he decodes the formula.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Film noir parody episode"
    },
    {
        "episode_id": 23,
        "title": "Sky Turtles",
        "season": 3,
        "episode_number": 5,
        "air_date": "1989-09-29",
        "synopsis": "The Turtles gain the ability to fly using anti-gravity devices, but Krang plans to use the technology to lift entire cities into space.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Flying Turtles episode"
    },
    {
        "episode_id": 24,
        "title": "The Old Switcheroo",
        "season": 3,
        "episode_number": 6,
        "air_date": "1989-10-02",
        "synopsis": "Shredder and Splinter switch bodies due to a personality transference device malfunction. Chaos ensues as they try to adapt to their new forms.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Body swap episode"
    },
    {
        "episode_id": 25,
        "title": "Burne's Blues",
        "season": 3,
        "episode_number": 7,
        "air_date": "1989-10-03",
        "synopsis": "Burne Thompson becomes a vigilante crime fighter after being frustrated with the Turtles' methods, but his inexperience causes more problems.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Burne Thompson"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Burne Thompson focus episode"
    },
    {
        "episode_id": 26,
        "title": "The Fifth Turtle",
        "season": 3,
        "episode_number": 8,
        "air_date": "1989-10-04",
        "synopsis": "A wannabe turtle named Zach tries to join the team but his eagerness to help often makes situations worse.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"],
            {"character_name": "Zach", "voice_actor": "Rob Paulsen", "role": "guest"}
        ],
        "writer": "Francis Moss",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Introduction of Zach character"
    },
    {
        "episode_id": 27,
        "title": "Enter the Rat King",
        "season": 3,
        "episode_number": 9,
        "air_date": "1989-10-05",
        "synopsis": "The Rat King makes his first appearance, controlling armies of rats to take over the city. The Turtles must stop his rodent revolution.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Rat King"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Rat King"],
        "notes": "First appearance of the Rat King"
    },
    {
        "episode_id": 28,
        "title": "Turtles at the Earth's Core",
        "season": 3,
        "episode_number": 10,
        "air_date": "1989-10-06",
        "synopsis": "The Turtles travel to the center of the Earth where they discover dinosaurs and must prevent Shredder from enslaving them.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Journey to the Center of the Earth homage"
    },
    {
        "episode_id": 29,
        "title": "April's Fool",
        "season": 3,
        "episode_number": 11,
        "air_date": "1989-10-09",
        "synopsis": "April is kidnapped by aliens who mistake her for an Earth princess. The Turtles must rescue her from an intergalactic marriage.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "April-focused episode"
    },
    {
        "episode_id": 30,
        "title": "Attack of Big MACC",
        "season": 3,
        "episode_number": 12,
        "air_date": "1989-10-10",
        "synopsis": "A military robot named MACC goes haywire and befriends the Turtles, but Shredder wants to reprogram it for evil purposes.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"],
            {"character_name": "MACC", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Sentient robot character episode"
    },
    {
        "episode_id": 31,
        "title": "The Ninja Sword of Nowhere",
        "season": 3,
        "episode_number": 13,
        "air_date": "1989-10-11",
        "synopsis": "An alien sword causes havoc by switching people between dimensions. The Turtles must find a way to return everyone home.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Dimensional travel episode"
    },
    {
        "episode_id": 32,
        "title": "20,000 Leaks Under the City",
        "season": 3,
        "episode_number": 14,
        "air_date": "1989-10-12",
        "synopsis": "Krang floods the city as part of a plan to turn New York into an underwater base for the Technodrome.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Underwater adventure episode"
    },
    {
        "episode_id": 33,
        "title": "Take Me to Your Leader",
        "season": 3,
        "episode_number": 15,
        "air_date": "1989-10-13",
        "synopsis": "Aliens mistake Leonardo for Earth's leader and take him to negotiate a peace treaty, leaving his brothers to rescue him.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Leonardo-focused episode"
    },
    {
        "episode_id": 34,
        "title": "Four Musketurtles",
        "season": 3,
        "episode_number": 16,
        "air_date": "1989-10-16",
        "synopsis": "The Turtles travel back to medieval times and must help a young Arthur become king while preventing Shredder from changing history.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Time travel to medieval period"
    },
    {
        "episode_id": 35,
        "title": "Turtles, Turtles Everywhere",
        "season": 3,
        "episode_number": 17,
        "air_date": "1989-10-17",
        "synopsis": "Multiple dimensions collide, bringing different versions of the Turtles together to stop a multiversal threat.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Multiverse episode"
    },
    {
        "episode_id": 36,
        "title": "Cowabunga Shredhead",
        "season": 3,
        "episode_number": 18,
        "air_date": "1989-10-18",
        "synopsis": "Shredder and Michelangelo switch personalities, leading to a fun-loving Shredder and a serious Michelangelo.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Francis Moss",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Personality swap episode"
    },
    {
        "episode_id": 37,
        "title": "Invasion of the Turtle Snatchers",
        "season": 3,
        "episode_number": 19,
        "air_date": "1989-10-19",
        "synopsis": "Aliens kidnap the Turtles to add to their intergalactic zoo. The heroes must escape and return to Earth.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "Francis Moss",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Alien abduction episode"
    },
    {
        "episode_id": 38,
        "title": "Camera Bugged",
        "season": 3,
        "episode_number": 20,
        "air_date": "1989-10-20",
        "synopsis": "An alien takes over April's camera equipment, using it to spy on Earth and prepare for an invasion.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Technology possession episode"
    },
    {
        "episode_id": 39,
        "title": "Green with Jealousy",
        "season": 3,
        "episode_number": 21,
        "air_date": "1989-10-23",
        "synopsis": "Donatello and Baxter Stockman compete to prove who is the superior inventor, leading to dangerous consequences.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"], 
            SEASON3_RECURRING_CAST["Baxter Stockman"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Baxter Stockman"],
        "notes": "Donatello vs Baxter rivalry"
    },
    {
        "episode_id": 40,
        "title": "Return of the Fly",
        "season": 3,
        "episode_number": 22,
        "air_date": "1989-10-24",
        "synopsis": "Baxter Stockman returns with new powers and a plan for revenge against both Shredder and the Turtles.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Baxter Stockman"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Baxter Stockman"],
        "notes": "Baxter Stockman revenge episode"
    },
    {
        "episode_id": 41,
        "title": "Casey Jones - Outlaw Hero",
        "season": 3,
        "episode_number": 23,
        "air_date": "1989-10-25",
        "synopsis": "Casey Jones makes his animated debut as a vigilante who clashes with both criminals and the Turtles' methods.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Casey Jones"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "First appearance of Casey Jones"
    },
    {
        "episode_id": 42,
        "title": "Mutagen Monster",
        "season": 3,
        "episode_number": 24,
        "air_date": "1989-10-26",
        "synopsis": "A mutagen creature formed from toxic waste threatens the city, absorbing everything in its path.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Shredder"]],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Monster of the week episode"
    },
    {
        "episode_id": 43,
        "title": "Corporate Raiders from Dimension X",
        "season": 3,
        "episode_number": 25,
        "air_date": "1989-10-27",
        "synopsis": "Business-minded aliens attempt a hostile takeover of Earth, treating the planet like a corporate acquisition.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Casey Jones"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": [],
        "notes": "Corporate satire episode"
    },
    {
        "episode_id": 44,
        "title": "Pizza by the Shred",
        "season": 3,
        "episode_number": 26,
        "air_date": "1989-10-30",
        "synopsis": "Shredder opens a pizza parlor as a front for his latest scheme to eliminate the Turtles using their favorite food.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Pizza-themed villain plot"
    },
    {
        "episode_id": 45,
        "title": "Super Bebop & Mighty Rocksteady",
        "season": 3,
        "episode_number": 27,
        "air_date": "1989-10-31",
        "synopsis": "Bebop and Rocksteady gain superpowers and become more dangerous than ever, forcing the Turtles to find their weakness.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Powered-up henchmen episode"
    },
    {
        "episode_id": 46,
        "title": "Beware the Lotus",
        "season": 3,
        "episode_number": 28,
        "air_date": "1989-11-01",
        "synopsis": "A mysterious female ninja named Lotus Blossom arrives in New York, catching Leonardo's attention and Shredder's interest.",
        "cast": MAIN_CAST + [
            {"character_name": "Lotus Blossom", "voice_actor": "Renae Jacobs", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": [],
        "notes": "Introduction of Lotus Blossom"
    },
    {
        "episode_id": 47,
        "title": "Blast from the Past",
        "season": 3,
        "episode_number": 29,
        "air_date": "1989-11-02",
        "synopsis": "The Turtles travel to prehistoric times and must survive among dinosaurs while preventing Shredder from altering evolution.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Prehistoric time travel episode"
    },
    {
        "episode_id": 48,
        "title": "Leatherhead: Terror of the Swamp",
        "season": 3,
        "episode_number": 30,
        "air_date": "1989-11-03",
        "synopsis": "The Turtles encounter Leatherhead, a mutant alligator living in the Florida Everglades who has been tricked by Shredder.",
        "cast": MAIN_CAST + [SEASON3_RECURRING_CAST["Leatherhead"]],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Leatherhead"],
        "notes": "First appearance of Leatherhead"
    },
    {
        "episode_id": 49,
        "title": "Michelangelo's Birthday",
        "season": 3,
        "episode_number": 31,
        "air_date": "1989-11-06",
        "synopsis": "The Turtles celebrate Michelangelo's birthday, but Shredder plans to crash the party with a deadly surprise.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Ted Pedersen & Francis Moss",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Birthday celebration episode"
    },
    {
        "episode_id": 50,
        "title": "Usagi Yojimbo",
        "season": 3,
        "episode_number": 32,
        "air_date": "1989-11-07",
        "synopsis": "The Turtles meet the samurai rabbit Usagi Yojimbo when a dimensional portal brings him to their world.",
        "cast": MAIN_CAST + [
            {"character_name": "Usagi Yojimbo", "voice_actor": "Townsend Coleman", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": [],
        "notes": "Crossover with Stan Sakai's Usagi Yojimbo"
    },
    {
        "episode_id": 51,
        "title": "Case of the Hot Kimono",
        "season": 3,
        "episode_number": 33,
        "air_date": "1989-11-08",
        "synopsis": "A mystical kimono causes trouble when it possesses April, giving her incredible martial arts abilities but evil intentions.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Mystical possession episode"
    },
    {
        "episode_id": 52,
        "title": "Usagi Come Home",
        "season": 3,
        "episode_number": 34,
        "air_date": "1989-11-09",
        "synopsis": "Usagi returns and needs the Turtles' help to save his dimension from an evil shogun working with Shredder.",
        "cast": MAIN_CAST + [
            {"character_name": "Usagi Yojimbo", "voice_actor": "Townsend Coleman", "role": "guest"}, 
            SEASON3_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Second Usagi Yojimbo appearance"
    },
    {
        "episode_id": 53,
        "title": "The Making of Metalhead",
        "season": 3,
        "episode_number": 35,
        "air_date": "1989-11-10",
        "synopsis": "Krang creates a robot turtle called Metalhead to infiltrate and destroy the team from within.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"],
            {"character_name": "Metalhead", "voice_actor": "James Avery", "role": "guest"}
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Introduction of Metalhead"
    },
    {
        "episode_id": 54,
        "title": "Leatherhead Meets the Rat King",
        "season": 3,
        "episode_number": 36,
        "air_date": "1989-11-13",
        "synopsis": "Two villains team up as Leatherhead and the Rat King join forces to take revenge on the Turtles.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Leatherhead"], 
            SEASON3_RECURRING_CAST["Rat King"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Leatherhead", "Rat King"],
        "notes": "Villain team-up episode"
    },
    {
        "episode_id": 55,
        "title": "The Turtle Terminator",
        "season": 3,
        "episode_number": 37,
        "air_date": "1989-11-14",
        "synopsis": "Shredder creates an unstoppable turtle-hunting robot called the Turtle Terminator, programmed to destroy the heroes.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"], 
            SEASON3_RECURRING_CAST["Irma"]
        ],
        "writer": "Jack Mendelsohn & David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Terminator homage episode"
    },
    {
        "episode_id": 56,
        "title": "The Great Boldini",
        "season": 3,
        "episode_number": 38,
        "air_date": "1989-11-15",
        "synopsis": "A ghost magician named Boldini haunts the city, and the Turtles must solve the mystery of his return.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"],
            {"character_name": "The Great Boldini", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Supernatural mystery episode"
    },
    {
        "episode_id": 57,
        "title": "The Missing Map",
        "season": 3,
        "episode_number": 39,
        "air_date": "1989-11-16",
        "synopsis": "Shredder seeks a treasure map that leads to an ancient weapon, racing against the Turtles to find it first.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Treasure hunt episode"
    },
    {
        "episode_id": 58,
        "title": "The Gang's All Here",
        "season": 3,
        "episode_number": 40,
        "air_date": "1989-11-17",
        "synopsis": "The Turtles face multiple villains when Shredder organizes a villain team-up to finally defeat them.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"], 
            SEASON3_RECURRING_CAST["Baxter Stockman"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady", "Baxter Stockman"],
        "notes": "Multiple villain team-up"
    },
    {
        "episode_id": 59,
        "title": "The Grybyx",
        "season": 3,
        "episode_number": 41,
        "air_date": "1989-11-20",
        "synopsis": "A creature from Dimension X called the Grybyx arrives on Earth, and only kindness can stop its rampage.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Gentle giant episode"
    },
    {
        "episode_id": 60,
        "title": "Mister Ogg Goes to Town",
        "season": 3,
        "episode_number": 42,
        "air_date": "1989-11-21",
        "synopsis": "An alien named Mr. Ogg comes to Earth seeking employment, but his good intentions cause chaos.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"],
            {"character_name": "Mr. Ogg", "voice_actor": "Rob Paulsen", "role": "guest"}
        ],
        "writer": "Francis Moss & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Comedy-focused episode"
    },
    {
        "episode_id": 61,
        "title": "Shredderville",
        "season": 3,
        "episode_number": 43,
        "air_date": "1989-11-22",
        "synopsis": "The Turtles enter an alternate dimension where Shredder rules and they were never mutated, showing a dark timeline.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Francis Moss & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Alternate dimension/It's a Wonderful Life homage"
    },
    {
        "episode_id": 62,
        "title": "Bye, Bye, Fly",
        "season": 3,
        "episode_number": 44,
        "air_date": "1989-11-24",
        "synopsis": "Baxter Stockman seeks a way to become human again, but his attempts lead to more dangerous mutations.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Baxter Stockman"], 
            SEASON3_RECURRING_CAST["Shredder"]
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Baxter Stockman", "Shredder"],
        "notes": "Baxter transformation episode"
    },
    {
        "episode_id": 63,
        "title": "The Big Rip-Off",
        "season": 3,
        "episode_number": 45,
        "air_date": "1989-11-27",
        "synopsis": "Shredder steals advanced technology from various sources to create the ultimate weapon against the Turtles.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Technology theft episode"
    },
    {
        "episode_id": 64,
        "title": "The Big Break-In",
        "season": 3,
        "episode_number": 46,
        "air_date": "1989-11-28",
        "synopsis": "The Turtles infiltrate the Technodrome to stop Shredder's latest plan, leading to an epic confrontation.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Part 1 of season finale"
    },
    {
        "episode_id": 65,
        "title": "The Big Blow Out",
        "season": 3,
        "episode_number": 47,
        "air_date": "1989-11-29",
        "synopsis": "The Technodrome returns to Earth's surface for a final assault on New York City in the season's climactic battle.",
        "cast": MAIN_CAST + [
            SEASON3_RECURRING_CAST["Shredder"], 
            SEASON3_RECURRING_CAST["Krang"], 
            SEASON3_RECURRING_CAST["Bebop"], 
            SEASON3_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Season 3 finale - Part 2"
    }
]