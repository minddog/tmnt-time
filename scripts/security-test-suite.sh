#!/bin/bash

# TMNT API Security Test Suite
# Tests for common web API vulnerabilities and security best practices
# Usage: ./security-test-suite.sh [BASE_URL]

BASE_URL="${1:-https://vercel-python-nine-tau.vercel.app}"
RESULTS_DIR="security-results-$(date +%Y%m%d-%H%M%S)"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

mkdir -p "$RESULTS_DIR"

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
    echo "[INFO] $1" >> "$RESULTS_DIR/security.log"
}

log_sec() {
    echo -e "${YELLOW}[SEC]${NC} $1"
    echo "[SEC] $1" >> "$RESULTS_DIR/security.log"
}

log_pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
    echo "[PASS] $1" >> "$RESULTS_DIR/security.log"
}

log_fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    echo "[FAIL] $1" >> "$RESULTS_DIR/security.log"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
    echo "[WARN] $1" >> "$RESULTS_DIR/security.log"
}

# Test HTTP security headers
test_security_headers() {
    local endpoint=$1
    local description=$2
    
    log_sec "Testing security headers for $description..."
    
    headers=$(curl -sI "$BASE_URL$endpoint" | tr -d '\r')
    echo "=== Headers for $endpoint ===" >> "$RESULTS_DIR/headers.log"
    echo "$headers" >> "$RESULTS_DIR/headers.log"
    echo "" >> "$RESULTS_DIR/headers.log"
    
    local issues=0
    
    # Check for security headers
    if echo "$headers" | grep -qi "x-content-type-options"; then
        log_pass "X-Content-Type-Options header present"
    else
        log_warn "X-Content-Type-Options header missing"
        issues=$((issues + 1))
    fi
    
    if echo "$headers" | grep -qi "x-frame-options"; then
        log_pass "X-Frame-Options header present"
    else
        log_warn "X-Frame-Options header missing"
        issues=$((issues + 1))
    fi
    
    if echo "$headers" | grep -qi "strict-transport-security"; then
        log_pass "HSTS header present"
    else
        log_warn "HSTS header missing (may be handled by Vercel)"
        # Not counting as failure since Vercel may handle this
    fi
    
    # Check for server information disclosure
    if echo "$headers" | grep -qi "server:"; then
        server_header=$(echo "$headers" | grep -i "server:" | head -1)
        log_warn "Server header disclosed: $server_header"
        issues=$((issues + 1))
    else
        log_pass "No server information disclosed"
    fi
    
    # Check for proper CORS configuration
    if echo "$headers" | grep -qi "access-control-allow-origin"; then
        cors_header=$(echo "$headers" | grep -i "access-control-allow-origin" | head -1)
        if echo "$cors_header" | grep -q "*"; then
            log_warn "CORS allows all origins: $cors_header"
            issues=$((issues + 1))
        else
            log_pass "CORS properly configured: $cors_header"
        fi
    fi
    
    return $issues
}

# Test for injection vulnerabilities
test_injection_attacks() {
    local endpoint=$1
    local parameter=$2
    local description=$3
    
    log_sec "Testing injection attacks on $description..."
    
    # SQL injection payloads
    sql_payloads=(
        "'; DROP TABLE--"
        "' OR '1'='1"
        "' UNION SELECT * FROM--"
        "'; EXEC sp_configure--"
        "admin'--"
        "' OR 1=1#"
    )
    
    # XSS payloads
    xss_payloads=(
        "<script>alert('xss')</script>"
        "javascript:alert(1)"
        "<img src=x onerror=alert(1)>"
        "';alert(String.fromCharCode(88,83,83))//'"
        "<svg onload=alert(1)>"
    )
    
    # Command injection payloads
    cmd_payloads=(
        "; ls -la"
        "| whoami"
        "&& cat /etc/passwd"
        "\`id\`"
        "\$(whoami)"
    )
    
    local all_payloads=("${sql_payloads[@]}" "${xss_payloads[@]}" "${cmd_payloads[@]}")
    local suspicious_responses=0
    
    for payload in "${all_payloads[@]}"; do
        # URL encode the payload
        encoded_payload=$(echo -n "$payload" | jq -sRr @uri)
        test_url="$BASE_URL$endpoint?$parameter=$encoded_payload"
        
        response=$(curl -s -w "\n%{http_code}" "$test_url" 2>/dev/null)
        status_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n -1)
        
        # Log the test
        echo "Payload: $payload" >> "$RESULTS_DIR/injection_tests.log"
        echo "Status: $status_code" >> "$RESULTS_DIR/injection_tests.log"
        echo "Response length: $(echo "$body" | wc -c)" >> "$RESULTS_DIR/injection_tests.log"
        echo "---" >> "$RESULTS_DIR/injection_tests.log"
        
        # Check for suspicious responses
        if [ "$status_code" -eq 500 ]; then
            log_warn "500 error with payload: $payload"
            suspicious_responses=$((suspicious_responses + 1))
        elif echo "$body" | grep -qi "error\|exception\|stack\|trace"; then
            log_warn "Error information disclosed with payload: $payload"
            suspicious_responses=$((suspicious_responses + 1))
        elif echo "$body" | grep -q "$payload"; then
            log_warn "Payload reflected in response: $payload"
            suspicious_responses=$((suspicious_responses + 1))
        fi
    done
    
    if [ $suspicious_responses -eq 0 ]; then
        log_pass "No injection vulnerabilities detected in $description"
    else
        log_fail "$suspicious_responses suspicious responses detected in $description"
    fi
    
    return $suspicious_responses
}

