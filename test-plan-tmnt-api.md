# TMNT API Comprehensive Test Plan & Regression Suite

## Risk Assessment Summary

### High-Risk Areas
1. **Edge Config Connectivity** - API depends entirely on Vercel Edge Config for data
2. **Cache Invalidation** - Multiple cache layers (CDN, Edge, Browser) could serve stale data
3. **Search Functionality** - Complex cross-collection search with potential performance impacts
4. **Pagination Logic** - Episodes endpoint with offset/limit parameters
5. **Error Handling** - Fallback mechanisms when Edge Config fails

### Medium-Risk Areas
1. **Random Quote Generation** - No-cache implementation for true randomness
2. **Case-Sensitive Name Lookups** - String normalization across different endpoints
3. **CORS Configuration** - Wide-open CORS policy needs validation

### Low-Risk Areas
1. **Static Data Models** - Well-defined Pydantic models
2. **Health Check** - Simple status endpoint
3. **API Documentation** - Static endpoint information

## Test Plan Structure

### Phase 1: Core Functionality Tests
**Objective**: Verify all endpoints return expected data structures and status codes
**Priority**: Critical
**Environment**: Production (https://vercel-python-nine-tau.vercel.app)

### Phase 2: Edge Cases & Error Scenarios
**Objective**: Test boundary conditions, invalid inputs, and error handling
**Priority**: High
**Environment**: Production + Staging (if available)

### Phase 3: Performance & Caching
**Objective**: Validate caching behavior, response times, and load handling
**Priority**: High
**Environment**: Production

### Phase 4: Security & CORS
**Objective**: Verify security headers, CORS policy, and data exposure
**Priority**: Medium
**Environment**: Production

### Phase 5: Regression Suite
**Objective**: Automated test suite for pre-deployment validation
**Priority**: Critical
**Environment**: Staging → Production

---

## Phase 1: Core Functionality Tests

### Test Suite 1.1: API Root & Health Endpoints

#### Test Case 1.1.1: API Root Endpoint
**Endpoint**: `GET /api`
**Expected**: 200 OK with API documentation
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\nTime: %{time_total}s\n"
```
**Validation**:
- Status: 200
- Content-Type: application/json
- Response includes: message, version, features, endpoints
- Cache-Control header: "public, s-maxage=3600"

#### Test Case 1.1.2: Health Check Endpoint
**Endpoint**: `GET /api/health`
**Expected**: 200 OK with health status
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/health" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\nTime: %{time_total}s\n"
```
**Validation**:
- Status: 200
- Response includes: status="healthy", service="TMNT API", edge_config, version
- Cache-Control header: "no-cache"

### Test Suite 1.2: Turtles Endpoints

#### Test Case 1.2.1: Get All Turtles
**Endpoint**: `GET /api/v1/turtles`
**Expected**: 200 OK with list of 4 turtles
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/turtles" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\nTime: %{time_total}s\n"
```
**Validation**:
- Status: 200
- Array length: 4
- Each turtle has: name, full_name, color, weapon, personality, favorite_pizza, catchphrase
- Cache headers present: "public, s-maxage=3600"

#### Test Case 1.2.2: Get Turtle by Name (Valid)
**Endpoint**: `GET /api/v1/turtles/{name}`
**Test Data**: leonardo, donatello, raphael, michelangelo
```bash
for turtle in leonardo donatello raphael michelangelo; do
  echo "Testing turtle: $turtle"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/turtles/$turtle" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\nTime: %{time_total}s\n\n"
done
```
**Validation**:
- Status: 200 for each
- Response matches Turtle model schema
- Name field matches request parameter (lowercase)

### Test Suite 1.3: Villains Endpoints

#### Test Case 1.3.1: Get All Villains
**Endpoint**: `GET /api/v1/villains`
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/villains" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\nTime: %{time_total}s\n"
```
**Validation**:
- Status: 200
- Array with multiple villains
- Each villain has: name, description, abilities (array), first_appearance

#### Test Case 1.3.2: Get Villain by Name (Valid)
**Endpoint**: `GET /api/v1/villains/{name}`
**Test Data**: shredder, krang, bebop, rocksteady
```bash
for villain in shredder krang bebop rocksteady; do
  echo "Testing villain: $villain"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/villains/$villain" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\nTime: %{time_total}s\n\n"
done
```

### Test Suite 1.4: Episodes Endpoints

#### Test Case 1.4.1: Get Episodes (No Parameters)
**Endpoint**: `GET /api/v1/episodes`
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\nTime: %{time_total}s\n"
```
**Validation**:
- Status: 200
- Default limit: 10 episodes
- Each episode has: id, title, season, episode_number, synopsis

#### Test Case 1.4.2: Get Episodes with Pagination
**Endpoint**: `GET /api/v1/episodes?limit={limit}&offset={offset}`
```bash
# Test different pagination scenarios
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?limit=5&offset=0" \
  -H "Accept: application/json" -w "\nStatus: %{http_code}\n"

curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?limit=3&offset=5" \
  -H "Accept: application/json" -w "\nStatus: %{http_code}\n"
```

#### Test Case 1.4.3: Get Episodes by Season
**Endpoint**: `GET /api/v1/episodes?season={season}`
```bash
for season in 1 2 3; do
  echo "Testing season: $season"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?season=$season" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\n\n"
done
```

### Test Suite 1.5: Quotes & Weapons Endpoints

#### Test Case 1.5.1: Get Random Quote
**Endpoint**: `GET /api/v1/quotes/random`
```bash
# Test multiple times to verify randomness
for i in {1..5}; do
  echo "Random quote test #$i:"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/quotes/random" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\n\n"
done
```
**Validation**:
- Status: 200
- Cache-Control: "no-cache, no-store, must-revalidate"
- Response has: id, text, character

#### Test Case 1.5.2: Get All Weapons
**Endpoint**: `GET /api/v1/weapons`
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/weapons" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\nTime: %{time_total}s\n"
```

### Test Suite 1.6: Search Functionality

#### Test Case 1.6.1: Search Across Collections
**Endpoint**: `GET /api/v1/search?q={query}`
```bash
# Test various search terms
for query in "turtle" "pizza" "shredder" "katana"; do
  echo "Searching for: $query"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/search?q=$query" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\n\n"
done
```
**Validation**:
- Status: 200
- Response contains: turtles, villains, episodes, quotes arrays
- Results are relevant to search query

---

## Phase 2: Edge Cases & Error Scenarios

### Test Suite 2.1: Invalid Inputs

#### Test Case 2.1.1: Non-existent Turtle
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/turtles/splinter" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```
**Expected**: 404 Not Found with error message

#### Test Case 2.1.2: Non-existent Villain
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/villains/batman" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```
**Expected**: 404 Not Found

#### Test Case 2.1.3: Invalid Episode ID
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes/999999" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```
**Expected**: 404 Not Found

### Test Suite 2.2: Boundary Testing

#### Test Case 2.2.1: Search Query Too Short
```bash
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/search?q=a" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```
**Expected**: 422 Validation Error

#### Test Case 2.2.2: Pagination Boundaries
```bash
# Test maximum limit
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?limit=101" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"

# Test negative offset
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?offset=-1" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"

# Test negative limit
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?limit=0" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```
**Expected**: 422 Validation Error for each

#### Test Case 2.2.3: Season Boundaries
```bash
# Test invalid season numbers
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?season=0" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"

curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/episodes?season=11" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```
**Expected**: 422 Validation Error

### Test Suite 2.3: Case Sensitivity & Special Characters

#### Test Case 2.3.1: Case Variations in Names
```bash
# Test different case variations
for name in "LEONARDO" "Leonardo" "LeOnArDo"; do
  echo "Testing case variation: $name"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/turtles/$name" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\n\n"
done
```
**Expected**: All should return 200 (API normalizes to lowercase)

#### Test Case 2.3.2: Special Characters in Search
```bash
# Test special characters and encoding
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/search?q=%20turtle%20" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"

curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/search?q=turtle%26pizza" \
  -H "Accept: application/json" \
  -w "\nStatus: %{http_code}\n"
```

---

## Phase 3: Performance & Caching Tests

### Test Suite 3.1: Cache Header Validation

#### Test Case 3.1.1: Static Content Caching
```bash
# Test cache headers on static endpoints
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/turtles"
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/villains"
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/weapons"
```
**Expected**: Cache-Control: "public, s-maxage=3600, stale-while-revalidate=86400"

#### Test Case 3.1.2: Dynamic Content Caching
```bash
# Test cache headers on dynamic endpoints
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/episodes"
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/search?q=turtle"
```
**Expected**: Cache-Control: "public, s-maxage=60, stale-while-revalidate=300"

#### Test Case 3.1.3: No-Cache Endpoints
```bash
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/quotes/random"
curl -I "https://vercel-python-nine-tau.vercel.app/api/health"
```
**Expected**: Cache-Control: "no-cache" or "no-cache, no-store, must-revalidate"

### Test Suite 3.2: Response Time Testing

#### Test Case 3.2.1: Cold Start Performance
```bash
# Test response times for different endpoints
endpoints=(
  "/api"
  "/api/health"
  "/api/v1/turtles"
  "/api/v1/villains"
  "/api/v1/episodes"
  "/api/v1/quotes/random"
  "/api/v1/search?q=turtle"
)

for endpoint in "${endpoints[@]}"; do
  echo "Testing performance for: $endpoint"
  curl -X GET "https://vercel-python-nine-tau.vercel.app$endpoint" \
    -H "Accept: application/json" \
    -w "Time: %{time_total}s, Size: %{size_download} bytes\n" \
    -o /dev/null -s
done
```
**Performance Thresholds**:
- Static endpoints: < 500ms
- Dynamic endpoints: < 1000ms
- Search endpoint: < 1500ms

### Test Suite 3.3: Load Testing

#### Test Case 3.3.1: Concurrent Requests
```bash
# Simple concurrent load test using xargs
echo "https://vercel-python-nine-tau.vercel.app/api/v1/turtles" | \
  xargs -I {} -P 10 -n 1 curl -s -o /dev/null -w "%{http_code} %{time_total}s\n" {}
```

---

## Phase 4: Security & CORS Tests

### Test Suite 4.1: CORS Validation

#### Test Case 4.1.1: Cross-Origin Requests
```bash
# Test CORS headers
curl -X OPTIONS "https://vercel-python-nine-tau.vercel.app/api/v1/turtles" \
  -H "Origin: https://example.com" \
  -H "Access-Control-Request-Method: GET" \
  -v

# Test from different origins
curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/turtles" \
  -H "Origin: https://malicious-site.com" \
  -v
```
**Expected**: CORS headers should allow all origins (verify this is intentional)

### Test Suite 4.2: Security Headers

#### Test Case 4.2.1: Response Headers Analysis
```bash
curl -I "https://vercel-python-nine-tau.vercel.app/api/v1/turtles"
```
**Check for**:
- No sensitive information in headers
- Appropriate content-type headers
- No server version disclosure

### Test Suite 4.3: Input Validation

#### Test Case 4.3.1: SQL Injection Attempts
```bash
# Test various injection patterns in search
injection_payloads=(
  "'; DROP TABLE--"
  "' OR '1'='1"
  "<script>alert('xss')</script>"
  "../../../etc/passwd"
)

for payload in "${injection_payloads[@]}"; do
  echo "Testing payload: $payload"
  curl -X GET "https://vercel-python-nine-tau.vercel.app/api/v1/search?q=$(echo -n "$payload" | jq -sRr @uri)" \
    -H "Accept: application/json" \
    -w "\nStatus: %{http_code}\n\n"
done
```

---

## Phase 5: Regression Test Suite

### Automated Test Script: `regression-test-suite.sh`

```bash
#!/bin/bash

# TMNT API Regression Test Suite
# Run before every deployment to Vercel

BASE_URL="https://vercel-python-nine-tau.vercel.app"
FAILED_TESTS=0
TOTAL_TESTS=0

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_test() {
    echo -e "${YELLOW}[TEST]${NC} $1"
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
}

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    FAILED_TESTS=$((FAILED_TESTS + 1))
}

# Test function template
test_endpoint() {
    local endpoint=$1
    local expected_status=$2
    local description=$3
    
    log_test "$description"
    
    response=$(curl -s -w "\n%{http_code}" "$BASE_URL$endpoint")
    status_code=$(echo "$response" | tail -n1)
    body=$(echo "$response" | head -n -1)
    
    if [ "$status_code" -eq "$expected_status" ]; then
        log_pass "Status $status_code for $endpoint"
        return 0
    else
        log_fail "Expected $expected_status, got $status_code for $endpoint"
        return 1
    fi
}

# Critical Path Tests
echo "========================================="
echo "TMNT API Regression Test Suite"
echo "========================================="

# Health check
test_endpoint "/api/health" 200 "Health check endpoint"

# API root
test_endpoint "/api" 200 "API root documentation"

# Core endpoints
test_endpoint "/api/v1/turtles" 200 "Get all turtles"
test_endpoint "/api/v1/turtles/leonardo" 200 "Get turtle by name"
test_endpoint "/api/v1/villains" 200 "Get all villains"
test_endpoint "/api/v1/villains/shredder" 200 "Get villain by name"
test_endpoint "/api/v1/episodes" 200 "Get episodes"
test_endpoint "/api/v1/quotes/random" 200 "Get random quote"
test_endpoint "/api/v1/weapons" 200 "Get all weapons"
test_endpoint "/api/v1/search?q=turtle" 200 "Search functionality"

# Error cases
test_endpoint "/api/v1/turtles/nonexistent" 404 "Non-existent turtle"
test_endpoint "/api/v1/villains/nonexistent" 404 "Non-existent villain"
test_endpoint "/api/v1/search?q=a" 422 "Search query too short"

# Pagination validation
test_endpoint "/api/v1/episodes?limit=5&offset=0" 200 "Pagination with valid params"
test_endpoint "/api/v1/episodes?limit=101" 422 "Pagination with invalid limit"

echo "========================================="
echo "Test Results Summary"
echo "========================================="
echo "Total Tests: $TOTAL_TESTS"
echo "Failed Tests: $FAILED_TESTS"
echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}All tests passed! ✅${NC}"
    exit 0
else
    echo -e "${RED}$FAILED_TESTS test(s) failed! ❌${NC}"
    exit 1
fi
```

### Continuous Integration Test Script: `ci-integration-tests.sh`

```bash
#!/bin/bash

# Extended CI tests for integration scenarios
BASE_URL="https://vercel-python-nine-tau.vercel.app"

echo "Running Integration Tests..."

# Test 1: Data Consistency Across Endpoints
echo "Testing data consistency..."
turtle_count=$(curl -s "$BASE_URL/api/v1/turtles" | jq '. | length')
weapon_count=$(curl -s "$BASE_URL/api/v1/weapons" | jq '. | length')

if [ "$turtle_count" -eq "$weapon_count" ]; then
    echo "✅ Turtle-Weapon consistency check passed"
else
    echo "❌ Turtle-Weapon count mismatch: $turtle_count turtles, $weapon_count weapons"
fi

# Test 2: Search Result Validation
echo "Testing search result integrity..."
search_results=$(curl -s "$BASE_URL/api/v1/search?q=leonardo")
turtle_found=$(echo "$search_results" | jq '.turtles | length')

if [ "$turtle_found" -gt 0 ]; then
    echo "✅ Search finds relevant turtle data"
else
    echo "❌ Search failed to find expected turtle data"
fi

# Test 3: Cache Behavior Validation
echo "Testing cache headers..."
cache_header=$(curl -sI "$BASE_URL/api/v1/turtles" | grep -i "cache-control")
if [[ $cache_header == *"s-maxage=3600"* ]]; then
    echo "✅ Cache headers correctly set"
else
    echo "❌ Cache headers missing or incorrect: $cache_header"
fi

# Test 4: Random Quote Uniqueness
echo "Testing random quote uniqueness..."
quote1=$(curl -s "$BASE_URL/api/v1/quotes/random" | jq -r '.text')
quote2=$(curl -s "$BASE_URL/api/v1/quotes/random" | jq -r '.text')
quote3=$(curl -s "$BASE_URL/api/v1/quotes/random" | jq -r '.text')

unique_quotes=$(echo -e "$quote1\n$quote2\n$quote3" | sort -u | wc -l)
if [ "$unique_quotes" -gt 1 ]; then
    echo "✅ Random quotes showing variety"
else
    echo "⚠️  Random quotes may not be sufficiently random"
fi

echo "Integration tests completed."
```

---

## Test Data Requirements

### Test Environment Setup
1. **Production URL**: https://vercel-python-nine-tau.vercel.app
2. **Required Tools**: curl, jq, bash
3. **Optional Tools**: Apache Bench (ab), wrk for load testing

### Expected Test Data
- **Turtles**: 4 entries (leonardo, donatello, raphael, michelangelo)
- **Villains**: Multiple entries including shredder, krang
- **Episodes**: Multiple episodes with seasons 1-10
- **Quotes**: 8+ quotes from various characters
- **Weapons**: 4 weapons corresponding to turtles

---

## Automation & CI/CD Integration

### Pre-Deployment Checklist
1. Run regression test suite
2. Validate cache headers
3. Test error handling
4. Verify search functionality
5. Check performance thresholds

### Post-Deployment Validation
1. Health check verification
2. Sample data validation
3. Performance baseline comparison
4. Error rate monitoring

### Monitoring & Alerts
- Set up synthetic monitoring for critical endpoints
- Monitor error rates and response times
- Alert on cache miss ratios
- Track search query performance

---

## Test Maintenance

### Regular Review Schedule
- **Weekly**: Run full regression suite
- **Monthly**: Performance baseline review
- **Quarterly**: Security test updates
- **Release-based**: Update test data expectations

### Test Coverage Metrics
- Endpoint coverage: 100%
- Error scenario coverage: 90%
- Performance test coverage: 80%
- Security test coverage: 70%

This comprehensive test plan ensures the TMNT API maintains high quality and reliability when deployed to Vercel, with particular attention to the Edge Config dependency and caching strategies.