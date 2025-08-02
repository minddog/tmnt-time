"""
TMNT 1987 Series - Season 4 Episodes (1990)
Total Episodes: 39
"""

from typing import List, Dict, Any
from .season1 import MAIN_CAST

# Recurring cast for Season 4
SEASON4_RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Baxter Stockman": {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Rat King": {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"},
    "Slash": {"character_name": "Slash", "voice_actor": "Pat Fraley", "role": "guest"},
    "Casey Jones": {"character_name": "Casey Jones", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Irma": {"character_name": "Irma Langinstein", "voice_actor": "Jennifer Darling", "role": "recurring"},
    "Vernon": {"character_name": "Vernon Fenwick", "voice_actor": "Peter Renaday", "role": "recurring"},
    "Burne Thompson": {"character_name": "Burne Thompson", "voice_actor": "Pat Fraley", "role": "recurring"},
}

SEASON4_EPISODES: List[Dict[str, Any]] = [
    {
        "episode_id": 66,
        "title": "Plan Six from Outer Space",
        "season": 4,
        "episode_number": 1,
        "air_date": "1990-09-10",
        "synopsis": "The Turtles face an alien invasion as creatures from Dimension X implement their sixth plan to conquer Earth.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Season 4 premiere"
    },
    {
        "episode_id": 67,
        "title": "Turtles of the Jungle",
        "season": 4,
        "episode_number": 2,
        "air_date": "1990-09-11",
        "synopsis": "Professor Willard W. Willard turns the city into a jungle, and a Tarzan-like hero named Jess Harley helps the Turtles.",
        "cast": MAIN_CAST + [
            {"character_name": "Jess Harley", "voice_actor": "Jim Cummings", "role": "guest"},
            {"character_name": "Professor Willard", "voice_actor": "Peter Renaday", "role": "guest"}
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Professor Willard"],
        "notes": "Jungle transformation episode"
    },
    {
        "episode_id": 68,
        "title": "Michelangelo Toys Around",
        "season": 4,
        "episode_number": 3,
        "air_date": "1990-09-12",
        "synopsis": "Michelangelo refuses to grow up and gets trapped in a toy world, forcing his brothers to rescue him.",
        "cast": MAIN_CAST + [SEASON4_RECURRING_CAST["Shredder"]],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Toy-themed episode"
    },
    {
        "episode_id": 69,
        "title": "Peking Turtle",
        "season": 4,
        "episode_number": 4,
        "air_date": "1990-09-13",
        "synopsis": "The Turtles travel to Beijing to stop Shredder from stealing an ancient power source.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "International adventure"
    },
    {
        "episode_id": 70,
        "title": "Shredder's Mom",
        "season": 4,
        "episode_number": 5,
        "air_date": "1990-09-14",
        "synopsis": "Shredder's mother arrives from Japan and disapproves of her son's villainous lifestyle.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"],
            {"character_name": "Miyoko", "voice_actor": "Pat Musick", "role": "guest"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Comedy episode featuring Shredder's mother"
    },
    {
        "episode_id": 71,
        "title": "Four Turtles and a Baby",
        "season": 4,
        "episode_number": 6,
        "air_date": "1990-09-17",
        "synopsis": "The Turtles must protect an alien baby from both Shredder and its destructive powers.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise & Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Baby-sitting episode"
    },
    {
        "episode_id": 72,
        "title": "Turtlemaniac",
        "season": 4,
        "episode_number": 7,
        "air_date": "1990-09-18",
        "synopsis": "A young fan of the Turtles tries to help them but ends up causing more trouble than good.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"],
            {"character_name": "Zach", "voice_actor": "Rob Paulsen", "role": "guest"}
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Return of Zach character"
    },
    {
        "episode_id": 73,
        "title": "Rondo in New York",
        "season": 4,
        "episode_number": 8,
        "air_date": "1990-09-19",
        "synopsis": "Shredder and Krang try to steal a powerful energy source during a concert at the Metropolitan Opera House.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Gordon Bressack",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Opera-themed episode"
    },
    {
        "episode_id": 74,
        "title": "Planet of the Turtles",
        "season": 4,
        "episode_number": 9,
        "air_date": "1990-09-20",
        "synopsis": "The Turtles travel to Shell-Ri-La, a planet populated by humanoid turtles who need their help.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "George Shea",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Alien turtle civilization"
    },
    {
        "episode_id": 75,
        "title": "Name That Toon",
        "season": 4,
        "episode_number": 10,
        "air_date": "1990-09-21",
        "synopsis": "A magical remote control brings cartoon characters to life, causing chaos in the real world.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "Jack Mendelsohn & Carole Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Meta cartoon episode"
    },
    {
        "episode_id": 76,
        "title": "Menace Maestro, Please",
        "season": 4,
        "episode_number": 11,
        "air_date": "1990-09-24",
        "synopsis": "A mad composer uses his music to control people's minds, and the Turtles must stop his symphonic scheme.",
        "cast": MAIN_CAST + [
            {"character_name": "Maestro", "voice_actor": "Cam Clarke", "role": "guest"}
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Maestro"],
        "notes": "Music-themed villain"
    },
    {
        "episode_id": 77,
        "title": "Superhero for a Day",
        "season": 4,
        "episode_number": 12,
        "air_date": "1990-09-25",
        "synopsis": "A gadget salesman becomes a superhero called Gadgetman but causes more problems than he solves.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"],
            {"character_name": "Gadgetman", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "Francis Moss",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Superhero parody"
    },
    {
        "episode_id": 78,
        "title": "Back to the Egg",
        "season": 4,
        "episode_number": 13,
        "air_date": "1990-09-26",
        "synopsis": "Krang's latest invention turns the Turtles back into baby turtles, leaving them vulnerable to attack.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Age regression episode"
    },
    {
        "episode_id": 79,
        "title": "Son of Return of the Fly II",
        "season": 4,
        "episode_number": 14,
        "air_date": "1990-10-06",
        "synopsis": "Baxter Stockman returns once again with a new plan for revenge and a way to restore his human form.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Baxter Stockman"], 
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Baxter Stockman", "Shredder"],
        "notes": "Another Baxter return episode"
    },
    {
        "episode_id": 80,
        "title": "Raphael Knocks 'em Dead",
        "season": 4,
        "episode_number": 15,
        "air_date": "1990-10-13",
        "synopsis": "Raphael tries stand-up comedy but becomes controlled by aliens who use laughter as a weapon.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"],
            {"character_name": "Barney Stockman", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Aliens"],
        "notes": "Comedy club episode"
    },
    {
        "episode_id": 81,
        "title": "Bebop and Rocksteady Conquer the Universe",
        "season": 4,
        "episode_number": 16,
        "air_date": "1990-10-20",
        "synopsis": "Bebop and Rocksteady steal the Technodrome's power source and attempt to conquer the world themselves.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Bebop", "Rocksteady", "Shredder", "Krang"],
        "notes": "Bebop and Rocksteady focus episode"
    },
    {
        "episode_id": 82,
        "title": "Raphael Meets His Match",
        "season": 4,
        "episode_number": 17,
        "air_date": "1990-10-27",
        "synopsis": "Raphael meets Mona Lisa, a mutant lizard who becomes his love interest while they fight Captain Filch.",
        "cast": MAIN_CAST + [
            {"character_name": "Mona Lisa", "voice_actor": "Cree Summer", "role": "guest"},
            {"character_name": "Captain Filch", "voice_actor": "Cam Clarke", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Captain Filch"],
        "notes": "Introduction of Mona Lisa"
    },
    {
        "episode_id": 83,
        "title": "Slash - The Evil Turtle from Dimension X",
        "season": 4,
        "episode_number": 18,
        "air_date": "1990-11-03",
        "synopsis": "Bebop and Rocksteady's pet turtle Slash is mutated and becomes a dangerous enemy of the Turtles.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"],
            SEASON4_RECURRING_CAST["Slash"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Slash", "Shredder", "Krang", "Bebop", "Rocksteady"],
        "notes": "Introduction of Slash"
    },
    {
        "episode_id": 84,
        "title": "Leonardo Lightens Up",
        "season": 4,
        "episode_number": 19,
        "air_date": "1990-11-10",
        "synopsis": "A personality ray makes Leonardo act silly and carefree, jeopardizing the team during a crucial mission.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Leonardo personality change"
    },
    {
        "episode_id": 85,
        "title": "Were-Rats from Channel 6",
        "season": 4,
        "episode_number": 20,
        "air_date": "1990-11-17",
        "synopsis": "The Rat King turns April and Irma into were-rats as part of his plan to create a rodent army.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Rat King"], 
            SEASON4_RECURRING_CAST["Irma"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Rat King"],
        "notes": "Were-rat transformation"
    },
    {
        "episode_id": 86,
        "title": "Funny, They Shrunk Michelangelo",
        "season": 4,
        "episode_number": 21,
        "air_date": "1990-11-24",
        "synopsis": "Michelangelo is shrunk to microscopic size and must navigate the dangers of being tiny.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Shrinking episode"
    },
    {
        "episode_id": 87,
        "title": "The Big Zipp Attack",
        "season": 4,
        "episode_number": 22,
        "air_date": "1990-09-08",
        "synopsis": "Aliens called Zippies invade Earth, and their cuteness hides their true destructive nature.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "Francis Moss & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Zippies"],
        "notes": "Cute but deadly aliens"
    },
    {
        "episode_id": 88,
        "title": "Donatello Makes Time",
        "season": 4,
        "episode_number": 23,
        "air_date": "1990-09-15",
        "synopsis": "Donatello invents a time-stopping device, but it falls into the wrong hands.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Time manipulation episode"
    },
    {
        "episode_id": 89,
        "title": "Farewell, Lotus Blossom",
        "season": 4,
        "episode_number": 24,
        "air_date": "1990-09-22",
        "synopsis": "Lotus Blossom returns and must choose between her ninja clan and her feelings for Leonardo.",
        "cast": MAIN_CAST + [
            {"character_name": "Lotus Blossom", "voice_actor": "Renae Jacobs", "role": "guest"},
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Lotus Blossom returns"
    },
    {
        "episode_id": 90,
        "title": "Rebel Without a Fin",
        "season": 4,
        "episode_number": 25,
        "air_date": "1990-09-29",
        "synopsis": "A mutant fish named Ray joins the Turtles and must learn to control his rebellious nature.",
        "cast": MAIN_CAST + [
            {"character_name": "Ray", "voice_actor": "Pat Fraley", "role": "guest"},
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Mutant fish character"
    },
    {
        "episode_id": 91,
        "title": "Rhino-Man",
        "season": 4,
        "episode_number": 26,
        "air_date": "1990-10-27",
        "synopsis": "The world's dumbest criminal becomes the powerful Rhino-Man and challenges the Turtles.",
        "cast": MAIN_CAST + [
            {"character_name": "Rhino-Man", "voice_actor": "Jim Cummings", "role": "guest"},
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Rhino-Man", "Shredder"],
        "notes": "New mutant villain"
    },
    {
        "episode_id": 92,
        "title": "Michelangelo Meets Bugman",
        "season": 4,
        "episode_number": 27,
        "air_date": "1990-11-03",
        "synopsis": "Michelangelo befriends Bugman, a superhero whose good intentions often backfire.",
        "cast": MAIN_CAST + [
            {"character_name": "Bugman", "voice_actor": "Dan Gilvezan", "role": "guest"},
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Superhero team-up"
    },
    {
        "episode_id": 93,
        "title": "Poor Little Rich Turtle",
        "season": 4,
        "episode_number": 28,
        "air_date": "1990-11-10",
        "synopsis": "Michelangelo inherits a fortune and must decide between wealth and his family.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Antonio Ortiz & Rowby Goren",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Wealth and values episode"
    },
    {
        "episode_id": 94,
        "title": "What's Michelangelo Good For?",
        "season": 4,
        "episode_number": 29,
        "air_date": "1990-11-17",
        "synopsis": "Michelangelo feels useless and tries to prove his worth to the team.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "Charles M. Howell IV & Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Michelangelo character development"
    },
    {
        "episode_id": 95,
        "title": "The Dimension X Story",
        "season": 4,
        "episode_number": 30,
        "air_date": "1990-11-24",
        "synopsis": "April travels to Dimension X to report on Krang's home dimension and gets trapped there.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"], 
            SEASON4_RECURRING_CAST["Vernon"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Dimension X exploration"
    },
    {
        "episode_id": 96,
        "title": "Donatello's Degree",
        "season": 4,
        "episode_number": 31,
        "air_date": "1990-12-01",
        "synopsis": "Donatello receives an honorary degree but must defend the university from Shredder's attack.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Jack Mendelsohn",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"],
        "notes": "Donatello honor episode"
    },
    {
        "episode_id": 97,
        "title": "The Big Cufflink Caper!",
        "season": 4,
        "episode_number": 32,
        "air_date": "1990-10-20",
        "synopsis": "The Turtles investigate the theft of priceless cufflinks that hide alien technology.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Mystery caper episode"
    },
    {
        "episode_id": 98,
        "title": "Leonardo Versus Tempestra",
        "season": 4,
        "episode_number": 33,
        "air_date": "1990-11-24",
        "synopsis": "Leonardo falls in love with a mysterious woman who turns out to be a dangerous sorceress.",
        "cast": MAIN_CAST + [
            {"character_name": "Tempestra", "voice_actor": "Tress MacNeille", "role": "guest"},
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Tempestra", "Shredder"],
        "notes": "Leonardo romance episode"
    },
    {
        "episode_id": 99,
        "title": "Splinter Vanishes",
        "season": 4,
        "episode_number": 34,
        "air_date": "1990-12-01",
        "synopsis": "Splinter mysteriously disappears, and the Turtles must find him before Shredder does.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "Francis Moss & Ted Pedersen",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Splinter disappearance mystery"
    },
    {
        "episode_id": 100,
        "title": "Raphael Drives 'Em Wild",
        "season": 4,
        "episode_number": 35,
        "air_date": "1990-12-08",
        "synopsis": "Raphael's aggressive driving gets him into trouble when he enters a dangerous race.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"],
            {"character_name": "Otto", "voice_actor": "Pat Fraley", "role": "guest"}
        ],
        "writer": "Misty Taggart",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Racing episode"
    },
    {
        "episode_id": 101,
        "title": "Beyond the Donatello Nebula",
        "season": 4,
        "episode_number": 36,
        "air_date": "1990-12-15",
        "synopsis": "Donatello discovers a nebula named after him but it hides a dangerous alien threat.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder", "Krang"],
        "notes": "Space adventure"
    },
    {
        "episode_id": 102,
        "title": "Big Bug Blunder",
        "season": 4,
        "episode_number": 37,
        "air_date": "1990-12-22",
        "synopsis": "Genghis Frog accidentally releases giant insects that threaten the city.",
        "cast": MAIN_CAST + [
            {"character_name": "Genghis Frog", "voice_actor": "Jim Cummings", "role": "guest"},
            SEASON4_RECURRING_CAST["Shredder"]
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "villains_featured": ["Giant Insects"],
        "notes": "Return of Genghis Frog"
    },
    {
        "episode_id": 103,
        "title": "The Foot Soldiers are Revolting",
        "season": 4,
        "episode_number": 38,
        "air_date": "1990-12-29",
        "synopsis": "The Foot Soldiers rebel against Shredder and start their own crime wave.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"], 
            SEASON4_RECURRING_CAST["Krang"], 
            SEASON4_RECURRING_CAST["Bebop"], 
            SEASON4_RECURRING_CAST["Rocksteady"]
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "villains_featured": ["Foot Soldiers", "Shredder", "Krang"],
        "notes": "Foot Soldier rebellion"
    },
    {
        "episode_id": 104,
        "title": "Unidentified Flying Leonardo",
        "season": 4,
        "episode_number": 39,
        "air_date": "1991-01-05",
        "synopsis": "Leonardo is mistaken for an alien and becomes the target of UFO hunters.",
        "cast": MAIN_CAST + [
            SEASON4_RECURRING_CAST["Shredder"],
            {"character_name": "UFO Hunters", "voice_actor": "Various", "role": "guest"}
        ],
        "writer": "Dennis O'Flaherty",
        "director": "Fred Wolf",
        "villains_featured": ["Shredder"],
        "notes": "Season 4 finale - UFO conspiracy episode"
    }
]