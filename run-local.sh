#!/bin/bash

# TMNT API Local Development Server

echo "🐢 Starting TMNT API Local Development Server..."

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

# Run the Python script
python3 run_local.py