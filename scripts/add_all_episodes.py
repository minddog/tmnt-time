#!/usr/bin/env python3
"""
Script to add ALL TMNT episodes (1987-1996) to Convex database
Total: 193 episodes across 10 seasons
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from convex import ConvexClient
from dotenv import load_dotenv

# Import all episodes from the organized season files
from api.data.episodes import ALL_EPISODES, SEASON_INFO, get_total_episode_count

# Load environment variables
load_dotenv()

def create_add_mutation():
    """Create the mutation in Convex to add new episodes"""
    mutation_code = '''
import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const addEpisode = mutation({
  args: {
    episode_id: v.number(),
    title: v.string(),
    season: v.number(),
    episode_number: v.number(),
    air_date: v.string(),
    synopsis: v.string(),
    cast: v.optional(v.array(v.object({
      character_name: v.string(),
      voice_actor: v.string(),
      role: v.string(),
    }))),
    writer: v.optional(v.string()),
    director: v.optional(v.string()),
    notes: v.optional(v.string()),
    villains_featured: v.optional(v.array(v.string())),
  },
  handler: async (ctx, args) => {
    // Check if episode already exists
    const existing = await ctx.db
      .query("episodes")
      .withIndex("by_episode_id", (q) => q.eq("episode_id", args.episode_id))
      .first();
    
    if (existing) {
      throw new Error(`Episode ${args.episode_id} already exists`);
    }
    
    // Add the episode
    await ctx.db.insert("episodes", args);
    
    return { success: true, episode_id: args.episode_id };
  },
});
'''
    print("\nTo enable adding episodes, add this mutation to convex/episodes.js:")
    print(mutation_code)

def add_all_episodes(dry_run=True, episodes_to_process=None):
    """Add all TMNT episodes to the database"""
    # Use production URL
    convex_url = "https://useful-ptarmigan-757.convex.cloud"
    print(f"Using Convex URL: {convex_url}")
    
    # Connect to Convex
    client = ConvexClient(convex_url)
    
    # Use provided episodes or default to ALL_EPISODES
    episodes = episodes_to_process if episodes_to_process is not None else ALL_EPISODES
    
    print(f"Connected to Convex")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE UPDATE'}")
    print(f"Total episodes to process: {len(episodes)}")
    print("-" * 60)
    
    # Show season breakdown
    print("\nSeason Breakdown:")
    for season_num, info in SEASON_INFO.items():
        print(f"  Season {season_num}: {info['episodes']} episodes ({info['year']}) - {info['description']}")
    print("-" * 60)
    
    # Process each episode
    success_count = 0
    error_count = 0
    skipped_count = 0
    
    for episode in episodes:
        try:
            episode_id = episode['episode_id']
            print(f"\nProcessing Episode {episode_id}: {episode['title']} (S{episode['season']}E{episode['episode_number']})")
            
            if not dry_run:
                # Check if episode exists
                try:
                    existing = client.query("episodes:getById", {"episode_id": episode_id})
                    if existing:
                        print(f"  → Episode already exists, skipping")
                        skipped_count += 1
                        continue
                except Exception as e:
                    # Episode doesn't exist, which is what we want
                    pass
                
                # Add the episode - make sure we're only sending the fields we need
                episode_data = {
                    "episode_id": episode["episode_id"],
                    "title": episode["title"],
                    "season": episode["season"],
                    "episode_number": episode["episode_number"],
                    "air_date": episode["air_date"],
                    "synopsis": episode["synopsis"]
                }
                
                # Add optional fields if they exist
                if "cast" in episode and episode["cast"]:
                    episode_data["cast"] = episode["cast"]
                if "writer" in episode and episode["writer"]:
                    episode_data["writer"] = episode["writer"]
                if "director" in episode and episode["director"]:
                    episode_data["director"] = episode["director"]
                if "notes" in episode and episode["notes"]:
                    episode_data["notes"] = episode["notes"]
                if "villains_featured" in episode and episode["villains_featured"]:
                    episode_data["villains_featured"] = episode["villains_featured"]
                
                result = client.mutation("episodes:addEpisode", episode_data)
                print(f"  ✓ Added successfully")
                success_count += 1
            else:
                print(f"  - Would add (dry run)")
                success_count += 1
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
            error_count += 1
    
    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  Total episodes: {len(episodes)}")
    print(f"  Success: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Skipped: {skipped_count}")
    
    if dry_run:
        print("\nThis was a DRY RUN. To perform actual updates:")
        print("1. Create the addEpisode mutation in Convex")
        print("2. Run this script with --live flag")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Add all TMNT episodes')
    parser.add_argument('--live', action='store_true', help='Perform actual updates (default is dry run)')
    parser.add_argument('--show-mutation', action='store_true', help='Show the Convex mutation code')
    parser.add_argument('--season', type=int, help='Add episodes from a specific season only')
    parser.add_argument('--list-seasons', action='store_true', help='List all seasons with episode counts')
    
    args = parser.parse_args()
    
    if args.show_mutation:
        create_add_mutation()
    elif args.list_seasons:
        print("\nTMNT 1987 Series - All Seasons:")
        print("-" * 60)
        for season_num, info in SEASON_INFO.items():
            print(f"Season {season_num}: {info['episodes']} episodes ({info['year']}) - {info['description']}")
        print(f"\nTotal Episodes: {get_total_episode_count()}")
    else:
        # If specific season requested, filter episodes
        if args.season:
            from api.data.episodes import get_episodes_by_season
            season_episodes = get_episodes_by_season(args.season)
            if season_episodes:
                print(f"\nProcessing Season {args.season} only ({len(season_episodes)} episodes)")
                add_all_episodes(dry_run=not args.live, episodes_to_process=season_episodes)
            else:
                print(f"Season {args.season} not found!")
        else:
            add_all_episodes(dry_run=not args.live)