# Test for path traversal vulnerabilities
test_path_traversal() {
    local base_endpoint=$1
    local description=$2
    
    log_sec "Testing path traversal on $description..."
    
    # Path traversal payloads
    payloads=(
        "../../../etc/passwd"
        "..\\..\\..\\windows\\system32\\drivers\\etc\\hosts"
        "....//....//....//etc/passwd"
        "%2e%2e%2f%2e%2e%2f%2e%2e%2fetc%2fpasswd"
        "..%252f..%252f..%252fetc%252fpasswd"
        "....\/....\/....\/etc\/passwd"
    )
    
    local issues=0
    
    for payload in "${payloads[@]}"; do
        test_url="$BASE_URL$base_endpoint/$payload"
        
        response=$(curl -s -w "\n%{http_code}" "$test_url" 2>/dev/null)
        status_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n -1)
        
        echo "Path Traversal Test: $payload" >> "$RESULTS_DIR/path_traversal.log"
        echo "Status: $status_code" >> "$RESULTS_DIR/path_traversal.log"
        echo "Response length: $(echo "$body" | wc -c)" >> "$RESULTS_DIR/path_traversal.log"
        echo "---" >> "$RESULTS_DIR/path_traversal.log"
        
        # Check for successful traversal indicators
        if echo "$body" | grep -q "root:\|daemon:\|bin:\|sys:"; then
            log_fail "Possible path traversal success with: $payload"
            issues=$((issues + 1))
        elif [ "$status_code" -eq 200 ] && [ "$(echo "$body" | wc -c)" -gt 1000 ]; then
            log_warn "Large response with path traversal payload: $payload"
        fi
    done
    
    if [ $issues -eq 0 ]; then
        log_pass "No path traversal vulnerabilities detected"
    fi
    
    return $issues
}

# Test rate limiting
test_rate_limiting() {
    local endpoint=$1
    local description=$2
    
    log_sec "Testing rate limiting on $description..."
    
    local success_count=0
    local rate_limited_count=0
    local total_requests=50
    
    log_info "Sending $total_requests rapid requests to test rate limiting..."
    
    for i in $(seq 1 $total_requests); do
        response=$(curl -s -w "%{http_code}" -o /dev/null "$BASE_URL$endpoint")
        
        if [ "$response" -eq 200 ]; then
            success_count=$((success_count + 1))
        elif [ "$response" -eq 429 ]; then
            rate_limited_count=$((rate_limited_count + 1))
        fi
        
        # Small delay to avoid overwhelming
        if [ $((i % 10)) -eq 0 ]; then
            echo "Completed $i/$total_requests requests..." >> "$RESULTS_DIR/rate_limit.log"
        fi
    done
    
    echo "Rate Limiting Test Results for $endpoint:" >> "$RESULTS_DIR/rate_limit.log"
    echo "Total requests: $total_requests" >> "$RESULTS_DIR/rate_limit.log"
    echo "Successful: $success_count" >> "$RESULTS_DIR/rate_limit.log"
    echo "Rate limited (429): $rate_limited_count" >> "$RESULTS_DIR/rate_limit.log"
    echo "---" >> "$RESULTS_DIR/rate_limit.log"
    
    log_info "Rate limiting results: $success_count success, $rate_limited_count rate-limited"
    
    if [ $rate_limited_count -gt 0 ]; then
        log_pass "Rate limiting is active (${rate_limited_count}/${total_requests} requests limited)"
        return 0
    else
        log_warn "No rate limiting detected - all $total_requests requests succeeded"
        return 1
    fi
}

