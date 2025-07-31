import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_api_root():
    response = client.get("/api")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Welcome to the TMNT API!"


def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "TMNT API"


def test_get_all_turtles():
    response = client.get("/api/v1/turtles")
    assert response.status_code == 200
    turtles = response.json()
    assert len(turtles) == 4
    turtle_names = [t["name"] for t in turtles]
    assert "leonardo" in turtle_names
    assert "donatello" in turtle_names
    assert "raphael" in turtle_names
    assert "michelangelo" in turtle_names


def test_get_turtle_by_name():
    response = client.get("/api/v1/turtles/leonardo")
    assert response.status_code == 200
    turtle = response.json()
    assert turtle["name"] == "leonardo"
    assert turtle["color"] == "blue"
    assert turtle["weapon"] == "Katana"


def test_get_turtle_not_found():
    response = client.get("/api/v1/turtles/splinter")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]


def test_get_all_villains():
    response = client.get("/api/v1/villains")
    assert response.status_code == 200
    villains = response.json()
    assert len(villains) >= 5
    villain_names = [v["name"] for v in villains]
    assert "shredder" in villain_names
    assert "krang" in villain_names


def test_get_villain_by_name():
    response = client.get("/api/v1/villains/shredder")
    assert response.status_code == 200
    villain = response.json()
    assert villain["name"] == "shredder"
    assert villain["real_name"] == "Oroku Saki"


def test_get_episodes():
    response = client.get("/api/v1/episodes")
    assert response.status_code == 200
    episodes = response.json()
    assert len(episodes) >= 5
    assert all("title" in ep for ep in episodes)
    assert all("season" in ep for ep in episodes)


def test_get_episodes_with_pagination():
    response = client.get("/api/v1/episodes?limit=2&offset=0")
    assert response.status_code == 200
    episodes = response.json()
    assert len(episodes) <= 2


def test_get_episode_by_id():
    response = client.get("/api/v1/episodes/1")
    assert response.status_code == 200
    episode = response.json()
    assert episode["id"] == 1
    assert episode["title"] == "Turtle Tracks"


def test_get_random_quote():
    response = client.get("/api/v1/quotes/random")
    assert response.status_code == 200
    quote = response.json()
    assert "text" in quote
    assert "character" in quote


def test_get_all_quotes():
    response = client.get("/api/v1/quotes")
    assert response.status_code == 200
    quotes = response.json()
    assert len(quotes) >= 8


def test_get_quotes_by_character():
    response = client.get("/api/v1/quotes?character=Michelangelo")
    assert response.status_code == 200
    quotes = response.json()
    assert all(q["character"] == "Michelangelo" for q in quotes)


def test_get_weapons():
    response = client.get("/api/v1/weapons")
    assert response.status_code == 200
    weapons = response.json()
    assert len(weapons) == 4
    weapon_names = [w["name"] for w in weapons]
    assert "Katana" in weapon_names
    assert "Bo Staff" in weapon_names
    assert "Sai" in weapon_names
    assert "Nunchucks" in weapon_names


def test_search_functionality():
    response = client.get("/api/v1/search?q=turtle")
    assert response.status_code == 200
    results = response.json()
    assert "turtles" in results
    assert "villains" in results
    assert "episodes" in results
    assert "quotes" in results


def test_search_minimum_length():
    response = client.get("/api/v1/search?q=a")
    assert response.status_code == 422  # Validation error for too short query