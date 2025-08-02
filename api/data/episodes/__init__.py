"""
TMNT 1987 Series Episodes Collection
Total: 193 episodes across 10 seasons (1987-1996)
"""

from .season1 import SEASON1_EPISODES
from .season2 import SEASON2_EPISODES
from .season3 import SEASON3_EPISODES
from .season4 import SEASON4_EPISODES
from .season5 import SEASON5_EPISODES
from .season6 import SEASON6_EPISODES
from .season7 import SEASON7_EPISODES
from .season8 import SEASON8_EPISODES
from .season9 import SEASON9_EPISODES
from .season10 import SEASON10_EPISODES

# Combine all episodes
ALL_EPISODES = (
    SEASON1_EPISODES +
    SEASON2_EPISODES +
    SEASON3_EPISODES +
    SEASON4_EPISODES +
    SEASON5_EPISODES +
    SEASON6_EPISODES +
    SEASON7_EPISODES +
    SEASON8_EPISODES +
    SEASON9_EPISODES +
    SEASON10_EPISODES
)

# Export season lists and combined list
__all__ = [
    'SEASON1_EPISODES',
    'SEASON2_EPISODES', 
    'SEASON3_EPISODES',
    'SEASON4_EPISODES',
    'SEASON5_EPISODES',
    'SEASON6_EPISODES',
    'SEASON7_EPISODES',
    'SEASON8_EPISODES',
    'SEASON9_EPISODES',
    'SEASON10_EPISODES',
    'ALL_EPISODES'
]

# Season information
SEASON_INFO = {
    1: {"episodes": 5, "year": 1987, "description": "Series premiere - Origin story"},
    2: {"episodes": 13, "year": 1988, "description": "First full season"},
    3: {"episodes": 47, "year": 1989, "description": "Longest season - Daily syndication"},
    4: {"episodes": 39, "year": 1990, "description": "New mutants and characters"},
    5: {"episodes": 13, "year": 1991, "description": "More mutant allies"},
    6: {"episodes": 16, "year": 1992, "description": "Final CBS season"},
    7: {"episodes": 27, "year": 1993, "description": "European vacation tour"},
    8: {"episodes": 8, "year": 1994, "description": "Red Sky era begins - Lord Dregg arrives"},
    9: {"episodes": 8, "year": 1995, "description": "Red Sky continues - Carter joins"},
    10: {"episodes": 8, "year": 1996, "description": "Final season - Series conclusion"}
}

def get_episodes_by_season(season_number):
    """Get all episodes for a specific season"""
    season_map = {
        1: SEASON1_EPISODES,
        2: SEASON2_EPISODES,
        3: SEASON3_EPISODES,
        4: SEASON4_EPISODES,
        5: SEASON5_EPISODES,
        6: SEASON6_EPISODES,
        7: SEASON7_EPISODES,
        8: SEASON8_EPISODES,
        9: SEASON9_EPISODES,
        10: SEASON10_EPISODES
    }
    return season_map.get(season_number, [])

def get_total_episode_count():
    """Get total number of episodes in the series"""
    return len(ALL_EPISODES)

def get_episodes_by_villain(villain_name):
    """Get all episodes featuring a specific villain"""
    episodes = []
    for episode in ALL_EPISODES:
        if villain_name in episode.get("villains_featured", []):
            episodes.append(episode)
    return episodes

def get_episodes_by_year(year):
    """Get all episodes that aired in a specific year"""
    episodes = []
    for episode in ALL_EPISODES:
        if episode["air_date"].startswith(str(year)):
            episodes.append(episode)
    return episodes