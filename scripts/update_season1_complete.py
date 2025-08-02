#!/usr/bin/env python3
"""
Script to update Season 1 episodes with complete data
Fixes missing cast, writers, directors, and villain information
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from convex import ConvexClient
from dotenv import load_dotenv
from api.data.episodes import SEASON1_EPISODES

# Load environment variables from .env.local for development database
load_dotenv('.env.local')

def update_season1_episodes():
    """Update all Season 1 episodes with complete data"""
    # Get Convex URL from environment
    convex_url = os.getenv('CONVEX_URL')
    if not convex_url:
        print("Error: CONVEX_URL not found in environment variables")
        print("Please set CONVEX_URL in your .env.local file")
        return
    
    print(f"Using Convex URL: {convex_url}")
    print("=" * 60)
    
    # Connect to Convex
    try:
        client = ConvexClient(convex_url)
        print("Connected to Convex\n")
    except Exception as e:
        print(f"Failed to connect to Convex: {e}")
        return
    
    print("Updating Season 1 episodes with complete data...")
    print("-" * 60)
    
    success_count = 0
    error_count = 0
    
    for episode in SEASON1_EPISODES:
        try:
            print(f"\nProcessing Episode {episode['episode_id']}: {episode['title']}")
            
            # Prepare update data
            update_data = {
                "episode_id": episode['episode_id']
            }
            
            # Add cast information if present
            if 'cast' in episode and episode['cast']:
                update_data["cast"] = [
                    {
                        "character_name": cast_member.get('character_name', ''),
                        "voice_actor": cast_member.get('voice_actor', ''),
                        "role": cast_member.get('role', 'main')
                    }
                    for cast_member in episode['cast']
                ]
                print(f"  - Adding {len(episode['cast'])} cast members")
            
            # Add writer if present
            if 'writer' in episode and episode['writer']:
                update_data["writer"] = episode['writer']
                print(f"  - Writer: {episode['writer']}")
            
            # Add director if present
            if 'director' in episode and episode['director']:
                update_data["director"] = episode['director']
                print(f"  - Director: {episode['director']}")
            
            # Add notes if present
            if 'notes' in episode and episode['notes']:
                update_data["notes"] = episode['notes']
                print(f"  - Notes: {episode['notes'][:50]}...")
            
            # Add villains featured if present
            if 'villains_featured' in episode and episode['villains_featured']:
                update_data["villains_featured"] = episode['villains_featured']
                print(f"  - Villains: {', '.join(episode['villains_featured'])}")
            
            # Update the episode
            result = client.mutation("episodes:updateEpisode", update_data)
            success_count += 1
            print(f"  ✓ Successfully updated")
            
        except Exception as e:
            error_count += 1
            print(f"  ✗ Error updating episode {episode['episode_id']}: {e}")
    
    print("\n" + "=" * 60)
    print(f"Update Summary:")
    print(f"  ✓ Successfully updated: {success_count} episodes")
    if error_count > 0:
        print(f"  ✗ Errors encountered: {error_count} episodes")
    print("=" * 60)

def main():
    """Main function"""
    print("Season 1 Episode Data Updater")
    print("This will update existing Season 1 episodes with complete information")
    print("including cast, writers, directors, and villains featured.\n")
    
    response = input("Do you want to proceed? (yes/no): ")
    if response.lower() != 'yes':
        print("Update cancelled.")
        return
    
    update_season1_episodes()

if __name__ == "__main__":
    main()