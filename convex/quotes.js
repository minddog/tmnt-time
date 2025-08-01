import { query } from "./_generated/server";
import { v } from "convex/values";

// Get all quotes
export const getAll = query({
  args: {
    character: v.optional(v.string()),
  },
  handler: async (ctx, args) => {
    if (args.character) {
      return await ctx.db
        .query("quotes")
        .withIndex("by_character", (q) => q.eq("character", args.character))
        .collect();
    }
    
    return await ctx.db.query("quotes").collect();
  },
});

// Get a random quote
export const getRandom = query({
  args: {
    seed: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const quotes = await ctx.db.query("quotes").collect();
    
    if (quotes.length === 0) {
      throw new Error("No quotes available");
    }
    
    // Use seed if provided, otherwise use random
    const seed = args.seed || Math.floor(Math.random() * 10000);
    const randomIndex = seed % quotes.length;
    return quotes[randomIndex];
  },
});