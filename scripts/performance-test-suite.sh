#!/bin/bash

# TMNT API Performance Test Suite
# Focused on response times, concurrent load, and cache effectiveness
# Usage: ./performance-test-suite.sh [BASE_URL] [CONCURRENT_USERS]

BASE_URL="${1:-https://vercel-python-nine-tau.vercel.app}"
CONCURRENT_USERS="${2:-10}"
REQUESTS_PER_USER=5
RESULTS_DIR="performance-results-$(date +%Y%m%d-%H%M%S)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

mkdir -p "$RESULTS_DIR"

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
    echo "[INFO] $1" >> "$RESULTS_DIR/performance.log"
}

log_perf() {
    echo -e "${YELLOW}[PERF]${NC} $1"
    echo "[PERF] $1" >> "$RESULTS_DIR/performance.log"
}

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    echo "[PASS] $1" >> "$RESULTS_DIR/performance.log"
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    echo "[FAIL] $1" >> "$RESULTS_DIR/performance.log"
}

# Function to test single endpoint performance
test_endpoint_performance() {
    local endpoint=$1
    local description=$2
    local threshold=$3
    
    log_perf "Testing $description..."
    
    local times=()
    local statuses=()
    
    # Run 10 requests to get average
    for i in {1..10}; do
        response=$(curl -s -w "%{time_total}:%{http_code}" -o /dev/null "$BASE_URL$endpoint")
        time=$(echo "$response" | cut -d: -f1)
        status=$(echo "$response" | cut -d: -f2)
        
        times+=($time)
        statuses+=($status)
    done
    
    # Calculate statistics
    avg_time=$(printf '%s\n' "${times[@]}" | awk '{sum+=$1} END {print sum/NR}')
    min_time=$(printf '%s\n' "${times[@]}" | sort -n | head -1)
    max_time=$(printf '%s\n' "${times[@]}" | sort -n | tail -1)
    
    # Check success rate
    success_count=0
    for status in "${statuses[@]}"; do
        if [ "$status" -eq 200 ]; then
            success_count=$((success_count + 1))
        fi
    done
    success_rate=$((success_count * 100 / 10))
    
    # Log results
    echo "Endpoint: $endpoint" >> "$RESULTS_DIR/performance_details.log"
    echo "Average: ${avg_time}s, Min: ${min_time}s, Max: ${max_time}s" >> "$RESULTS_DIR/performance_details.log" 
    echo "Success Rate: ${success_rate}%" >> "$RESULTS_DIR/performance_details.log"
    echo "---" >> "$RESULTS_DIR/performance_details.log"
    
    # Check against threshold
    if (( $(echo "$avg_time < $threshold" | bc -l) )) && [ "$success_rate" -eq 100 ]; then
        log_pass "$description: Avg ${avg_time}s (threshold: ${threshold}s), Success: ${success_rate}%"
        return 0
    else
        log_fail "$description: Avg ${avg_time}s (threshold: ${threshold}s), Success: ${success_rate}%"
        return 1
    fi
}

