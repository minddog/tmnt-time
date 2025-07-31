#!/bin/bash

# TMNT API Regression Test Suite
# Run before every deployment to Vercel
# Usage: ./regression-test-suite.sh [BASE_URL]

BASE_URL="${1:-https://vercel-python-nine-tau.vercel.app}"
FAILED_TESTS=0
TOTAL_TESTS=0
START_TIME=$(date +%s)

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Create test results directory
RESULTS_DIR="test-results-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$RESULTS_DIR"

log_test() {
    echo -e "${YELLOW}[TEST]${NC} $1"
    echo "[TEST] $1" >> "$RESULTS_DIR/test.log"
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
}

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    echo "[PASS] $1" >> "$RESULTS_DIR/test.log"
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    echo "[FAIL] $1" >> "$RESULTS_DIR/test.log"
    FAILED_TESTS=$((FAILED_TESTS + 1))
}

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
    echo "[INFO] $1" >> "$RESULTS_DIR/test.log"
}

# Test function with detailed response logging
test_endpoint() {
    local endpoint=$1
    local expected_status=$2
    local description=$3
    local additional_checks=$4
    
    log_test "$description"
    
    # Make request and capture timing
    local start_time=$(date +%s.%N)
    response=$(curl -s -w "\n%{http_code}\n%{time_total}" "$BASE_URL$endpoint" 2>/dev/null)
    local end_time=$(date +%s.%N)
    
    if [ $? -ne 0 ]; then
        log_fail "Curl request failed for $endpoint"
        echo "Curl error for $endpoint" >> "$RESULTS_DIR/errors.log"
        return 1
    fi
    
    # Parse response
    local body=$(echo "$response" | head -n -2)
    local status_code=$(echo "$response" | tail -n 2 | head -n 1)
    local curl_time=$(echo "$response" | tail -n 1)
    
    # Save response for debugging
    echo "=== $endpoint ===" >> "$RESULTS_DIR/responses.log"
    echo "Status: $status_code" >> "$RESULTS_DIR/responses.log"
    echo "Time: $curl_time" >> "$RESULTS_DIR/responses.log"
    echo "Body: $body" >> "$RESULTS_DIR/responses.log"
    echo "" >> "$RESULTS_DIR/responses.log"
    
    # Check status code
    if [ "$status_code" -eq "$expected_status" ]; then
        log_pass "Status $status_code for $endpoint (${curl_time}s)"
        
        # Additional checks if provided
        if [ -n "$additional_checks" ]; then
            eval "$additional_checks"
        fi
        
        return 0
    else
        log_fail "Expected $expected_status, got $status_code for $endpoint"
        echo "Status mismatch: $endpoint expected $expected_status got $status_code" >> "$RESULTS_DIR/errors.log"
        return 1
    fi
}

# Advanced test function with JSON validation
test_json_endpoint() {
    local endpoint=$1
    local expected_status=$2
    local description=$3
    local json_checks=$4
    
    log_test "$description"
    
    response=$(curl -s -w "\n%{http_code}" "$BASE_URL$endpoint" -H "Accept: application/json")
    status_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n -1)
    
    if [ "$status_code" -eq "$expected_status" ]; then
        # Validate JSON structure
        if echo "$body" | jq . >/dev/null 2>&1; then
            log_pass "Valid JSON response for $endpoint"
            
            # Run additional JSON checks
            if [ -n "$json_checks" ]; then
                if echo "$body" | jq -e "$json_checks" >/dev/null 2>&1; then
                    log_pass "JSON structure validation passed for $endpoint"
                else
                    log_fail "JSON structure validation failed for $endpoint"
                    echo "JSON validation failed: $endpoint - $json_checks" >> "$RESULTS_DIR/errors.log"
                    return 1
                fi
            fi
            return 0
        else
            log_fail "Invalid JSON response for $endpoint"
            echo "Invalid JSON: $endpoint" >> "$RESULTS_DIR/errors.log"
            return 1
        fi
    else
        log_fail "Expected $expected_status, got $status_code for $endpoint"
        return 1
    fi
}

