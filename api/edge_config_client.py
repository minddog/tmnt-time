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
        self._cache = {}
        # Always load fallback data as cache
        self._load_fallback_data()
        if not self.edge_config_url:
            self.edge_config_url = None
    
    def _load_fallback_data(self):
        """Load fallback data when Edge Config is not available"""
        try:
            # Import the existing data as fallback
            from api.data.tmnt_data import TURTLES, VILLAINS, WEAPONS, QUOTES, EPISODES
            self._cache = {
                'turtles': {k: v.model_dump() for k, v in TURTLES.items()},
                'villains': {k: v.model_dump() for k, v in VILLAINS.items()},
                'weapons': [w.model_dump() for w in WEAPONS],
                'quotes': [q.model_dump() for q in QUOTES],
                'episodes': [e.model_dump() for e in EPISODES]
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
            # First, get all data from Edge Config
            all_data = self.get_all()
            
            # Check if data is in the expected structure
            if isinstance(all_data, dict):
                # If the data has an 'items' key, look inside it
                if 'items' in all_data and isinstance(all_data['items'], dict):
                    edge_data = all_data['items'].get(key)
                    # If Edge Config has old PNG URLs, use our cached SVG data
                    if key in ['turtles', 'villains'] and edge_data:
                        # Check if it's using old PNG URLs
                        if isinstance(edge_data, dict):
                            first_item = next(iter(edge_data.values()), {})
                            if isinstance(first_item, dict) and first_item.get('image_url', '').endswith('.png'):
                                return self._cache.get(key)
                    return edge_data
                # Otherwise, check at the root level
                return all_data.get(key)
            
            return None
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