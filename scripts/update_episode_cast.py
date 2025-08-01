#!/usr/bin/env python3
"""
Script to update episodes with cast information
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from convex import ConvexClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Sample cast data for the first few episodes
EPISODE_CAST_DATA = {
    1: {  # "Turtle Tracks"
        "cast": [
            {"character_name": "Leonardo", "voice_actor": "Cam Clarke", "role": "main"},
            {"character_name": "Donatello", "voice_actor": "Barry Gordon", "role": "main"},
            {"character_name": "Raphael", "voice_actor": "Rob Paulsen", "role": "main"},
            {"character_name": "Michelangelo", "voice_actor": "Townsend Coleman", "role": "main"},
            {"character_name": "Splinter", "voice_actor": "Peter Renaday", "role": "main"},
            {"character_name": "April O'Neil", "voice_actor": "Renae Jacobs", "role": "main"},
            {"character_name": "Shredder", "voice_actor": "James Avery", "role": "main"},
            {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "guest"},
            {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "guest"}
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "notes": "Series premiere episode introducing the turtles and their origin story"
    },
    2: {  # "Enter the Shredder"
        "cast": [
            {"character_name": "Leonardo", "voice_actor": "Cam Clarke", "role": "main"},
            {"character_name": "Donatello", "voice_actor": "Barry Gordon", "role": "main"},
            {"character_name": "Raphael", "voice_actor": "Rob Paulsen", "role": "main"},
            {"character_name": "Michelangelo", "voice_actor": "Townsend Coleman", "role": "main"},
            {"character_name": "Splinter", "voice_actor": "Peter Renaday", "role": "main"},
            {"character_name": "April O'Neil", "voice_actor": "Renae Jacobs", "role": "main"},
            {"character_name": "Shredder", "voice_actor": "James Avery", "role": "main"},
            {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"}
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "notes": "First appearance of Krang"
    },
    3: {  # "A Thing About Rats"
        "cast": [
            {"character_name": "Leonardo", "voice_actor": "Cam Clarke", "role": "main"},
            {"character_name": "Donatello", "voice_actor": "Barry Gordon", "role": "main"},
            {"character_name": "Raphael", "voice_actor": "Rob Paulsen", "role": "main"},
            {"character_name": "Michelangelo", "voice_actor": "Townsend Coleman", "role": "main"},
            {"character_name": "Splinter", "voice_actor": "Peter Renaday", "role": "main"},
            {"character_name": "April O'Neil", "voice_actor": "Renae Jacobs", "role": "main"},
            {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Shredder", "voice_actor": "James Avery", "role": "main"}
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "Introduction of Baxter Stockman and his Mousers"
    }
}

def update_episodes_with_cast():
    """Update episodes in Convex with cast information"""
    convex_url = os.environ.get('CONVEX_URL')
    if not convex_url:
        print("Error: CONVEX_URL not found in environment variables")
        return
    
    # Connect to Convex
    client = ConvexClient(convex_url)
    
    # Get all episodes first
    episodes = client.query("episodes:getAll", {})
    print(f"Found {len(episodes)} episodes in database")
    
    # Update episodes with cast data
    for episode in episodes:
        episode_id = episode.get('episode_id')
        if episode_id in EPISODE_CAST_DATA:
            cast_data = EPISODE_CAST_DATA[episode_id]
            
            # Check if we already have cast data
            if episode.get('cast') and len(episode['cast']) > 0:
                print(f"Episode {episode_id} already has cast data, skipping...")
                continue
            
            # Update episode
            try:
                # We need to use a mutation to update the episode
                # For now, let's just print what we would update
                print(f"\nWould update Episode {episode_id}: {episode['title']}")
                print(f"  - Adding {len(cast_data['cast'])} cast members")
                print(f"  - Writer: {cast_data.get('writer', 'N/A')}")
                print(f"  - Director: {cast_data.get('director', 'N/A')}")
                print(f"  - Notes: {cast_data.get('notes', 'N/A')[:50]}...")
                
                # In a real scenario, you would call a mutation here:
                # client.mutation("episodes:update", {
                #     "episode_id": episode_id,
                #     "cast": cast_data['cast'],
                #     "writer": cast_data.get('writer'),
                #     "director": cast_data.get('director'),
                #     "notes": cast_data.get('notes')
                # })
                
            except Exception as e:
                print(f"Error updating episode {episode_id}: {e}")
    
    print("\nNote: This is a dry run. To actually update, you'll need to:")
    print("1. Create an update mutation in convex/episodes.js")
    print("2. Uncomment the mutation call in this script")

if __name__ == "__main__":
    update_episodes_with_cast()