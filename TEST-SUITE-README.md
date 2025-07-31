# TMNT API - Test Suite Documentation

## Overview

This directory contains a comprehensive test suite for the TMNT API deployed on Vercel. The test suite includes regression, performance, and security testing to ensure the API is production-ready before deployment.

## Quick Start

### Prerequisites
- `curl` - for HTTP requests
- `jq` - for JSON processing  
- `bc` - for mathematical calculations

### Run All Tests
```bash
./scripts/run-all-tests.sh
```

### Run Individual Test Suites
```bash
# Regression tests (functional testing)
./scripts/regression-test-suite.sh

# Performance tests (load and cache testing)
./scripts/performance-test-suite.sh

# Security tests (vulnerability assessment)
./scripts/security-test-suite.sh

# Quick validation (fast endpoint check)
./scripts/quick-validation.sh
```

## Test Suites

### 1. Regression Test Suite (`regression-test-suite.sh`)
**Purpose**: Verify all API endpoints function correctly and handle errors appropriately.

**Coverage**:
- ✅ All 10 API endpoints
- ✅ JSON response validation
- ✅ Error handling (404, 422 status codes)
- ✅ Input validation and boundary testing
- ✅ Case sensitivity testing
- ✅ Basic performance thresholds

**Pass Criteria**: All endpoints return expected status codes and valid JSON structures.

### 2. Performance Test Suite (`performance-test-suite.sh`)
**Purpose**: Validate response times, concurrent load handling, and cache effectiveness.

**Coverage**:
- ⚡ Single endpoint performance testing
- ⚡ Concurrent load testing (configurable users)
- ⚡ Cache effectiveness validation
- ⚡ Network latency analysis

**Thresholds**:
- Static endpoints: < 1.0s response time
- Dynamic endpoints: < 1.5s response time
- Search functionality: < 1.8s response time
- Concurrent load: >95% success rate

### 3. Security Test Suite (`security-test-suite.sh`)
**Purpose**: Identify security vulnerabilities and validate security best practices.

**Coverage**:
- 🔒 HTTP security headers validation
- 🔒 HTTPS enforcement testing
- 🔒 Injection attack protection (SQL, XSS, Command)
- 🔒 Path traversal vulnerability testing
- 🔒 Rate limiting assessment
- 🔒 Information disclosure detection
- 🔒 CORS policy validation

**Security Checks**:
- Input sanitization
- Error message security
- Authentication bypass attempts
- API versioning security

### 4. Quick Validation (`quick-validation.sh`)
**Purpose**: Fast endpoint availability check for CI/CD pipelines.

**Coverage**:
- 🚀 Basic endpoint availability (200 status codes)
- 🚀 Response time validation
- 🚀 Minimal dependencies

## API Endpoints Tested

| Endpoint | Description | Test Coverage |
|----------|-------------|---------------|
| `/api` | API root documentation | ✅ Functional, ⚡ Performance, 🔒 Security |
| `/api/health` | Health check | ✅ Functional, ⚡ Performance, 🔒 Security |
| `/api/v1/turtles` | Get all turtles | ✅ Functional, ⚡ Performance, 🔒 Security |
| `/api/v1/turtles/{name}` | Get turtle by name | ✅ Functional, ⚡ Performance, 🔒 Security |
| `/api/v1/villains` | Get all villains | ✅ Functional, ⚡ Performance, 🔒 Security |
| `/api/v1/villains/{name}` | Get villain by name | ✅ Functional, ⚡ Performance |
| `/api/v1/episodes` | Get episodes (paginated) | ✅ Functional, ⚡ Performance |
| `/api/v1/quotes/random` | Get random quote | ✅ Functional, ⚡ Performance |
| `/api/v1/weapons` | Get all weapons | ✅ Functional, ⚡ Performance |
| `/api/v1/search?q={query}` | Search functionality | ✅ Functional, ⚡ Performance, 🔒 Security |

## Test Result Interpretation

### Exit Codes
- `0` - All tests passed, ready for deployment
- `1` - Some tests failed, review required before deployment

### Result Files
Each test run generates timestamped directories with detailed logs:

