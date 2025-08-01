#!/usr/bin/env python3
"""
Script to clear all data from Convex database
"""
import os
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from convex import ConvexClient
import argparse


def clear_convex(convex_url: str):
    """Clear all data from Convex database"""
    client = ConvexClient(convex_url)
    
    print("🗑️  Clearing all data from Convex...")
    
    try:
        result = client.mutation("mutations:clearAllData")
        print("✅ All data cleared successfully!")
        print(f"   {result}")
    except Exception as e:
        print(f"❌ Failed to clear data: {e}")


def main():
    parser = argparse.ArgumentParser(description='Clear all data from Convex database')
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
    
    # Confirm before clearing
    response = input("⚠️  Are you sure you want to clear ALL data? (yes/no): ")
    if response.lower() != 'yes':
        print("Cancelled.")
        sys.exit(0)
    
    # Run the function
    clear_convex(convex_url)


if __name__ == "__main__":
    main()