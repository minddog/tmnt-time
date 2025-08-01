import { mutation } from "./_generated/server";
import { v } from "convex/values";

// Create a new turtle
export const createTurtle = mutation({
  args: {
    name: v.string(),
    full_name: v.string(),
    color: v.string(),
    weapon: v.string(),
    personality: v.string(),
    favorite_pizza: v.string(),
    catchphrase: v.string(),
    image_url: v.string(),
  },
  handler: async (ctx, args) => {
    const turtleId = await ctx.db.insert("turtles", args);
    return turtleId;
  },
});

// Create a new villain
export const createVillain = mutation({
  args: {
    name: v.string(),
    real_name: v.optional(v.string()),
    description: v.string(),
    first_appearance: v.string(),
    abilities: v.array(v.string()),
    threat_level: v.string(),
    image_url: v.string(),
  },
  handler: async (ctx, args) => {
    const villainId = await ctx.db.insert("villains", args);
    return villainId;
  },
});

// Create a new episode
export const createEpisode = mutation({
  args: {
    episode_id: v.number(),
    title: v.string(),
    season: v.number(),
    episode_number: v.number(),
    air_date: v.string(),
    synopsis: v.string(),
  },
  handler: async (ctx, args) => {
    const episodeId = await ctx.db.insert("episodes", args);
    return episodeId;
  },
});

// Create a new quote
export const createQuote = mutation({
  args: {
    text: v.string(),
    character: v.string(),
    episode: v.optional(v.string()),
    context: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    // Convert null to undefined for optional fields
    const quoteData = {
      text: args.text,
      character: args.character,
      episode: args.episode || undefined,
      context: args.context || undefined,
    };
    const quoteId = await ctx.db.insert("quotes", quoteData);
    return quoteId;
  },
});

// Create a new weapon
export const createWeapon = mutation({
  args: {
    name: v.string(),
    wielder: v.string(),
    type: v.string(),
    description: v.string(),
    special_moves: v.array(v.string()),
  },
  handler: async (ctx, args) => {
    const weaponId = await ctx.db.insert("weapons", args);
    return weaponId;
  },
});

// Clear all data (useful for testing)
export const clearAllData = mutation({
  handler: async (ctx) => {
    // Delete all records from each table
    const tables = ["turtles", "villains", "episodes", "quotes", "weapons"];
    
    for (const table of tables) {
      const records = await ctx.db.query(table).collect();
      for (const record of records) {
        await ctx.db.delete(record._id);
      }
    }
    
    return { message: "All data cleared" };
  },
});