```
test-results-YYYYMMDD-HHMMSS/
├── summary.txt           # High-level test summary
├── test.log             # Detailed test execution log
├── responses.log        # API response details
└── errors.log           # Failed test details

performance-results-YYYYMMDD-HHMMSS/
├── performance_summary.txt    # Performance test summary
├── performance_details.log   # Individual endpoint metrics
├── load_test_details.log     # Concurrent load test results
└── cache_test_details.log    # Cache effectiveness analysis

security-results-YYYYMMDD-HHMMSS/
├── security_summary.txt      # Security assessment summary
├── security.log             # Detailed security test log
├── headers.log              # HTTP security headers analysis
├── injection_tests.log      # Injection attack test results
└── info_disclosure.log      # Information disclosure tests
```

## CI/CD Integration

### Pre-Deployment Checklist
1. Run regression test suite: `./scripts/regression-test-suite.sh`
2. Validate performance thresholds: `./scripts/performance-test-suite.sh`
3. Check security posture: `./scripts/security-test-suite.sh`
4. Review all test results for failures
5. Only deploy if all tests pass

### GitHub Actions Example
```yaml
name: API Test Suite
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y curl jq bc
      - name: Run regression tests
        run: ./scripts/regression-test-suite.sh
      - name: Run performance tests
        run: ./scripts/performance-test-suite.sh
      - name: Run security tests
        run: ./scripts/security-test-suite.sh
```

### Vercel Deployment Integration
```bash
# Pre-deployment validation
./scripts/run-all-tests.sh

# Deploy only if tests pass
if [ $? -eq 0 ]; then
  vercel --prod
else
  echo "Tests failed - deployment blocked"
  exit 1
fi
```

## Customization

### Testing Different Environments
```bash
# Test staging environment
./scripts/run-all-tests.sh https://staging-api.vercel.app

# Test local development
./scripts/run-all-tests.sh http://localhost:8000

# Skip performance tests for faster feedback
./scripts/run-all-tests.sh https://api.example.com true false
```

### Performance Tuning
Adjust performance thresholds in `performance-test-suite.sh`:
```bash
# Modify these values based on your requirements
STATIC_THRESHOLD="1.0"      # Static content response time
DYNAMIC_THRESHOLD="1.5"     # Dynamic content response time
SEARCH_THRESHOLD="1.8"      # Search functionality response time
```

### Security Configuration
Customize security tests in `security-test-suite.sh`:
```bash
# Add custom injection payloads
custom_payloads=(
  "your-custom-payload"
  "another-test-case"
)

# Modify expected security headers
expected_headers=(
  "X-Content-Type-Options"
  "X-Frame-Options"
  "Your-Custom-Header"
)
```

## Troubleshooting

### Common Issues

1. **Tests timing out**
   - Increase curl timeout values
   - Check network connectivity
   - Verify API is deployed and accessible

2. **JSON validation failures**
   - Ensure `jq` is installed and up-to-date
   - Check API responses for valid JSON format
   - Review response logs for malformed JSON

3. **Performance tests failing**
   - Adjust performance thresholds
   - Consider network latency to test environment
   - Check for API rate limiting

4. **Security tests reporting issues**
   - Review security findings in detail
   - Some warnings may be acceptable for development
   - Prioritize fixing high-severity issues

### Getting Help

1. Review detailed logs in result directories
2. Check API health endpoint: `/api/health`
3. Validate individual endpoints manually with curl
4. Run quick validation for fast debugging: `./scripts/quick-validation.sh`

## Best Practices

### Before Each Deployment
1. Run full test suite: `./scripts/run-all-tests.sh`
2. Review any warnings or failures
3. Update test expectations if API behavior changes intentionally
4. Archive test results for audit trails

### Ongoing Maintenance
1. Update test data expectations when API data changes
2. Adjust performance thresholds based on production metrics
3. Add new test cases for new features
4. Review security test coverage regularly

### Test Data Management
- Tests use live API data from Edge Config
- Ensure test data is stable and representative
- Consider test data isolation for critical tests
- Document any test data dependencies

---

## Summary

This comprehensive test suite ensures the TMNT API maintains high quality and reliability when deployed to Vercel. The combination of functional, performance, and security testing provides confidence in the API's production readiness.

**Key Benefits:**
- 🎯 **Comprehensive Coverage**: Tests all endpoints and edge cases
- ⚡ **Performance Validation**: Ensures acceptable response times
- 🔒 **Security Assessment**: Identifies vulnerabilities before deployment
- 🚀 **CI/CD Ready**: Integrates with deployment pipelines
- 📊 **Detailed Reporting**: Provides actionable insights

Use these tests as part of your deployment process to catch issues early and maintain a high-quality API experience for your users.