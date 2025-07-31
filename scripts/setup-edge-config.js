// This script sets up the Edge Config with TMNT data
// Run this after creating an Edge Config in Vercel Dashboard

const TMNT_DATA = {
  turtles: {
    leonardo: {
      name: "leonardo",
      full_name: "Leonardo",
      color: "blue",
      weapon: "Katana",
      personality: "Leader, disciplined, responsible",
      favorite_pizza: "Pepperoni",
      catchphrase: "We strike hard and fade away into the night",
      image_url: "/images/leonardo.png"
    },
    donatello: {
      name: "donatello",
      full_name: "Donatello",
      color: "purple",
      weapon: "Bo Staff",
      personality: "Tech genius, inventor, problem solver",
      favorite_pizza: "Hawaiian",
      catchphrase: "Does machine!",
      image_url: "/images/donatello.png"
    },
    raphael: {
      name: "raphael",
      full_name: "Raphael",
      color: "red",
      weapon: "Sai",
      personality: "Hot-headed, tough, rebellious",
      favorite_pizza: "Meat Lovers",
      catchphrase: "Turtle Power!",
      image_url: "/images/raphael.png"
    },
    michelangelo: {
      name: "michelangelo",
      full_name: "Michelangelo",
      color: "orange",
      weapon: "Nunchucks",
      personality: "Fun-loving, laid-back, party dude",
      favorite_pizza: "Extra Cheese",
      catchphrase: "Cowabunga!",
      image_url: "/images/michelangelo.png"
    }
  },
  villains: {
    shredder: {
      name: "shredder",
      real_name: "Oroku Saki",
      description: "The leader of the Foot Clan and arch-nemesis of the Turtles",
      abilities: ["Master martial artist", "Strategic genius", "Bladed armor"],
      first_appearance: "Episode 1: Turtle Tracks",
      arch_enemy_of: "Splinter",
      image_url: "/images/shredder.png"
    },
    krang: {
      name: "krang",
      real_name: "Krang",
      description: "An alien warlord from Dimension X, operates from within a mechanical body",
      abilities: ["Super intelligence", "Advanced technology", "Dimensional portal creation"],
      first_appearance: "Episode 5: Shredder & Splintered",
      image_url: "/images/krang.png"
    },
    bebop: {
      name: "bebop",
      real_name: "Anton Zeck",
      description: "Mutant warthog and Shredder's henchman",
      abilities: ["Super strength", "Enhanced durability", "Street fighting"],
      first_appearance: "Episode 25: Slash and Destroy",
      image_url: "/images/bebop.png"
    },
    rocksteady: {
      name: "rocksteady",
      real_name: "Ivan Steranko",
      description: "Mutant rhinoceros and Shredder's henchman",
      abilities: ["Super strength", "Thick hide", "Military training"],
      first_appearance: "Episode 25: Slash and Destroy",
      image_url: "/images/rocksteady.png"
    },
    baxter_stockman: {
      name: "baxter_stockman",
      real_name: "Dr. Baxter Stockman",
      description: "Mad scientist who creates the Mousers and later becomes a mutant fly",
      abilities: ["Scientific genius", "Robotics expert", "Flight (as mutant)"],
      first_appearance: "Episode 2: A Better Mousetrap",
      image_url: "/images/baxter.png"
    }
  },
  weapons: [
    {
      name: "Katana",
      type: "Sword",
      wielder: "Leonardo",
      description: "Twin katana swords, symbols of leadership and honor",
      special_moves: ["Double slice", "Spinning blade shield", "Precision strike"]
    },
    {
      name: "Bo Staff",
      type: "Staff",
      wielder: "Donatello",
      description: "Six-foot bo staff, perfect for reach and defense",
      special_moves: ["Vault kick", "Spinning defense", "Staff sweep"]
    },
    {
      name: "Sai",
      type: "Dagger",
      wielder: "Raphael",
      description: "Twin sai, ideal for close combat and disarming",
      special_moves: ["Sai spin", "Disarm technique", "Power thrust"]
    },
    {
      name: "Nunchucks",
      type: "Flail",
      wielder: "Michelangelo",
      description: "Nunchaku, requiring skill and providing unpredictable attacks",
      special_moves: ["Helicopter spin", "Lightning strikes", "Chuck wrap"]
    }
  ],
  quotes: [
    {
      id: 1,
      text: "Cowabunga!",
      character: "Michelangelo",
      context: "Battle cry"
    },
    {
      id: 2,
      text: "Turtle Power!",
      character: "All Turtles",
      context: "Team battle cry"
    },
    {
      id: 3,
      text: "Tonight I dine on turtle soup!",
      character: "Shredder",
      context: "Threatening the Turtles"
    },
    {
      id: 4,
      text: "Does machine!",
      character: "Donatello",
      context: "After fixing something"
    },
    {
      id: 5,
      text: "We strike hard and fade away into the night.",
      character: "Leonardo",
      context: "Explaining ninja tactics"
    },
    {
      id: 6,
      text: "I love being a turtle!",
      character: "Michelangelo",
      context: "Expressing joy"
    },
    {
      id: 7,
      text: "Wise men say forgiveness is divine, but never pay full price for late pizza.",
      character: "Michelangelo",
      context: "Pizza delivery scene"
    },
    {
      id: 8,
      text: "A true ninja is a master of himself and his environment.",
      character: "Master Splinter",
      context: "Training the Turtles"
    }
  ]
};

console.log('TMNT Edge Config Data:');
console.log(JSON.stringify(TMNT_DATA, null, 2));
console.log('\n\nTo set up Edge Config:');
console.log('1. Go to https://vercel.com/dashboard/stores');
console.log('2. Create a new Edge Config store');
console.log('3. Add the above data to your Edge Config');
console.log('4. Connect it to your project');
console.log('5. The connection string will be added as EDGE_CONFIG env var');