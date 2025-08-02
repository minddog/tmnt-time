#!/usr/bin/env python3
"""
Script to reload Season 1 episodes in Convex database
This will clear existing Season 1 episodes and re-add them
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from convex import ConvexClient
from dotenv import load_dotenv
from api.data.episodes.season1 import SEASON_1_EPISODES

# Load environment variables from .env.local for development database
load_dotenv('.env.local')

def clear_season1_episodes(client):
    """Clear all Season 1 episodes from the database"""
    print("Clearing Season 1 episodes...")
    
    try:
        # Get all Season 1 episodes
        episodes = client.query("episodes:getAll", {"season": 1})
        cleared_count = 0
        
        for episode in episodes:
            # Delete each episode
            try:
                client.mutation("episodes:deleteById", {"id": episode["_id"]})
                cleared_count += 1
                print(f"  - Deleted: {episode['title']}")
            except Exception as e:
                print(f"  ✗ Error deleting {episode['title']}: {e}")
        
        print(f"\n✓ Cleared {cleared_count} Season 1 episodes")
        return True
    except Exception as e:
        print(f"✗ Error clearing episodes: {e}")
        return False

def add_season1_episodes(client):
    """Add all Season 1 episodes to the database"""
    print("\nAdding Season 1 episodes...")
    
    success_count = 0
    error_count = 0
    
    for episode in SEASON_1_EPISODES:
        try:
            # Prepare episode data
            episode_data = {
                "episode_id": episode.id,
                "title": episode.title,
                "season": episode.season,
                "episode_number": episode.episode_number,
                "air_date": episode.air_date,
                "synopsis": episode.synopsis
            }
            
            # Add optional fields if present
            if episode.cast:
                episode_data["cast"] = [
                    {
                        "character_name": cast.character_name,
                        "voice_actor": cast.voice_actor,
                        "role": cast.role
                    }
                    for cast in episode.cast
                ]
            
            if episode.writer:
                episode_data["writer"] = episode.writer
            
            if episode.director:
                episode_data["director"] = episode.director
            
            if episode.notes:
                episode_data["notes"] = episode.notes
            
            if episode.villains_featured:
                episode_data["villains_featured"] = episode.villains_featured
            
            # Add the episode
            client.mutation("episodes:addEpisode", episode_data)
            success_count += 1
            print(f"  ✓ Added: {episode.title}")
            
        except Exception as e:
            error_count += 1
            print(f"  ✗ Error adding {episode.title}: {e}")
    
    print(f"\n✓ Added {success_count} episodes")
    if error_count > 0:
        print(f"✗ {error_count} errors occurred")
    
    return error_count == 0

def main():
    """Main function"""
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
    
    # First, we need to create a delete mutation in Convex
    print("NOTE: This script requires a 'deleteById' mutation in convex/episodes.js")
    print("Add this mutation if it doesn't exist:")
    print("""
export const deleteById = mutation({
  args: { id: v.id("episodes") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return { success: true };
  },
});
""")
    
    response = input("\nDo you want to proceed? (yes/no): ")
    if response.lower() != 'yes':
        print("Aborted.")
        return
    
    # Clear Season 1 episodes
    if clear_season1_episodes(client):
        # Re-add Season 1 episodes
        if add_season1_episodes(client):
            print("\n✅ Season 1 episodes successfully reloaded!")
        else:
            print("\n⚠️  Some errors occurred while adding episodes")
    else:
        print("\n❌ Failed to clear Season 1 episodes")

if __name__ == "__main__":
    main()