# Function to test concurrent load
test_concurrent_load() {
    local endpoint=$1
    local description=$2
    local users=$3
    local requests=$4
    
    log_perf "Testing concurrent load: $description ($users users, $requests requests each)..."
    
    # Create temp file for storing results
    local temp_file=$(mktemp)
    
    # Function to run requests for one user
    run_user_requests() {
        local user_id=$1
        local results_file=$2
        
        for ((r=1; r<=requests; r++)); do
            start_time=$(date +%s.%N)
            response=$(curl -s -w "%{http_code}" -o /dev/null "$BASE_URL$endpoint")
            end_time=$(date +%s.%N)
            
            duration=$(echo "$end_time - $start_time" | bc)
            echo "$user_id,$r,$duration,$response" >> "$results_file"
        done
    }
    
    # Start concurrent users
    start_time=$(date +%s.%N)
    for ((u=1; u<=users; u++)); do
        run_user_requests "$u" "$temp_file" &
    done
    
    # Wait for all background jobs to complete
    wait
    end_time=$(date +%s.%N)
    
    total_time=$(echo "$end_time - $start_time" | bc)
    
    # Analyze results
    total_requests=$(wc -l < "$temp_file")
    successful_requests=$(grep ",200$" "$temp_file" | wc -l)
    failed_requests=$((total_requests - successful_requests))
    
    avg_response_time=$(awk -F, '{sum+=$3} END {print sum/NR}' "$temp_file")
    min_response_time=$(awk -F, '{print $3}' "$temp_file" | sort -n | head -1)
    max_response_time=$(awk -F, '{print $3}' "$temp_file" | sort -n | tail -1)
    
    requests_per_second=$(echo "scale=2; $total_requests / $total_time" | bc)
    success_rate=$(echo "scale=2; $successful_requests * 100 / $total_requests" | bc)
    
    # Log detailed results
    {
        echo "=== Concurrent Load Test: $description ==="
        echo "Users: $users"
        echo "Requests per user: $requests"
        echo "Total requests: $total_requests"
        echo "Total time: ${total_time}s"
        echo "Successful requests: $successful_requests"
        echo "Failed requests: $failed_requests"
        echo "Success rate: ${success_rate}%"
        echo "Requests per second: $requests_per_second"
        echo "Avg response time: ${avg_response_time}s"
        echo "Min response time: ${min_response_time}s"
        echo "Max response time: ${max_response_time}s"
        echo ""
    } >> "$RESULTS_DIR/load_test_details.log"
    
    # Summary
    log_perf "$description Results:"
    log_perf "  Total Requests: $total_requests"
    log_perf "  Success Rate: ${success_rate}%"
    log_perf "  Requests/sec: $requests_per_second"
    log_perf "  Avg Response: ${avg_response_time}s"
    
    # Cleanup
    rm "$temp_file"
    
    # Pass/fail criteria
    if (( $(echo "$success_rate >= 95" | bc -l) )) && (( $(echo "$avg_response_time < 2.0" | bc -l) )); then
        log_pass "$description load test passed"
        return 0
    else
        log_fail "$description load test failed"
        return 1
    fi
}

# Function to test cache effectiveness
test_cache_effectiveness() {
    local endpoint=$1
    local description=$2
    
    log_perf "Testing cache effectiveness for $description..."
    
    # First request (cache miss)
    first_time=$(curl -s -w "%{time_total}" -o /dev/null "$BASE_URL$endpoint")
    
    # Wait a moment
    sleep 1
    
    # Second request (should be cached)
    second_time=$(curl -s -w "%{time_total}" -o /dev/null "$BASE_URL$endpoint")
    
    # Third request (should still be cached)
    third_time=$(curl -s -w "%{time_total}" -o /dev/null "$BASE_URL$endpoint")
    
    # Check if subsequent requests are faster (indicating cache hit)
    improvement_2nd=$(echo "scale=2; ($first_time - $second_time) / $first_time * 100" | bc)
    improvement_3rd=$(echo "scale=2; ($first_time - $third_time) / $first_time * 100" | bc)
    
    log_perf "$description Cache Test:"
    log_perf "  1st request: ${first_time}s"
    log_perf "  2nd request: ${second_time}s (${improvement_2nd}% improvement)"
    log_perf "  3rd request: ${third_time}s (${improvement_3rd}% improvement)"
    
    # Log to file
    {
        echo "Cache Test: $description"
        echo "1st: ${first_time}s, 2nd: ${second_time}s, 3rd: ${third_time}s"
        echo "Improvement: 2nd=${improvement_2nd}%, 3rd=${improvement_3rd}%"
        echo "---"
    } >> "$RESULTS_DIR/cache_test_details.log"
    
    # Cache is effective if 2nd and 3rd requests are faster
    if (( $(echo "$second_time < $first_time" | bc -l) )) && (( $(echo "$third_time < $first_time" | bc -l) )); then
        log_pass "$description cache is effective"
        return 0
    else
        log_fail "$description cache may not be working optimally"
        return 1
    fi
}

echo "========================================="
echo "TMNT API Performance Test Suite"
echo "========================================="
echo "Base URL: $BASE_URL"
echo "Concurrent Users: $CONCURRENT_USERS"
echo "Requests per User: $REQUESTS_PER_USER"
echo "Results Dir: $RESULTS_DIR"
echo "Start Time: $(date)"
echo "========================================="

FAILED_TESTS=0
TOTAL_TESTS=0

# Single endpoint performance tests
log_info "Running single endpoint performance tests..."

