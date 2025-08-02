#!/usr/bin/env python3
"""Test script to verify homepage renders locally"""
import subprocess
import time
import httpx
import sys

print("🧪 Testing homepage rendering...")

# Start the server
print("Starting server...")
server = subprocess.Popen(
    [sys.executable, "run_local.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

# Wait for server to start
print("Waiting for server to start...")
time.sleep(3)

try:
    # Test endpoints
    with httpx.Client() as client:
        print("\n📍 Testing endpoints:")
        
        # Test homepage
        print("  Testing homepage (/)...", end=" ")
        response = client.get("http://localhost:8000/")
        if response.status_code == 200 and "TMNT API" in response.text:
            print("✅ Success!")
            print(f"    - Status: {response.status_code}")
            print(f"    - Content-Type: {response.headers.get('content-type')}")
            print(f"    - Title found: {'<title>' in response.text}")
            print(f"    - Size: {len(response.text)} bytes")
        else:
            print("❌ Failed!")
            print(f"    - Status: {response.status_code}")
        
        # Test CSS
        print("\n  Testing CSS (/css/styles.css)...", end=" ")
        response = client.get("http://localhost:8000/css/styles.css")
        if response.status_code == 200:
            print("✅ Success!")
        else:
            print(f"❌ Failed! Status: {response.status_code}")
        
        # Test JS
        print("  Testing JS (/js/app.js)...", end=" ")
        response = client.get("http://localhost:8000/js/app.js")
        if response.status_code == 200:
            print("✅ Success!")
        else:
            print(f"❌ Failed! Status: {response.status_code}")
        
        # Test API
        print("  Testing API (/api/health)...", end=" ")
        response = client.get("http://localhost:8000/api/health")
        if response.status_code == 200:
            print("✅ Success!")
        else:
            print(f"❌ Failed! Status: {response.status_code}")

except Exception as e:
    print(f"\n❌ Error: {e}")
finally:
    # Stop the server
    print("\n🛑 Stopping server...")
    server.terminate()
    server.wait()
    print("✅ Test complete!")