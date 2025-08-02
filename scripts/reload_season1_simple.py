#!/usr/bin/env python3
"""
Simple script to reload Season 1 episodes
Works by attempting to add each episode (will skip if already exists)
"""

import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from dotenv import load_dotenv

# Load environment variables from .env.local for development database
load_dotenv('.env.local')

# Now run the add_all_episodes script with just Season 1
from api.data.episodes import SEASON1_EPISODES
from scripts.add_all_episodes import add_all_episodes

def main():
    """Main function"""
    print("Reloading Season 1 episodes...")
    print("=" * 60)
    
    # Run the add_all_episodes function with just Season 1 episodes
    # Use live mode (not dry run)
    add_all_episodes(dry_run=False, episodes_to_process=SEASON1_EPISODES)

if __name__ == "__main__":
    main()