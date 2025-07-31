#!/usr/bin/env python3
"""
Script to populate Vercel Edge Config with TMNT data
"""
import os
import json
import sys
from api.data.tmnt_data import TURTLES, VILLAINS, WEAPONS, QUOTES, EPISODES

def main():
    print("Preparing TMNT data for Edge Config...")
    
    # Convert data to JSON-serializable format
    data = {
        "turtles": {k: v.dict() for k, v in TURTLES.items()},
        "villains": {k: v.dict() for k, v in VILLAINS.items()},
        "weapons": [w.dict() for w in WEAPONS],
        "quotes": [q.dict() for q in QUOTES],
        "episodes": [e.dict() for e in EPISODES]
    }
    
    # Write to file for manual upload
    with open('edge_config_data.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    print("Data written to edge_config_data.json")
    print("\nTo update Edge Config:")
    print("1. Go to https://vercel.com/aballais-projects/vercel-python/stores")
    print("2. Click on your Edge Config store")
    print("3. Click 'Edit' and paste the contents of edge_config_data.json")
    print("4. Save the changes")
    
    # Show a preview of the data
    print("\nData preview:")
    print(f"- Turtles: {list(data['turtles'].keys())}")
    print(f"- Villains: {list(data['villains'].keys())}")
    print(f"- Weapons: {len(data['weapons'])} items")
    print(f"- Quotes: {len(data['quotes'])} items")
    print(f"- Episodes: {len(data['episodes'])} items")

if __name__ == "__main__":
    main()