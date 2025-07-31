#!/usr/bin/env node

/**
 * Automated Edge Config Hydration Script
 * This script automatically populates your Edge Config with TMNT data
 * 
 * Usage:
 * 1. Create a .env file with:
 *    - VERCEL_TOKEN: Your Vercel API token
 *    - EDGE_CONFIG_ID: Your Edge Config ID
 *    - VERCEL_TEAM_ID: Your team ID (optional)
 * 
 * 2. Run: node scripts/hydrate-edge-config.js
 */

// Load environment variables from .env file
try {
  require('dotenv').config();
} catch (e) {
  // dotenv is not installed, continue with environment variables
}

const https = require('https');

// TMNT Data
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
  ],
  episodes: [
    {
      id: 1,
      title: "Turtle Tracks",
      season: 1,
      episode_number: 1,
      air_date: "1987-12-14",
      synopsis: "The Turtles make their first appearance and battle the Foot Clan",
      villains_featured: ["Shredder", "Foot Soldiers"]
    },
    {
      id: 2,
      title: "Enter: The Shredder",
      season: 1,
      episode_number: 2,
      air_date: "1987-12-15",
      synopsis: "The Turtles face off against Shredder for the first time",
      villains_featured: ["Shredder", "Foot Soldiers"]
    },
    {
      id: 3,
      title: "A Better Mousetrap",
      season: 1,
      episode_number: 3,
      air_date: "1987-12-16",
      synopsis: "Baxter Stockman unleashes his Mousers on the city",
      villains_featured: ["Baxter Stockman"]
    },
    {
      id: 4,
      title: "Hot Rodding Teenagers from Dimension X",
      season: 1,
      episode_number: 4,
      air_date: "1987-12-17",
      synopsis: "The Neutrinos arrive from Dimension X",
      villains_featured: ["Shredder", "Krang"]
    },
    {
      id: 5,
      title: "Shredder & Splintered",
      season: 1,
      episode_number: 5,
      air_date: "1987-12-18",
      synopsis: "Krang gives Shredder an ultimatum",
      villains_featured: ["Shredder", "Krang"]
    }
  ]
};

// Check for required environment variables
const VERCEL_TOKEN = process.env.VERCEL_TOKEN;
const EDGE_CONFIG_ID = process.env.EDGE_CONFIG_ID;
const VERCEL_TEAM_ID = process.env.VERCEL_TEAM_ID;

if (!VERCEL_TOKEN || !EDGE_CONFIG_ID) {
  console.error('❌ Missing required environment variables!');
  console.error('\nPlease set in .env file or environment:');
  console.error('  VERCEL_TOKEN - Your Vercel API token (create at https://vercel.com/account/tokens)');
  console.error('  EDGE_CONFIG_ID - Your Edge Config ID (from your Edge Config URL)');
  console.error('  VERCEL_TEAM_ID - Your team ID (optional, for team accounts)');
  console.error('\nOption 1: Create a .env file:');
  console.error('  cp .env.example .env');
  console.error('  # Then edit .env with your values');
  console.error('\nOption 2: Set directly:');
  console.error('  VERCEL_TOKEN=xxx EDGE_CONFIG_ID=ecfg_xxx node scripts/hydrate-edge-config.js');
  process.exit(1);
}

// Function to make API request
function makeRequest(method, path, data = null) {
  return new Promise((resolve, reject) => {
    const options = {
      hostname: 'api.vercel.com',
      port: 443,
      path: path,
      method: method,
      headers: {
        'Authorization': `Bearer ${VERCEL_TOKEN}`,
        'Content-Type': 'application/json'
      }
    };

    const req = https.request(options, (res) => {
      let responseData = '';

      res.on('data', (chunk) => {
        responseData += chunk;
      });

      res.on('end', () => {
        try {
          const parsed = JSON.parse(responseData);
          if (res.statusCode >= 200 && res.statusCode < 300) {
            resolve(parsed);
          } else {
            reject(new Error(`API Error: ${res.statusCode} - ${parsed.error?.message || responseData}`));
          }
        } catch (e) {
          reject(new Error(`Failed to parse response: ${responseData}`));
        }
      });
    });

    req.on('error', reject);

    if (data) {
      req.write(JSON.stringify(data));
    }

    req.end();
  });
}

// Function to update Edge Config items
async function updateEdgeConfig() {
  console.log('🚀 Starting Edge Config hydration...\n');

  const teamQuery = VERCEL_TEAM_ID ? `?teamId=${VERCEL_TEAM_ID}` : '';
  const path = `/v1/edge-config/${EDGE_CONFIG_ID}/items${teamQuery}`;

  // Prepare items for bulk update
  const items = Object.entries(TMNT_DATA).map(([key, value]) => ({
    operation: 'upsert',
    key: key,
    value: value
  }));

  try {
    console.log(`📝 Updating ${items.length} items in Edge Config...`);
    
    const response = await makeRequest('PATCH', path, {
      items: items
    });

    console.log('✅ Edge Config updated successfully!');
    console.log('\nUpdated keys:');
    items.forEach(item => {
      console.log(`  - ${item.key} (${typeof item.value === 'object' ? Object.keys(item.value).length + ' items' : 'value'})`);
    });

    console.log('\n🎉 Hydration complete! Your Edge Config now contains all TMNT data.');
    console.log('\n📊 Next steps:');
    console.log('1. Deploy your application: vercel --prod');
    console.log('2. Check the health endpoint to verify Edge Config connection');
    console.log('3. Monitor reduced function invocations in your Vercel dashboard');

  } catch (error) {
    console.error('❌ Failed to update Edge Config:', error.message);
    console.error('\nTroubleshooting:');
    console.error('1. Verify your VERCEL_TOKEN is valid');
    console.error('2. Check that EDGE_CONFIG_ID matches your Edge Config');
    console.error('3. For team accounts, ensure VERCEL_TEAM_ID is set');
    process.exit(1);
  }
}

// Run the hydration
updateEdgeConfig();