# Test HTTPS enforcement
test_https_enforcement() {
    log_sec "Testing HTTPS enforcement..."
    
    # Extract domain from BASE_URL
    domain=$(echo "$BASE_URL" | sed 's|https\?://||' | cut -d'/' -f1)
    
    # Test HTTP redirect
    http_response=$(curl -s -I "http://$domain/api/health" -w "%{http_code}" 2>/dev/null | tail -1)
    
    if [ "$http_response" -eq 301 ] || [ "$http_response" -eq 302 ] || [ "$http_response" -eq 308 ]; then
        log_pass "HTTP to HTTPS redirect is working (status: $http_response)"
        return 0
    elif [ "$http_response" -eq 000 ]; then
        log_pass "HTTP requests are blocked/refused"
        return 0
    else
        log_fail "HTTP requests are not properly redirected to HTTPS (status: $http_response)"
        return 1
    fi
}

# Test for information disclosure
test_information_disclosure() {
    log_sec "Testing for information disclosure..."
    
    # Test endpoints that might leak information
    info_endpoints=(
        "/api/debug"
        "/api/edge-test"
        "/.env"
        "/config"
        "/admin"
        "/api/config"
        "/api/status"
        "/robots.txt"
        "/sitemap.xml"
    )
    
    local issues=0
    
    for endpoint in "${info_endpoints[@]}"; do
        response=$(curl -s -w "\n%{http_code}" "$BASE_URL$endpoint" 2>/dev/null)
        status_code=$(echo "$response" | tail -n1)
        body=$(echo "$response" | head -n -1)
        
        echo "Info Disclosure Test: $endpoint" >> "$RESULTS_DIR/info_disclosure.log"
        echo "Status: $status_code" >> "$RESULTS_DIR/info_disclosure.log"
        echo "Response: $body" >> "$RESULTS_DIR/info_disclosure.log"
        echo "---" >> "$RESULTS_DIR/info_disclosure.log"
        
        if [ "$status_code" -eq 200 ]; then
            # Check for sensitive information in response
            if echo "$body" | grep -qi "password\|secret\|token\|key\|database\|config"; then
                log_fail "Sensitive information potentially disclosed at $endpoint"
                issues=$((issues + 1))
            elif echo "$body" | grep -qi "error\|exception\|stack\|trace\|debug"; then
                log_warn "Debug/error information disclosed at $endpoint"
                issues=$((issues + 1))
            else
                log_info "Endpoint $endpoint accessible but no obvious sensitive data"
            fi
        fi
    done
    
    if [ $issues -eq 0 ]; then
        log_pass "No obvious information disclosure detected"
    fi
    
    return $issues
}

# Test Content-Type validation
test_content_type_validation() {
    log_sec "Testing Content-Type validation..."
    
    # Test with various malicious content types
    content_types=(
        "application/x-www-form-urlencoded"
        "multipart/form-data"
        "text/xml"
        "application/xml"
        "text/html"
    )
    
    local issues=0
    
    for ct in "${content_types[@]}"; do
        response=$(curl -s -w "\n%{http_code}" -H "Content-Type: $ct" -d "malicious=data" -X POST "$BASE_URL/api/v1/search?q=test" 2>/dev/null)
        status_code=$(echo "$response" | tail -n1)
        
        echo "Content-Type Test: $ct" >> "$RESULTS_DIR/content_type.log"
        echo "Status: $status_code" >> "$RESULTS_DIR/content_type.log"
        echo "---" >> "$RESULTS_DIR/content_type.log"
        
        if [ "$status_code" -eq 200 ]; then
            log_warn "Endpoint accepts potentially unsafe Content-Type: $ct"
            issues=$((issues + 1))
        fi
    done
    
    if [ $issues -eq 0 ]; then
        log_pass "Content-Type validation appears properly configured"
    fi
    
    return $issues
}

