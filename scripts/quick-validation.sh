#!/bin/bash

# Quick validation script to test API endpoints
# Usage: ./quick-validation.sh [BASE_URL]

BASE_URL="${1:-https://vercel-python-nine-tau.vercel.app}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

echo "Quick TMNT API Validation"
echo "========================="
echo "Base URL: $BASE_URL"
echo ""

# Test core endpoints
endpoints=(
    "/api:API Root"
    "/api/health:Health Check"
    "/api/v1/turtles:All Turtles"
    "/api/v1/turtles/leonardo:Leonardo"
    "/api/v1/villains:All Villains"
    "/api/v1/episodes:Episodes"
    "/api/v1/quotes/random:Random Quote"
    "/api/v1/weapons:Weapons"
    "/api/v1/search?q=turtle:Search"
)

failed=0
total=0

for endpoint_info in "${endpoints[@]}"; do
    IFS=':' read -r endpoint description <<< "$endpoint_info"
    total=$((total + 1))
    
    printf "Testing %-20s: " "$description"
    
    status=$(curl -s -w "%{http_code}" -o /dev/null "$BASE_URL$endpoint" --max-time 10)
    
    if [ "$status" -eq 200 ]; then
        echo -e "${GREEN}✓ PASS${NC} ($status)"
    else
        echo -e "${RED}✗ FAIL${NC} ($status)"
        failed=$((failed + 1))
    fi
done

echo ""
echo "Results: $((total - failed))/$total tests passed"

if [ $failed -eq 0 ]; then
    echo -e "${GREEN}All endpoints are responding correctly!${NC}"
    exit 0
else
    echo -e "${RED}$failed endpoint(s) failed!${NC}"
    exit 1
fi