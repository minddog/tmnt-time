from typing import Dict, List
from api.models import Turtle, Villain, Episode, Quote, Weapon

TURTLES: Dict[str, Turtle] = {
    "leonardo": Turtle(
        name="leonardo",
        full_name="Leonardo",
        color="blue",
        weapon="Katana",
        personality="Leader, disciplined, responsible",
        favorite_pizza="Pepperoni",
        catchphrase="We strike hard and fade away into the night",
        image_url="/images/leonardo.svg"
    ),
    "donatello": Turtle(
        name="donatello",
        full_name="Donatello",
        color="purple",
        weapon="Bo Staff",
        personality="Tech genius, inventor, problem solver",
        favorite_pizza="Hawaiian",
        catchphrase="Does machine!",
        image_url="/images/donatello.svg"
    ),
    "raphael": Turtle(
        name="raphael",
        full_name="Raphael",
        color="red",
        weapon="Sai",
        personality="Hot-headed, tough, rebellious",
        favorite_pizza="Meat Lovers",
        catchphrase="Turtle Power!",
        image_url="/images/raphael.svg"
    ),
    "michelangelo": Turtle(
        name="michelangelo",
        full_name="Michelangelo",
        color="orange",
        weapon="Nunchucks",
        personality="Fun-loving, laid-back, party dude",
        favorite_pizza="Extra Cheese",
        catchphrase="Cowabunga!",
        image_url="/images/michelangelo.svg"
    )
}

VILLAINS: Dict[str, Villain] = {
    "shredder": Villain(
        name="shredder",
        real_name="Oroku Saki",
        description="The leader of the Foot Clan and arch-nemesis of the Turtles",
        abilities=["Master martial artist", "Strategic genius", "Bladed armor"],
        first_appearance="Episode 1: Turtle Tracks",
        arch_enemy_of="Splinter",
        image_url="/images/shredder.svg"
    ),
    "krang": Villain(
        name="krang",
        real_name="Krang",
        description="An alien warlord from Dimension X, operates from within a mechanical body",
        abilities=["Super intelligence", "Advanced technology", "Dimensional portal creation"],
        first_appearance="Episode 5: Shredder & Splintered",
        image_url="/images/krang.svg"
    ),
    "bebop": Villain(
        name="bebop",
        real_name="Anton Zeck",
        description="Mutant warthog and Shredder's henchman",
        abilities=["Super strength", "Enhanced durability", "Street fighting"],
        first_appearance="Episode 25: Slash and Destroy",
        image_url="/images/bebop.png"
    ),
    "rocksteady": Villain(
        name="rocksteady",
        real_name="Ivan Steranko",
        description="Mutant rhinoceros and Shredder's henchman",
        abilities=["Super strength", "Thick hide", "Military training"],
        first_appearance="Episode 25: Slash and Destroy",
        image_url="/images/rocksteady.png"
    ),
    "baxter_stockman": Villain(
        name="baxter_stockman",
        real_name="Dr. Baxter Stockman",
        description="Mad scientist who creates the Mousers and later becomes a mutant fly",
        abilities=["Scientific genius", "Robotics expert", "Flight (as mutant)"],
        first_appearance="Episode 2: A Better Mousetrap",
        image_url="/images/baxter.png"
    )
}

EPISODES: List[Episode] = [
    Episode(
        id=1,
        title="Turtle Tracks",
        season=1,
        episode_number=1,
        air_date="1987-12-14",
        synopsis="The Turtles make their first appearance and battle the Foot Clan",
        villains_featured=["Shredder", "Foot Soldiers"]
    ),
    Episode(
        id=2,
        title="Enter: The Shredder",
        season=1,
        episode_number=2,
        air_date="1987-12-15",
        synopsis="The Turtles face off against Shredder for the first time",
        villains_featured=["Shredder", "Foot Soldiers"]
    ),
    Episode(
        id=3,
        title="A Better Mousetrap",
        season=1,
        episode_number=3,
        air_date="1987-12-16",
        synopsis="Baxter Stockman unleashes his Mousers on the city",
        villains_featured=["Baxter Stockman"]
    ),
    Episode(
        id=4,
        title="Hot Rodding Teenagers from Dimension X",
        season=1,
        episode_number=4,
        air_date="1987-12-17",
        synopsis="The Neutrinos arrive from Dimension X",
        villains_featured=["Shredder", "Krang"]
    ),
    Episode(
        id=5,
        title="Shredder & Splintered",
        season=1,
        episode_number=5,
        air_date="1987-12-18",
        synopsis="Krang gives Shredder an ultimatum",
        villains_featured=["Shredder", "Krang"]
    )
]

QUOTES: List[Quote] = [
    Quote(
        id=1,
        text="Cowabunga!",
        character="Michelangelo",
        context="Battle cry"
    ),
    Quote(
        id=2,
        text="Turtle Power!",
        character="All Turtles",
        context="Team battle cry"
    ),
    Quote(
        id=3,
        text="Tonight I dine on turtle soup!",
        character="Shredder",
        context="Threatening the Turtles"
    ),
    Quote(
        id=4,
        text="Does machine!",
        character="Donatello",
        context="After fixing something"
    ),
    Quote(
        id=5,
        text="We strike hard and fade away into the night.",
        character="Leonardo",
        context="Explaining ninja tactics"
    ),
    Quote(
        id=6,
        text="I love being a turtle!",
        character="Michelangelo",
        context="Expressing joy"
    ),
    Quote(
        id=7,
        text="Wise men say forgiveness is divine, but never pay full price for late pizza.",
        character="Michelangelo",
        context="Pizza delivery scene"
    ),
    Quote(
        id=8,
        text="A true ninja is a master of himself and his environment.",
        character="Master Splinter",
        context="Training the Turtles"
    )
]

WEAPONS: List[Weapon] = [
    Weapon(
        name="Katana",
        type="Sword",
        wielder="Leonardo",
        description="Twin katana swords, symbols of leadership and honor",
        special_moves=["Double slice", "Spinning blade shield", "Precision strike"]
    ),
    Weapon(
        name="Bo Staff",
        type="Staff",
        wielder="Donatello",
        description="Six-foot bo staff, perfect for reach and defense",
        special_moves=["Vault kick", "Spinning defense", "Staff sweep"]
    ),
    Weapon(
        name="Sai",
        type="Dagger",
        wielder="Raphael",
        description="Twin sai, ideal for close combat and disarming",
        special_moves=["Sai spin", "Disarm technique", "Power thrust"]
    ),
    Weapon(
        name="Nunchucks",
        type="Flail",
        wielder="Michelangelo",
        description="Nunchaku, requiring skill and providing unpredictable attacks",
        special_moves=["Helicopter spin", "Lightning strikes", "Chuck wrap"]
    )
]