"""
Convex client for Python
Handles connection to Convex backend and provides data access
"""
import os
from typing import Any, Optional, List, Dict
from convex import ConvexClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv(".env.local")

class ConvexDataClient:
    def __init__(self):
        """Initialize Convex client with URL from environment"""
        self.convex_url = os.environ.get('CONVEX_URL')
        if self.convex_url:
            self.convex_url = self.convex_url.strip()  # Remove any whitespace
        self._fallback_data = None
        
        if self.convex_url:
            try:
                self.client = ConvexClient(self.convex_url)
                self._connected = True
            except Exception as e:
                print(f"Failed to connect to Convex: {e}")
                self._connected = False
                self._load_fallback_data()
        else:
            self._connected = False
            self._load_fallback_data()
    
    def _load_fallback_data(self):
        """Load fallback data when Convex is not available"""
        try:
            # Import the existing data as fallback
            from api.data.tmnt_data import TURTLES, VILLAINS, WEAPONS, QUOTES, EPISODES
            self._fallback_data = {
                'turtles': {k: v.model_dump() for k, v in TURTLES.items()},
                'villains': {k: v.model_dump() for k, v in VILLAINS.items()},
                'weapons': [w.model_dump() for w in WEAPONS],
                'quotes': [q.model_dump() for q in QUOTES],
                'episodes': [e.model_dump() for e in EPISODES]
            }
        except ImportError:
            # If import fails, use empty data
            self._fallback_data = {
                'turtles': {},
                'villains': {},
                'weapons': [],
                'quotes': [],
                'episodes': []
            }
    
    def _clean_convex_data(self, data: Any) -> Any:
        """Remove Convex internal fields from data"""
        if isinstance(data, dict):
            cleaned = {k: v for k, v in data.items() if not k.startswith('_')}
            # Convert episode_id back to id and ensure it's an int
            if 'episode_id' in cleaned:
                cleaned['id'] = int(cleaned.pop('episode_id'))
            # Convert float fields to int for episodes
            if 'season' in cleaned and isinstance(cleaned['season'], float):
                cleaned['season'] = int(cleaned['season'])
            if 'episode_number' in cleaned and isinstance(cleaned['episode_number'], float):
                cleaned['episode_number'] = int(cleaned['episode_number'])
            return cleaned
        elif isinstance(data, list):
            return [self._clean_convex_data(item) for item in data]
        return data
    
    def get_turtles(self) -> List[Dict[str, Any]]:
        """Get all turtles"""
        if self._connected:
            try:
                turtles = self.client.query("turtles:getAll")
                # Convert Convex format to our API format
                return [self._clean_convex_data(t) for t in turtles] if turtles else []
            except Exception as e:
                print(f"Error querying Convex for turtles: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            return list(self._fallback_data['turtles'].values())
        return []
    
    def get_turtle(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a specific turtle by name"""
        if self._connected:
            try:
                turtle = self.client.query("turtles:getByName", {"name": name})
                return self._clean_convex_data(turtle) if turtle else None
            except Exception as e:
                print(f"Error querying Convex for turtle {name}: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            return self._fallback_data['turtles'].get(name)
        return None
    
    def get_villains(self) -> List[Dict[str, Any]]:
        """Get all villains"""
        if self._connected:
            try:
                villains = self.client.query("villains:getAll")
                return [self._clean_convex_data(v) for v in villains] if villains else []
            except Exception as e:
                print(f"Error querying Convex for villains: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            return list(self._fallback_data['villains'].values())
        return []
    
    def get_villain(self, name: str) -> Optional[Dict[str, Any]]:
        """Get a specific villain by name"""
        if self._connected:
            try:
                villain = self.client.query("villains:getByName", {"name": name})
                return self._clean_convex_data(villain) if villain else None
            except Exception as e:
                print(f"Error querying Convex for villain {name}: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            return self._fallback_data['villains'].get(name)
        return None
    
    def get_episodes(self, season: Optional[int] = None, limit: int = 10, offset: int = 0) -> List[Dict[str, Any]]:
        """Get episodes with optional filtering and pagination"""
        if self._connected:
            try:
                params = {"limit": limit, "offset": offset}
                if season is not None:
                    params["season"] = season
                
                episodes = self.client.query("episodes:getAll", params)
                return [self._clean_convex_data(e) for e in episodes] if episodes else []
            except Exception as e:
                print(f"Error querying Convex for episodes: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            episodes = self._fallback_data['episodes']
            
            # Filter by season if provided
            if season is not None:
                episodes = [ep for ep in episodes if ep['season'] == season]
            
            # Apply pagination
            return episodes[offset:offset + limit]
        return []
    
    def get_episode(self, episode_id: int) -> Optional[Dict[str, Any]]:
        """Get a specific episode by ID"""
        if self._connected:
            try:
                episode = self.client.query("episodes:getById", {"episode_id": episode_id})
                return self._clean_convex_data(episode) if episode else None
            except Exception as e:
                print(f"Error querying Convex for episode {episode_id}: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            for episode in self._fallback_data['episodes']:
                if episode['id'] == episode_id:
                    return episode
        return None
    
    def get_quotes(self, character: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get all quotes, optionally filtered by character"""
        if self._connected:
            try:
                params = {}
                if character:
                    params["character"] = character
                
                quotes = self.client.query("quotes:getAll", params)
                return [self._clean_convex_data(q) for q in quotes] if quotes else []
            except Exception as e:
                print(f"Error querying Convex for quotes: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            quotes = self._fallback_data['quotes']
            if character:
                quotes = [q for q in quotes if q['character'].lower() == character.lower()]
            return quotes
        return []
    
    def get_random_quote(self) -> Optional[Dict[str, Any]]:
        """Get a random quote"""
        if self._connected:
            try:
                quote = self.client.query("quotes:getRandom")
                return self._clean_convex_data(quote) if quote else None
            except Exception as e:
                print(f"Error querying Convex for random quote: {e}")
        
        # Fall back to local data
        if self._fallback_data and self._fallback_data['quotes']:
            import random
            return random.choice(self._fallback_data['quotes'])
        return None
    
    def get_weapons(self) -> List[Dict[str, Any]]:
        """Get all weapons"""
        if self._connected:
            try:
                weapons = self.client.query("weapons:getAll")
                return [self._clean_convex_data(w) for w in weapons] if weapons else []
            except Exception as e:
                print(f"Error querying Convex for weapons: {e}")
        
        # Fall back to local data
        if self._fallback_data:
            return self._fallback_data['weapons']
        return []

# Global instance
convex_client = ConvexDataClient()