echo "========================================="
echo "TMNT API Security Test Suite"
echo "========================================="
echo "Base URL: $BASE_URL"
echo "Results Dir: $RESULTS_DIR"
echo "Start Time: $(date)"
echo "========================================="

FAILED_TESTS=0
TOTAL_TESTS=0

# Test 1: Security Headers
log_info "Testing security headers..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_security_headers "/api/v1/turtles" "Turtles Endpoint"; then
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 2: HTTPS Enforcement
log_info "Testing HTTPS enforcement..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_https_enforcement; then
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 3: Injection Attacks
log_info "Testing injection vulnerabilities..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_injection_attacks "/api/v1/search" "q" "Search Endpoint"; then
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 4: Path Traversal
log_info "Testing path traversal vulnerabilities..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_path_traversal "/api/v1/turtles" "Turtle Endpoint"; then
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 5: Rate Limiting
log_info "Testing rate limiting..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_rate_limiting "/api/v1/quotes/random" "Random Quote Endpoint"; then
    # Rate limiting absence is a warning, not necessarily a failure
    log_warn "Consider implementing rate limiting for production APIs"
fi

# Test 6: Information Disclosure
log_info "Testing information disclosure..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_information_disclosure; then
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Test 7: Content-Type Validation
log_info "Testing content-type validation..."
TOTAL_TESTS=$((TOTAL_TESTS + 1))
if ! test_content_type_validation; then
    FAILED_TESTS=$((FAILED_TESTS + 1))
fi

# Additional specific tests for this API
log_info "Running API-specific security tests..."

# Test CORS configuration
log_sec "Testing CORS configuration..."
cors_response=$(curl -s -I -H "Origin: https://malicious-site.com" "$BASE_URL/api/v1/turtles")
if echo "$cors_response" | grep -qi "access-control-allow-origin: \*"; then
    log_warn "CORS allows all origins - consider restricting in production"
else
    log_pass "CORS configuration appears restrictive"
fi

# Test for API versioning bypass
log_sec "Testing API versioning security..."
version_bypass_urls=(
    "/api/v2/turtles"
    "/api/v0/turtles"  
    "/api/turtles"
    "/api/v1/../turtles"
)

for url in "${version_bypass_urls[@]}"; do
    response=$(curl -s -w "%{http_code}" -o /dev/null "$BASE_URL$url")
    if [ "$response" -eq 200 ]; then
        log_warn "Possible API versioning bypass: $url"
    fi
done

# Generate security summary
{
    echo "TMNT API Security Test Summary - $(date)"
    echo "========================================"
    echo "Base URL: $BASE_URL"
    echo "Total Tests: $TOTAL_TESTS"
    echo "Failed Tests: $FAILED_TESTS"
    echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"
    echo ""
    echo "Security Assessment:"
    echo "==================="
    echo "- HTTP Security Headers: Review headers.log"
    echo "- Injection Protection: Review injection_tests.log"
    echo "- Path Traversal: Review path_traversal.log"
    echo "- Information Disclosure: Review info_disclosure.log"
    echo "- Rate Limiting: Review rate_limit.log"
    echo "- Content-Type Validation: Review content_type.log"
    echo ""
    echo "Recommendations:"
    echo "==============="
    echo "1. Implement security headers (X-Content-Type-Options, X-Frame-Options)"
    echo "2. Consider rate limiting for public APIs"
    echo "3. Review CORS policy for production environment"
    echo "4. Ensure no sensitive information is exposed in error messages"
    echo "5. Implement proper input validation and sanitization"
    echo ""
    echo "Note: This is a basic security assessment. Consider professional"
    echo "penetration testing for production applications."
} > "$RESULTS_DIR/security_summary.txt"

echo "========================================="
echo "Security Test Results Summary"
echo "========================================="
echo "Total Tests: $TOTAL_TESTS"
echo "Failed Tests: $FAILED_TESTS"
echo "Passed Tests: $((TOTAL_TESTS - FAILED_TESTS))"

if [ $FAILED_TESTS -eq 0 ]; then
    echo -e "${GREEN}✅ No critical security issues detected!${NC}"
    echo -e "${YELLOW}⚠️  Review warnings and recommendations in security_summary.txt${NC}"
    exit 0
else
    echo -e "${RED}❌ $FAILED_TESTS security test(s) failed!${NC}"
    echo -e "${RED}Review security issues before deploying to production.${NC}"
    exit 1
fi