# Test cache headers
test_cache_headers() {
    local endpoint=$1
    local expected_cache=$2
    local description=$3
    
    log_test "$description"
    
    headers=$(curl -sI "$BASE_URL$endpoint")
    cache_header=$(echo "$headers" | grep -i "cache-control" | tr -d '\r')
    
    if [[ $cache_header == *"$expected_cache"* ]]; then
        log_pass "Cache headers correct for $endpoint"
        return 0
    else
        log_fail "Cache headers incorrect for $endpoint. Expected: $expected_cache, Got: $cache_header"
        echo "Cache header mismatch: $endpoint" >> "$RESULTS_DIR/errors.log"
        return 1
    fi
}

echo "========================================="
echo "TMNT API Regression Test Suite"
echo "========================================="
echo "Base URL: $BASE_URL"
echo "Results Dir: $RESULTS_DIR"
echo "Start Time: $(date)"
echo "========================================="

# Test 1: Health and API Root
log_info "Testing core API endpoints..."
test_json_endpoint "/api/health" 200 "Health check endpoint" '.status == "healthy"'
test_json_endpoint "/api" 200 "API root documentation" '.message and .version and .endpoints'

# Test 2: Turtles endpoints
log_info "Testing turtle endpoints..."
test_json_endpoint "/api/v1/turtles" 200 "Get all turtles" 'length == 4'
test_json_endpoint "/api/v1/turtles/leonardo" 200 "Get Leonardo" '.name == "leonardo" and .color == "blue"'
test_json_endpoint "/api/v1/turtles/donatello" 200 "Get Donatello" '.name == "donatello" and .color == "purple"'
test_json_endpoint "/api/v1/turtles/raphael" 200 "Get Raphael" '.name == "raphael" and .color == "red"'
test_json_endpoint "/api/v1/turtles/michelangelo" 200 "Get Michelangelo" '.name == "michelangelo" and .color == "orange"'

# Test 3: Villains endpoints
log_info "Testing villain endpoints..."
test_json_endpoint "/api/v1/villains" 200 "Get all villains" 'length >= 5'
test_json_endpoint "/api/v1/villains/shredder" 200 "Get Shredder" '.name == "shredder"'
test_json_endpoint "/api/v1/villains/krang" 200 "Get Krang" '.name == "krang"'

# Test 4: Episodes endpoints
log_info "Testing episode endpoints..."
test_json_endpoint "/api/v1/episodes" 200 "Get episodes default" 'length <= 10'
test_json_endpoint "/api/v1/episodes?limit=5" 200 "Get episodes with limit" 'length <= 5'
test_json_endpoint "/api/v1/episodes?season=1" 200 "Get season 1 episodes" 'all(.season == 1)'

# Test 5: Quotes and weapons
log_info "Testing quotes and weapons..."
test_json_endpoint "/api/v1/quotes/random" 200 "Get random quote" '.text and .character'
test_json_endpoint "/api/v1/weapons" 200 "Get all weapons" 'length == 4'

# Test 6: Search functionality
log_info "Testing search functionality..."
test_json_endpoint "/api/v1/search?q=turtle" 200 "Search for turtle" '.turtles and .villains and .episodes and .quotes'
test_json_endpoint "/api/v1/search?q=leonardo" 200 "Search for leonardo" '.turtles | length >= 1'

# Test 7: Error cases
log_info "Testing error handling..."
test_endpoint "/api/v1/turtles/nonexistent" 404 "Non-existent turtle"
test_endpoint "/api/v1/villains/nonexistent" 404 "Non-existent villain"
test_endpoint "/api/v1/episodes/999999" 404 "Non-existent episode"
test_endpoint "/api/v1/search?q=a" 422 "Search query too short"

# Test 8: Input validation
log_info "Testing input validation..."
test_endpoint "/api/v1/episodes?limit=101" 422 "Pagination limit too high"
test_endpoint "/api/v1/episodes?limit=0" 422 "Pagination limit too low"
test_endpoint "/api/v1/episodes?offset=-1" 422 "Negative offset"
test_endpoint "/api/v1/episodes?season=0" 422 "Invalid season low"
test_endpoint "/api/v1/episodes?season=11" 422 "Invalid season high"

