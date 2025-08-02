#!/usr/bin/env python3
"""
Local development server for TMNT API
"""
import os
import sys
import subprocess
import json
from pathlib import Path

def check_requirements():
    """Check if required packages are installed"""
    try:
        import fastapi
        import uvicorn
        import convex
        import dotenv
    except ImportError as e:
        print(f"❌ Missing required package: {e.name}")
        print("\n📦 Installing requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed!")

def load_env():
    """Load environment variables from .env file"""
    from dotenv import load_dotenv
    env_path = Path(".env")
    
    if not env_path.exists():
        print("⚠️  No .env file found. Creating template...")
        with open(".env", "w") as f:
            f.write("""# Vercel Configuration
VERCEL_TOKEN=your_vercel_api_token
EDGE_CONFIG_ID=your_edge_config_id
VERCEL_TEAM_ID=your_team_id_if_applicable

# Convex Configuration
CONVEX_URL=your_convex_deployment_url
""")
        print("📝 Created .env template. Please fill in your credentials.")
        print("   - Get VERCEL_TOKEN from: https://vercel.com/account/tokens")
        print("   - Get CONVEX_URL from: https://dashboard.convex.dev")
        return False
    
    load_dotenv()
    return True

def load_dev_config():
    """Load development configuration from .dev-config.json if it exists"""
    config_path = Path(".dev-config.json")
    default_config = {
        "server": {
            "host": "0.0.0.0",
            "port": 8000,
            "reload": True,
            "log_level": "info",
            "use_colors": True
        },
        "watch": {
            "include_patterns": ["*.py", "*.json", "*.html", "*.css", "*.js", "*.md", "*.txt", "*.yml", "*.yaml", "*.env"],
            "exclude_patterns": ["*.pyc", "__pycache__", ".git", ".venv", "venv", "node_modules", ".pytest_cache"]
        }
    }
    
    if config_path.exists():
        try:
            with open(config_path) as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️  Error loading .dev-config.json: {e}")
            print("   Using default configuration")
    
    return default_config

def run_server():
    """Run the local development server"""
    # Load configuration
    config = load_dev_config()
    server_config = config.get("server", {})
    watch_config = config.get("watch", {})
    
    host = server_config.get("host", "0.0.0.0")
    port = server_config.get("port", 8000)
    
    print("\n🚀 Starting TMNT API local development server...")
    print(f"📍 API Documentation: http://localhost:{port}/docs")
    print(f"📍 API Root: http://localhost:{port}/api")
    print(f"📍 Health Check: http://localhost:{port}/api/health")
    print("\n🔄 Auto-reload enabled - watching all files in project directory")
    print("✨ Press Ctrl+C to stop the server\n")
    
    # Import and run the FastAPI app
    import uvicorn
    
    # Get the current directory as the root for watching
    current_dir = Path.cwd()
    
    uvicorn.run(
        "api.index:app",
        host=host,
        port=port,
        reload=server_config.get("reload", True),
        reload_dirs=[str(current_dir)],  # Watch current directory and all subdirectories
        reload_includes=watch_config.get("include_patterns", ["*.py"]),  # Watch these file types
        reload_excludes=watch_config.get("exclude_patterns", []),  # Ignore these
        log_level=server_config.get("log_level", "info"),
        use_colors=server_config.get("use_colors", True)
    )

def main():
    """Main entry point"""
    print("🐢 TMNT API Local Development Server 🐢")
    print("=" * 40)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        sys.exit(1)
    
    # Check and install requirements
    check_requirements()
    
    # Load environment variables
    if not load_env():
        print("\n⚠️  Please configure your .env file before running the server.")
        sys.exit(1)
    
    # Run the server
    try:
        run_server()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Cowabunga!")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()