endpoints=(
    "/api/health:Health Check:0.5"
    "/api:API Root:0.8"
    "/api/v1/turtles:Get All Turtles:1.0"
    "/api/v1/turtles/leonardo:Get Turtle by Name:1.0"
    "/api/v1/villains:Get All Villains:1.2"
    "/api/v1/villains/shredder:Get Villain by Name:1.0"
    "/api/v1/episodes:Get Episodes:1.5"
    "/api/v1/quotes/random:Random Quote:1.0"
    "/api/v1/weapons:Get Weapons:1.0"
    "/api/v1/search?q=turtle:Search Functionality:1.8"
)

for endpoint_info in "${endpoints[@]}"; do
    IFS=':' read -r endpoint description threshold <<< "$endpoint_info"
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if ! test_endpoint_performance "$endpoint" "$description" "$threshold"; then
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
done

# Concurrent load tests
log_info "Running concurrent load tests..."

load_test_endpoints=(
    "/api/v1/turtles:Turtles Endpoint"
    "/api/v1/villains:Villains Endpoint"
    "/api/v1/episodes:Episodes Endpoint"
    "/api/v1/search?q=ninja:Search Endpoint"
)

for endpoint_info in "${load_test_endpoints[@]}"; do
    IFS=':' read -r endpoint description <<< "$endpoint_info"
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if ! test_concurrent_load "$endpoint" "$description" "$CONCURRENT_USERS" "$REQUESTS_PER_USER"; then
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
done

# Cache effectiveness tests
log_info "Running cache effectiveness tests..."

cache_test_endpoints=(
    "/api/v1/turtles:Static Turtle Data"
    "/api/v1/villains:Static Villain Data"
    "/api/v1/weapons:Static Weapon Data"
    "/api/v1/episodes:Dynamic Episode Data"
)

for endpoint_info in "${cache_test_endpoints[@]}"; do
    IFS=':' read -r endpoint description <<< "$endpoint_info"
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    if ! test_cache_effectiveness "$endpoint" "$description"; then
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi
done

# Network latency test
log_info "Running network latency analysis..."
latency_results=()
for i in {1..10}; do
    latency=$(curl -s -w "%{time_namelookup}:%{time_connect}:%{time_starttransfer}:%{time_total}" -o /dev/null "$BASE_URL/api/health")
    latency_results+=("$latency")
done

# Analyze latency components
{
    echo "=== Network Latency Analysis ==="
    echo "Sample latencies (DNS:Connect:FirstByte:Total):"
    printf '%s\n' "${latency_results[@]}"
    echo ""
} >> "$RESULTS_DIR/latency_analysis.log"

# Generate performance summary
{
    echo "TMNT API Performance Test Summary - $(date)"
    echo "==========================================="
    echo "Base URL: $BASE_URL"
    echo "Concurrent Users: $CONCURRENT_USERS"
    echo "Total Tests: $TOTAL_TESTS"
    echo "Failed Tests: $FAILED_TESTS"
    echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"
    echo "Success Rate: $(echo "scale=2; ($TOTAL_TESTS - $FAILED_TESTS) * 100 / $TOTAL_TESTS" | bc)%"
    echo ""
    echo "Key Metrics:"
    echo "- All static endpoints should respond under 1s"
    echo "- Search functionality should respond under 1.8s"  
    echo "- Concurrent load should maintain >95% success rate"
    echo "- Cache should improve response times for static content"
    echo ""
    echo "Files Generated:"
    echo "- performance_details.log: Individual endpoint metrics"
    echo "- load_test_details.log: Concurrent load test results"
    echo "- cache_test_details.log: Cache effectiveness analysis"
    echo "- latency_analysis.log: Network latency breakdown"
} > "$RESULTS_DIR/performance_summary.txt"

echo "========================================="
echo "Performance Test Results Summary"
echo "========================================="
echo "Total Tests: $TOTAL_TESTS"
echo "Failed Tests: $FAILED_TESTS"
echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"
echo "Success Rate: $(echo "scale=2; ($TOTAL_TESTS - FAILED_TESTS) * 100 / $TOTAL_TESTS" | bc)%"

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}✅ All performance tests passed!${NC}"
    echo -e "${GREEN}API performance is within acceptable thresholds.${NC}"
    exit 0
else
    echo -e "${RED}❌ $FAILED_TESTS performance test(s) failed!${NC}"
    echo -e "${YELLOW}Review performance metrics in $RESULTS_DIR/ for optimization opportunities.${NC}"
    exit 1
fi