# Test 9: Cache headers
log_info "Testing cache headers..."
test_cache_headers "/api/v1/turtles" "s-maxage=3600" "Static content cache headers"
test_cache_headers "/api/v1/episodes" "s-maxage=60" "Dynamic content cache headers"
test_cache_headers "/api/v1/quotes/random" "no-cache" "No-cache headers"

# Test 10: Case sensitivity
log_info "Testing case sensitivity..."
test_json_endpoint "/api/v1/turtles/LEONARDO" 200 "Uppercase turtle name" '.name == "leonardo"'
test_json_endpoint "/api/v1/turtles/LeOnArDo" 200 "Mixed case turtle name" '.name == "leonardo"'

# Test 11: Performance checks
log_info "Running basic performance tests..."
endpoints_to_test=(
    "/api/health"
    "/api/v1/turtles"
    "/api/v1/villains"
    "/api/v1/episodes"
    "/api/v1/search?q=turtle"
)

for endpoint in "${endpoints_to_test[@]}"; do
    log_test "Performance test for $endpoint"
    
    times=()
    for i in {1..3}; do
        time=$(curl -s -w "%{time_total}" -o /dev/null "$BASE_URL$endpoint")
        times+=($time)
    done
    
    # Calculate average time
    avg_time=$(echo "${times[@]}" | awk '{sum=0; for(i=1;i<=NF;i++)sum+=$i; print sum/NF}')
    
    # Check if average time is reasonable (under 2 seconds)
    if (( $(echo "$avg_time < 2.0" | bc -l) )); then
        log_pass "Performance acceptable for $endpoint (avg: ${avg_time}s)"
    else
        log_fail "Performance slow for $endpoint (avg: ${avg_time}s)"
    fi
done

# Test 12: Random quote uniqueness test
log_info "Testing random quote uniqueness..."
quotes=()
for i in {1..5}; do
    quote=$(curl -s "$BASE_URL/api/v1/quotes/random" | jq -r '.text')
    quotes+=("$quote")
done

unique_count=$(printf '%s\n' "${quotes[@]}" | sort -u | wc -l)
if [ "$unique_count" -gt 1 ]; then
    log_pass "Random quotes showing variety ($unique_count unique out of 5)"
else
    log_fail "Random quotes not sufficiently random ($unique_count unique out of 5)"
fi

# Generate summary report
END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

echo "========================================="
echo "Test Results Summary"
echo "========================================="
echo "Test Suite: TMNT API Regression Tests"
echo "Base URL: $BASE_URL"
echo "Start Time: $(date -d @$START_TIME)"
echo "End Time: $(date -d @$END_TIME)"
echo "Duration: ${DURATION} seconds"
echo "Total Tests: $TOTAL_TESTS"
echo "Failed Tests: $FAILED_TESTS"
echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"
echo "Success Rate: $(echo "scale=2; ($TOTAL_TESTS - $FAILED_TESTS) * 100 / $TOTAL_TESTS" | bc)%"

# Save summary to file
{
    echo "TMNT API Test Summary - $(date)"
    echo "================================"
    echo "Base URL: $BASE_URL"
    echo "Total Tests: $TOTAL_TESTS"
    echo "Failed Tests: $FAILED_TESTS"
    echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"
    echo "Success Rate: $(echo "scale=2; ($TOTAL_TESTS - $FAILED_TESTS) * 100 / $TOTAL_TESTS" | bc)%"
    echo "Duration: ${DURATION} seconds"
} > "$RESULTS_DIR/summary.txt"

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}✅ All tests passed! API is ready for deployment.${NC}"
    exit 0
else
    echo -e "${RED}❌ $FAILED_TESTS test(s) failed! Check $RESULTS_DIR/errors.log for details.${NC}"
    echo -e "${YELLOW}Review failed tests before deploying to production.${NC}"
    exit 1
fi