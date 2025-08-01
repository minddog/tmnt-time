#!/usr/bin/env python3
"""
Script to populate Convex database with TMNT data
"""
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from convex import ConvexClient
from api.data.tmnt_data import TURTLES, VILLAINS, EPISODES, QUOTES, WEAPONS
from typing import Dict, Any
import argparse


def populate_convex(convex_url: str):
    """Populate Convex with all TMNT data"""
    client = ConvexClient(convex_url)
    
    print("🚀 Starting Convex data population...")
    print(f"📡 Connected to: {convex_url}")
    
    # Populate turtles
    print("\n🐢 Populating turtles...")
    for name, turtle in TURTLES.items():
        turtle_data = turtle.model_dump()
        # Ensure the name field matches the key
        turtle_data['name'] = name
        
        try:
            client.mutation("mutations:createTurtle", turtle_data)
            print(f"  ✅ Added turtle: {turtle.full_name}")
        except Exception as e:
            print(f"  ❌ Failed to add turtle {name}: {e}")
    
    # Populate villains
    print("\n👹 Populating villains...")
    for name, villain in VILLAINS.items():
        villain_data = villain.model_dump()
        # Ensure the name field matches the key
        villain_data['name'] = name
        # Remove arch_enemy_of as it's not in the Convex schema
        villain_data.pop('arch_enemy_of', None)
        
        try:
            client.mutation("mutations:createVillain", villain_data)
            print(f"  ✅ Added villain: {villain.name}")
        except Exception as e:
            print(f"  ❌ Failed to add villain {name}: {e}")
    
    # Populate episodes
    print("\n📺 Populating episodes...")
    for episode in EPISODES:
        episode_data = episode.model_dump()
        # Rename 'id' to 'episode_id' for Convex
        episode_data['episode_id'] = episode_data.pop('id')
        # Remove villains_featured as it's not in the Convex schema
        episode_data.pop('villains_featured', None)
        
        try:
            client.mutation("mutations:createEpisode", episode_data)
            print(f"  ✅ Added episode: {episode.title}")
        except Exception as e:
            print(f"  ❌ Failed to add episode {episode.id}: {e}")
    
    # Populate quotes
    print("\n💬 Populating quotes...")
    for quote in QUOTES:
        quote_data = quote.model_dump()
        # Remove id field as it's not in the Convex schema
        quote_data.pop('id', None)
        # Remove None values for optional fields
        quote_data = {k: v for k, v in quote_data.items() if v is not None}
        
        try:
            client.mutation("mutations:createQuote", quote_data)
            print(f"  ✅ Added quote from {quote.character}")
        except Exception as e:
            print(f"  ❌ Failed to add quote: {e}")
    
    # Populate weapons
    print("\n⚔️ Populating weapons...")
    for weapon in WEAPONS:
        try:
            client.mutation("mutations:createWeapon", weapon.model_dump())
            print(f"  ✅ Added weapon: {weapon.name}")
        except Exception as e:
            print(f"  ❌ Failed to add weapon {weapon.name}: {e}")
    
    print("\n✨ Data population complete!")


def main():
    parser = argparse.ArgumentParser(description='Populate Convex database with TMNT data')
    parser.add_argument('--convex-url', type=str, help='Convex deployment URL')
    parser.add_argument('--env-file', type=str, default='.env.local', 
                       help='Path to env file containing CONVEX_URL')
    
    args = parser.parse_args()
    
    # Get Convex URL from args or environment
    convex_url = args.convex_url
    
    if not convex_url:
        # Try to load from env file
        if os.path.exists(args.env_file):
            from dotenv import load_dotenv
            load_dotenv(args.env_file)
            convex_url = os.environ.get('CONVEX_URL')
    
    if not convex_url:
        print("❌ Error: No Convex URL provided")
        print("Please provide either:")
        print("  1. --convex-url flag with your Convex deployment URL")
        print("  2. CONVEX_URL in your .env.local file")
        sys.exit(1)
    
    # Run the function
    populate_convex(convex_url)


if __name__ == "__main__":
    main()