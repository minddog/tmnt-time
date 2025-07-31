#!/bin/bash

# Master Test Runner for TMNT API
# Runs all test suites in sequence and generates comprehensive report
# Usage: ./run-all-tests.sh [BASE_URL] [SKIP_PERFORMANCE] [SKIP_SECURITY]

BASE_URL="${1:-https://vercel-python-nine-tau.vercel.app}"
SKIP_PERFORMANCE="${2:-false}"
SKIP_SECURITY="${3:-false}"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Test results tracking
REGRESSION_RESULT=0
PERFORMANCE_RESULT=0
SECURITY_RESULT=0

# Create master results directory
MASTER_RESULTS_DIR="tmnt-api-test-results-$(date +%Y%m%d-%H%M%S)"
mkdir -p "$MASTER_RESULTS_DIR"

log_header() {
    echo ""
    echo -e "${CYAN}=========================================${NC}"
    echo -e "${CYAN}$1${NC}"
    echo -e "${CYAN}=========================================${NC}"
}

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_failure() {
    echo -e "${RED}[FAILURE]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Check if required tools are available
check_dependencies() {
    log_info "Checking dependencies..."
    
    local missing_tools=()
    
    if ! command -v curl &> /dev/null; then
        missing_tools+=("curl")
    fi
    
    if ! command -v jq &> /dev/null; then
        missing_tools+=("jq")
    fi
    
    if ! command -v bc &> /dev/null; then
        missing_tools+=("bc")
    fi
    
    if [ ${#missing_tools[@]} -ne 0 ]; then
        log_failure "Missing required tools: ${missing_tools[*]}"
        log_info "Please install missing tools and try again"
        exit 1
    fi
    
    log_success "All required tools are available"
}

# Test API availability before running tests
test_api_availability() {
    log_info "Testing API availability..."
    
    local health_check=$(curl -s -w "%{http_code}" -o /dev/null "$BASE_URL/api/health" --max-time 10)
    
    if [ "$health_check" -eq 200 ]; then
        log_success "API is available and responding"
        return 0
    else
        log_failure "API is not available (status: $health_check)"
        log_info "Please check if the API is deployed and accessible at: $BASE_URL"
        return 1
    fi
}

# Run regression test suite
run_regression_tests() {
    log_header "RUNNING REGRESSION TEST SUITE"
    
    if [ ! -f "./scripts/regression-test-suite.sh" ]; then
        log_failure "Regression test suite not found"
        return 1
    fi
    
    log_info "Starting regression tests..."
    ./scripts/regression-test-suite.sh "$BASE_URL"
    REGRESSION_RESULT=$?
    
    # Move results to master directory
    if ls test-results-* 1> /dev/null 2>&1; then
        latest_regression_dir=$(ls -dt test-results-* | head -1)
        mv "$latest_regression_dir" "$MASTER_RESULTS_DIR/regression-results"
        log_info "Regression test results moved to $MASTER_RESULTS_DIR/regression-results"
    fi
    
    if [ $REGRESSION_RESULT -eq 0 ]; then
        log_success "Regression tests PASSED"
    else
        log_failure "Regression tests FAILED"
    fi
    
    return $REGRESSION_RESULT
}

# Run performance test suite
run_performance_tests() {
    if [ "$SKIP_PERFORMANCE" = "true" ]; then
        log_warning "Skipping performance tests (as requested)"
        return 0
    fi
    
    log_header "RUNNING PERFORMANCE TEST SUITE"
    
    if [ ! -f "./scripts/performance-test-suite.sh" ]; then
        log_failure "Performance test suite not found"
        return 1
    fi
    
    log_info "Starting performance tests..."
    ./scripts/performance-test-suite.sh "$BASE_URL" 5  # Use 5 concurrent users for testing
    PERFORMANCE_RESULT=$?
    
    # Move results to master directory
    if ls performance-results-* 1> /dev/null 2>&1; then
        latest_performance_dir=$(ls -dt performance-results-* | head -1)
        mv "$latest_performance_dir" "$MASTER_RESULTS_DIR/performance-results"
        log_info "Performance test results moved to $MASTER_RESULTS_DIR/performance-results"
    fi
    
    if [ $PERFORMANCE_RESULT -eq 0 ]; then
        log_success "Performance tests PASSED"
    else
        log_failure "Performance tests FAILED"
    fi
    
    return $PERFORMANCE_RESULT
}

# Run security test suite
run_security_tests() {
    if [ "$SKIP_SECURITY" = "true" ]; then
        log_warning "Skipping security tests (as requested)"
        return 0
    fi
    
    log_header "RUNNING SECURITY TEST SUITE"
    
    if [ ! -f "./scripts/security-test-suite.sh" ]; then
        log_failure "Security test suite not found"
        return 1
    fi
    
    log_info "Starting security tests..."
    ./scripts/security-test-suite.sh "$BASE_URL"
    SECURITY_RESULT=$?
    
    # Move results to master directory
    if ls security-results-* 1> /dev/null 2>&1; then
        latest_security_dir=$(ls -dt security-results-* | head -1)
        mv "$latest_security_dir" "$MASTER_RESULTS_DIR/security-results"
        log_info "Security test results moved to $MASTER_RESULTS_DIR/security-results"
    fi
    
    if [ $SECURITY_RESULT -eq 0 ]; then
        log_success "Security tests PASSED"
    else
        log_failure "Security tests FAILED"
    fi
    
    return $SECURITY_RESULT
}

# Generate comprehensive test report
generate_master_report() {
    log_header "GENERATING COMPREHENSIVE TEST REPORT"
    
    local start_time="$1"
    local end_time="$2"
    local duration=$((end_time - start_time))
    
    # Calculate overall status
    local overall_status="PASSED"
    local failed_suites=()
    
    if [ $REGRESSION_RESULT -ne 0 ]; then
        overall_status="FAILED"
        failed_suites+=("Regression")
    fi
    
    if [ $PERFORMANCE_RESULT -ne 0 ]; then
        overall_status="FAILED"
        failed_suites+=("Performance")
    fi
    
    if [ $SECURITY_RESULT -ne 0 ]; then
        overall_status="FAILED"
        failed_suites+=("Security")
    fi
    
    # Create master report
    cat > "$MASTER_RESULTS_DIR/master-test-report.md" << EOF
# TMNT API - Comprehensive Test Report

**Generated:** $(date)  
**API URL:** $BASE_URL  
**Test Duration:** ${duration} seconds  
**Overall Status:** **$overall_status**

## Executive Summary

This report contains the results of comprehensive testing performed on the TMNT API before deployment to Vercel. The testing includes regression, performance, and security assessments.

## Test Suite Results

### 🔄 Regression Tests
- **Status:** $([ $REGRESSION_RESULT -eq 0 ] && echo "✅ PASSED" || echo "❌ FAILED")
- **Purpose:** Verify all API endpoints return expected data and handle errors correctly
- **Details:** See \`regression-results/\` directory

### ⚡ Performance Tests
- **Status:** $([ "$SKIP_PERFORMANCE" = "true" ] && echo "⏭️ SKIPPED" || ([ $PERFORMANCE_RESULT -eq 0 ] && echo "✅ PASSED" || echo "❌ FAILED"))
- **Purpose:** Validate response times, concurrent load handling, and cache effectiveness
- **Details:** See \`performance-results/\` directory

### 🔒 Security Tests
- **Status:** $([ "$SKIP_SECURITY" = "true" ] && echo "⏭️ SKIPPED" || ([ $SECURITY_RESULT -eq 0 ] && echo "✅ PASSED" || echo "❌ FAILED"))
- **Purpose:** Check for common vulnerabilities and security best practices
- **Details:** See \`security-results/\` directory

## Deployment Recommendation

EOF

    if [ "$overall_status" = "PASSED" ]; then
        cat >> "$MASTER_RESULTS_DIR/master-test-report.md" << EOF
✅ **APPROVED FOR DEPLOYMENT**

All test suites have passed successfully. The API is ready for production deployment to Vercel.

### Next Steps:
1. Deploy to Vercel using \`vercel --prod\`
2. Run post-deployment smoke tests
3. Monitor API performance and error rates
4. Set up ongoing monitoring and alerting

EOF
    else
        cat >> "$MASTER_RESULTS_DIR/master-test-report.md" << EOF
❌ **NOT APPROVED FOR DEPLOYMENT**

The following test suite(s) failed: ${failed_suites[*]}

### Required Actions:
1. Review failed test details in respective result directories
2. Fix identified issues
3. Re-run test suites until all pass
4. Only deploy after all tests pass

EOF
    fi
    
    cat >> "$MASTER_RESULTS_DIR/master-test-report.md" << EOF
## Test Coverage

### Endpoints Tested:
- \`/api\` - API root documentation
- \`/api/health\` - Health check
- \`/api/v1/turtles\` - Turtle data endpoints
- \`/api/v1/villains\` - Villain data endpoints  
- \`/api/v1/episodes\` - Episode data with pagination
- \`/api/v1/quotes/random\` - Random quote generation
- \`/api/v1/weapons\` - Weapon data
- \`/api/v1/search\` - Search functionality

### Test Types:
- **Functional Testing:** Endpoint functionality and data validation
- **Error Handling:** Invalid inputs and edge cases
- **Performance Testing:** Response times and concurrent load
- **Security Testing:** Injection attacks, headers, and best practices
- **Cache Testing:** Validation of caching strategies

## Files Generated

\`\`\`
$MASTER_RESULTS_DIR/
├── master-test-report.md          # This report
├── regression-results/            # Regression test details
│   ├── summary.txt
│   ├── test.log
│   ├── responses.log
│   └── errors.log
├── performance-results/           # Performance test details
│   ├── performance_summary.txt
│   ├── performance_details.log
│   ├── load_test_details.log
│   └── cache_test_details.log
└── security-results/              # Security test details
    ├── security_summary.txt
    ├── security.log
    ├── headers.log
    ├── injection_tests.log
    └── info_disclosure.log
\`\`\`

---
*Generated by TMNT API Test Suite - $(date)*
EOF

    # Create simple text summary for CI/CD
    cat > "$MASTER_RESULTS_DIR/test-summary.txt" << EOF
TMNT API Test Results Summary
============================
Overall Status: $overall_status
Regression Tests: $([ $REGRESSION_RESULT -eq 0 ] && echo "PASSED" || echo "FAILED")
Performance Tests: $([ "$SKIP_PERFORMANCE" = "true" ] && echo "SKIPPED" || ([ $PERFORMANCE_RESULT -eq 0 ] && echo "PASSED" || echo "FAILED"))
Security Tests: $([ "$SKIP_SECURITY" = "true" ] && echo "SKIPPED" || ([ $SECURITY_RESULT -eq 0 ] && echo "PASSED" || echo "FAILED"))
Test Duration: ${duration} seconds
Generated: $(date)
EOF

    log_success "Master test report generated: $MASTER_RESULTS_DIR/master-test-report.md"
}

# Main execution
main() {
    local start_time=$(date +%s)
    
    log_header "TMNT API - COMPREHENSIVE TEST SUITE"
    log_info "Base URL: $BASE_URL"
    log_info "Results Directory: $MASTER_RESULTS_DIR"
    log_info "Start Time: $(date)"
    
    # Pre-flight checks
    check_dependencies
    if ! test_api_availability; then
        log_failure "Cannot proceed with tests - API is not available"
        exit 1
    fi
    
    # Run test suites
    run_regression_tests
    
    if [ "$SKIP_PERFORMANCE" != "true" ]; then
        run_performance_tests
    fi
    
    if [ "$SKIP_SECURITY" != "true" ]; then
        run_security_tests
    fi
    
    local end_time=$(date +%s)
    
    # Generate comprehensive report
    generate_master_report "$start_time" "$end_time"
    
    # Final summary
    log_header "FINAL TEST RESULTS"
    
    local total_failed=0
    
    if [ $REGRESSION_RESULT -ne 0 ]; then
        log_failure "Regression tests failed"
        total_failed=$((total_failed + 1))
    else
        log_success "Regression tests passed"
    fi
    
    if [ "$SKIP_PERFORMANCE" = "true" ]; then
        log_warning "Performance tests skipped"
    elif [ $PERFORMANCE_RESULT -ne 0 ]; then
        log_failure "Performance tests failed"
        total_failed=$((total_failed + 1))
    else
        log_success "Performance tests passed"
    fi
    
    if [ "$SKIP_SECURITY" = "true" ]; then
        log_warning "Security tests skipped"
    elif [ $SECURITY_RESULT -ne 0 ]; then
        log_failure "Security tests failed"
        total_failed=$((total_failed + 1))
    else
        log_success "Security tests passed"
    fi
    
    echo ""
    log_info "Total execution time: $((end_time - start_time)) seconds"
    log_info "Detailed results available in: $MASTER_RESULTS_DIR/"
    
    if [ $total_failed -eq 0 ]; then
        echo ""
        log_success "🎉 ALL TESTS PASSED - API IS READY FOR DEPLOYMENT! 🎉"
        echo ""
        exit 0
    else
        echo ""
        log_failure "💥 $total_failed TEST SUITE(S) FAILED - FIX ISSUES BEFORE DEPLOYMENT 💥"
        echo ""
        exit 1
    fi
}

# Handle script arguments and help
if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    cat << EOF
TMNT API Comprehensive Test Suite

Usage: $0 [BASE_URL] [SKIP_PERFORMANCE] [SKIP_SECURITY]

Arguments:
    BASE_URL         API base URL (default: https://vercel-python-nine-tau.vercel.app)
    SKIP_PERFORMANCE Set to 'true' to skip performance tests (default: false)
    SKIP_SECURITY    Set to 'true' to skip security tests (default: false)

Examples:
    $0                                          # Run all tests with default URL
    $0 https://my-api.vercel.app               # Run all tests with custom URL
    $0 https://my-api.vercel.app true false    # Skip performance tests only
    $0 https://my-api.vercel.app true true     # Skip performance and security tests

Requirements:
    - curl (for HTTP requests)
    - jq (for JSON processing)
    - bc (for calculations)

Output:
    All test results are saved in a timestamped directory with detailed logs
    and a comprehensive markdown report suitable for sharing with stakeholders.
EOF
    exit 0
fi

# Run main function
main "$@"