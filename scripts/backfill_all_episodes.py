#!/usr/bin/env python3
"""
Script to backfill all episodes with complete cast and production information
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

# Main cast members (appear in most episodes)
MAIN_CAST = [
    {"character_name": "Leonardo", "voice_actor": "Cam Clarke", "role": "main"},
    {"character_name": "Donatello", "voice_actor": "Barry Gordon", "role": "main"},
    {"character_name": "Raphael", "voice_actor": "Rob Paulsen", "role": "main"},
    {"character_name": "Michelangelo", "voice_actor": "Townsend Coleman", "role": "main"},
    {"character_name": "Master Splinter", "voice_actor": "Peter Renaday", "role": "main"},
    {"character_name": "April O'Neil", "voice_actor": "Renae Jacobs", "role": "main"},
]

# Recurring villains
RECURRING_CAST = {
    "Shredder": {"character_name": "Shredder", "voice_actor": "James Avery", "role": "recurring"},
    "Krang": {"character_name": "Krang", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Bebop": {"character_name": "Bebop", "voice_actor": "Barry Gordon", "role": "recurring"},
    "Rocksteady": {"character_name": "Rocksteady", "voice_actor": "Cam Clarke", "role": "recurring"},
    "Baxter Stockman": {"character_name": "Baxter Stockman", "voice_actor": "Pat Fraley", "role": "recurring"},
    "Rat King": {"character_name": "Rat King", "voice_actor": "Townsend Coleman", "role": "recurring"},
    "Leatherhead": {"character_name": "Leatherhead", "voice_actor": "Jim Cummings", "role": "guest"},
}

# Comprehensive episode data for Season 1
EPISODE_DATA = {
    1: {
        "title": "Turtle Tracks",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Bebop"],
            RECURRING_CAST["Rocksteady"],
            {"character_name": "News Reporter", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "notes": "Series premiere. Introduces the Turtles' origin story and their first encounter with the Shredder.",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"]
    },
    2: {
        "title": "Enter the Shredder",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Krang"],
            {"character_name": "Foot Soldier", "voice_actor": "Various", "role": "guest"},
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "notes": "First appearance of Krang. The Turtles learn about Shredder's connection to Splinter.",
        "villains_featured": ["Shredder", "Krang"]
    },
    3: {
        "title": "A Thing About Rats",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Baxter Stockman"],
            {"character_name": "Mouser Robot", "voice_actor": "Sound Effects", "role": "guest"},
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "Introduction of Baxter Stockman and his Mouser robots. First use of the Party Wagon.",
        "villains_featured": ["Baxter Stockman", "Shredder"]
    },
    4: {
        "title": "Hot Rodding Teenagers from Dimension X",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Krang"],
            {"character_name": "Neutrino #1", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Neutrino #2", "voice_actor": "Renae Jacobs", "role": "guest"},
            {"character_name": "Neutrino #3", "voice_actor": "Cam Clarke", "role": "guest"},
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "First appearance of the Neutrinos from Dimension X. Introduction of interdimensional travel.",
        "villains_featured": ["Shredder", "Krang"]
    },
    5: {
        "title": "Shredder & Splintered",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Krang"],
            {"character_name": "Technodrome Computer", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "David Wise & Patti Howeth",
        "director": "Fred Wolf",
        "notes": "Season 1 finale. First appearance of the Technodrome. Shredder's origin revealed.",
        "villains_featured": ["Shredder", "Krang"]
    },
    # Season 2 episodes
    6: {
        "title": "Return of the Shredder",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            {"character_name": "Crooked Ninja Turtle Gang Member", "voice_actor": "Various", "role": "guest"},
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "Season 2 premiere. Shredder returns with a new plan involving fake turtle costumes.",
        "villains_featured": ["Shredder"]
    },
    7: {
        "title": "The Incredible Shrinking Turtles",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Baxter Stockman"],
            {"character_name": "Alien", "voice_actor": "Peter Renaday", "role": "guest"},
        ],
        "writer": "Larry Parr",
        "director": "Fred Wolf",
        "notes": "The Turtles are shrunk by Shredder's alien technology and must battle insects.",
        "villains_featured": ["Shredder", "Baxter Stockman"]
    },
    8: {
        "title": "It Came from Beneath the Sewers",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            {"character_name": "Plant Monster", "voice_actor": "Sound Effects", "role": "guest"},
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "notes": "A mysterious plant creature threatens the city's water supply.",
        "villains_featured": ["Shredder"]
    },
    9: {
        "title": "The Mean Machines",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Bebop"],
            RECURRING_CAST["Rocksteady"],
            {"character_name": "Robot", "voice_actor": "Sound Effects", "role": "guest"},
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "notes": "Shredder creates robot duplicates of the Turtle Van and other vehicles.",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"]
    },
    10: {
        "title": "Curse of the Evil Eye",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Baxter Stockman"],
            {"character_name": "Blizzard", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "Reed Shelly & Bruce Shelly",
        "director": "Fred Wolf",
        "notes": "The Turtles must stop Shredder from using an ancient helmet with mystical powers.",
        "villains_featured": ["Shredder", "Baxter Stockman"]
    },
    11: {
        "title": "Case of the Killer Pizzas",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Krang"],
            {"character_name": "Pizza Monster", "voice_actor": "Sound Effects", "role": "guest"},
        ],
        "writer": "Douglas Booth",
        "director": "Fred Wolf",
        "notes": "Krang's scheme involves meatballs that transform into dangerous creatures.",
        "villains_featured": ["Shredder", "Krang"]
    },
    12: {
        "title": "Enter: The Fly",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Baxter Stockman"],
            {"character_name": "Baxter Fly", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "Baxter Stockman is transformed into a mutant fly. Major character transformation episode.",
        "villains_featured": ["Shredder", "Baxter Stockman"]
    },
    13: {
        "title": "Invasion of the Punk Frogs",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            {"character_name": "Napoleon Bonafrog", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Genghis Frog", "voice_actor": "Jim Cummings", "role": "guest"},
            {"character_name": "Attila the Frog", "voice_actor": "Cam Clarke", "role": "guest"},
            {"character_name": "Rasputin the Mad Frog", "voice_actor": "Townsend Coleman", "role": "guest"},
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "notes": "Introduction of the Punk Frogs, mutant frogs initially tricked by Shredder.",
        "villains_featured": ["Shredder"]
    },
    14: {
        "title": "Splinter No More",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            {"character_name": "Scientist", "voice_actor": "Peter Renaday", "role": "guest"},
        ],
        "writer": "Larry Parr",
        "director": "Fred Wolf",
        "notes": "Donatello creates a formula to turn Splinter human again, with unexpected results.",
        "villains_featured": ["Shredder"]
    },
    15: {
        "title": "New York's Shiniest",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Bebop"],
            RECURRING_CAST["Rocksteady"],
            {"character_name": "Robot Cop", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "Shredder creates robot police officers to frame the Turtles for crimes.",
        "villains_featured": ["Shredder", "Bebop", "Rocksteady"]
    },
    16: {
        "title": "Teenagers from Dimension X",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Krang"],
            {"character_name": "Neutrino #1", "voice_actor": "Pat Fraley", "role": "guest"},
            {"character_name": "Neutrino #2", "voice_actor": "Renae Jacobs", "role": "guest"},
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "notes": "The Neutrinos return, pursued by Krang's forces from Dimension X.",
        "villains_featured": ["Shredder", "Krang"]
    },
    17: {
        "title": "The Cat Woman from Channel Six",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            {"character_name": "Irma", "voice_actor": "Jennifer Darling", "role": "recurring"},
            {"character_name": "Vernon", "voice_actor": "Peter Renaday", "role": "recurring"},
        ],
        "writer": "Richard Merwin",
        "director": "Fred Wolf",
        "notes": "April is mutated into a cat woman. First major April transformation episode.",
        "villains_featured": ["Shredder"]
    },
    18: {
        "title": "Return of the Technodrome",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            RECURRING_CAST["Krang"],
            RECURRING_CAST["Bebop"],
            RECURRING_CAST["Rocksteady"],
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "notes": "The Technodrome resurfaces with upgraded weapons. Major battle episode.",
        "villains_featured": ["Shredder", "Krang", "Bebop", "Rocksteady"]
    },
    19: {
        "title": "Beneath These Streets",
        "cast": MAIN_CAST + [
            RECURRING_CAST["Shredder"],
            {"character_name": "Tunneler", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "David Wise",
        "director": "Fred Wolf",
        "notes": "The Turtles explore abandoned subway tunnels and discover a lost civilization.",
        "villains_featured": ["Shredder"]
    },
    20: {
        "title": "Turtles on Trial",
        "cast": MAIN_CAST + [
            {"character_name": "Clayton Kellerman", "voice_actor": "Peter Renaday", "role": "guest"},
            {"character_name": "Judge", "voice_actor": "Pat Fraley", "role": "guest"},
        ],
        "writer": "Michael Reaves",
        "director": "Fred Wolf",
        "notes": "The Turtles are put on trial by a crooked prosecutor. Courtroom drama episode.",
        "villains_featured": []
    }
}

def create_update_mutation():
    """Create the mutation in Convex"""
    mutation_code = '''
import { mutation } from "./_generated/server";
import { v } from "convex/values";

export const updateEpisode = mutation({
  args: {
    episode_id: v.number(),
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
    // Find the episode
    const episode = await ctx.db
      .query("episodes")
      .withIndex("by_episode_id", (q) => q.eq("episode_id", args.episode_id))
      .first();
    
    if (!episode) {
      throw new Error(`Episode ${args.episode_id} not found`);
    }
    
    // Update the episode
    const updates = {};
    if (args.cast !== undefined) updates.cast = args.cast;
    if (args.writer !== undefined) updates.writer = args.writer;
    if (args.director !== undefined) updates.director = args.director;
    if (args.notes !== undefined) updates.notes = args.notes;
    if (args.villains_featured !== undefined) updates.villains_featured = args.villains_featured;
    
    await ctx.db.patch(episode._id, updates);
    
    return { success: true, episode_id: args.episode_id };
  },
});
'''
    print("\nTo enable updates, add this mutation to convex/episodes.js:")
    print(mutation_code)

def backfill_episodes(dry_run=True):
    """Backfill all episodes with cast and production data"""
    # Use production URL
    convex_url = "https://useful-ptarmigan-757.convex.cloud"
    print(f"Using Convex URL: {convex_url}")
    
    # Connect to Convex
    client = ConvexClient(convex_url)
    
    print(f"Connected to Convex")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE UPDATE'}")
    print("-" * 60)
    
    # Process each episode
    success_count = 0
    error_count = 0
    
    for episode_id, data in EPISODE_DATA.items():
        try:
            print(f"\nProcessing Episode {episode_id}: {data['title']}")
            print(f"  Cast members: {len(data['cast'])}")
            print(f"  Writer: {data.get('writer', 'Unknown')}")
            print(f"  Director: {data.get('director', 'Unknown')}")
            print(f"  Villains: {', '.join(data.get('villains_featured', []))}")
            
            if not dry_run:
                # Perform the actual update
                result = client.mutation("episodes:updateEpisode", {
                    "episode_id": episode_id,
                    "cast": data["cast"],
                    "writer": data.get("writer"),
                    "director": data.get("director"),
                    "notes": data.get("notes"),
                    "villains_featured": data.get("villains_featured", [])
                })
                print(f"  ✓ Updated successfully")
                success_count += 1
            else:
                print(f"  - Would update (dry run)")
                success_count += 1
                
        except Exception as e:
            print(f"  ✗ Error: {e}")
            error_count += 1
    
    print("\n" + "=" * 60)
    print(f"Summary:")
    print(f"  Total episodes: {len(EPISODE_DATA)}")
    print(f"  Success: {success_count}")
    print(f"  Errors: {error_count}")
    
    if dry_run:
        print("\nThis was a DRY RUN. To perform actual updates:")
        print("1. Create the updateEpisode mutation in Convex")
        print("2. Run this script with --live flag")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Backfill episode data')
    parser.add_argument('--live', action='store_true', help='Perform actual updates (default is dry run)')
    parser.add_argument('--show-mutation', action='store_true', help='Show the Convex mutation code')
    
    args = parser.parse_args()
    
    if args.show_mutation:
        create_update_mutation()
    else:
        backfill_episodes(dry_run=not args.live)