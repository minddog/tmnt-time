"""
Edge Config client for Python
Since Vercel Edge Config SDK is for JavaScript, we'll use HTTP API
"""
import os
import json
from typing import Any, Optional
import urllib.request
import urllib.error

class EdgeConfigClient:
    def __init__(self):
        # Edge Config connection string format:
        # https://edge-config.vercel.com/<config-id>?token=<token>
        self.edge_config_url = os.environ.get('EDGE_CONFIG')
        if not self.edge_config_url:
            self.edge_config_url = None
            self._cache = {}
            self._load_fallback_data()
    
    def _load_fallback_data(self):
        """Load fallback data when Edge Config is not available"""
        try:
            # Import the existing data as fallback
            from api.data.tmnt_data import TURTLES, VILLAINS, WEAPONS, QUOTES, EPISODES
            self._cache = {
                'turtles': {k: v.dict() for k, v in TURTLES.items()},
                'villains': {k: v.dict() for k, v in VILLAINS.items()},
                'weapons': [w.dict() for w in WEAPONS],
                'quotes': [q.dict() for q in QUOTES],
                'episodes': [e.dict() for e in EPISODES]
            }
        except ImportError:
            # If import fails, use empty cache
            self._cache = {
                'turtles': {},
                'villains': {},
                'weapons': [],
                'quotes': [],
                'episodes': []
            }
    
    def get(self, key: str) -> Optional[Any]:
        """Get a value from Edge Config"""
        if not self.edge_config_url:
            return self._cache.get(key)
        
        try:
            # Edge Config URL already includes the token
            url = f"{self.edge_config_url}/item/{key}"
            req = urllib.request.Request(url)
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            # Fall back to cached data on error
            return self._cache.get(key)
        except Exception:
            # Fall back to cached data on any error
            return self._cache.get(key)
    
    def get_all(self) -> dict:
        """Get all values from Edge Config"""
        if not self.edge_config_url:
            return self._cache
        
        try:
            # Get all items from Edge Config
            req = urllib.request.Request(self.edge_config_url)
            
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                return data
        except Exception:
            # Fall back to cached data on any error
            return self._cache

# Global instance
edge_config = EdgeConfigClient()