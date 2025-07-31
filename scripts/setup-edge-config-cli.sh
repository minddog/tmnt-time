#!/bin/bash

# TMNT Edge Config Setup Script
# This script helps you set up Edge Config step by step

echo "🐢 TMNT Edge Config Setup"
echo "========================="
echo ""

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "❌ Vercel CLI is not installed!"
    echo "Please install it first: npm i -g vercel"
    exit 1
fi

# Check if user is logged in
if ! vercel whoami &> /dev/null; then
    echo "❌ You're not logged in to Vercel!"
    echo "Please run: vercel login"
    exit 1
fi

echo "✅ Vercel CLI is installed and you're logged in"
echo ""

# Get user input
echo "📝 Please provide the following information:"
echo ""

read -p "1. Vercel API Token (create at https://vercel.com/account/tokens): " VERCEL_TOKEN
echo ""

read -p "2. Do you already have an Edge Config? (y/n): " HAS_EDGE_CONFIG

if [ "$HAS_EDGE_CONFIG" = "y" ] || [ "$HAS_EDGE_CONFIG" = "Y" ]; then
    read -p "3. Enter your Edge Config ID (from the URL, e.g., ecfg_xxx): " EDGE_CONFIG_ID
else
    echo "3. We'll create a new Edge Config for you"
    EDGE_CONFIG_ID=""
fi

echo ""
read -p "4. Are you using a team account? (y/n): " IS_TEAM

if [ "$IS_TEAM" = "y" ] || [ "$IS_TEAM" = "Y" ]; then
    read -p "5. Enter your Team ID: " VERCEL_TEAM_ID
else
    VERCEL_TEAM_ID=""
fi

echo ""
echo "🔄 Setting up Edge Config..."
echo ""

# Create .env file for local development
cat > .env.edge-config << EOF
# Vercel Edge Config Environment Variables
# Add these to your Vercel project settings
VERCEL_TOKEN=$VERCEL_TOKEN
EDGE_CONFIG_ID=$EDGE_CONFIG_ID
VERCEL_TEAM_ID=$VERCEL_TEAM_ID
EOF

# Run the hydration script
if [ -n "$EDGE_CONFIG_ID" ]; then
    echo "🚀 Hydrating Edge Config with TMNT data..."
    VERCEL_TOKEN=$VERCEL_TOKEN EDGE_CONFIG_ID=$EDGE_CONFIG_ID VERCEL_TEAM_ID=$VERCEL_TEAM_ID node scripts/hydrate-edge-config.js
else
    echo "⚠️  No Edge Config ID provided. Please:"
    echo "1. Go to https://vercel.com/dashboard/stores"
    echo "2. Create a new Edge Config"
    echo "3. Copy the Edge Config ID from the URL"
    echo "4. Run: VERCEL_TOKEN=$VERCEL_TOKEN EDGE_CONFIG_ID=<your-id> node scripts/hydrate-edge-config.js"
fi

echo ""
echo "📋 Next Steps:"
echo "1. Link Edge Config to your project in Vercel dashboard"
echo "2. Deploy your project: vercel --prod"
echo "3. Test the API: curl https://your-domain.vercel.app/api/health"