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
  args: {},
  handler: async (ctx) => {
    const quotes = await ctx.db.query("quotes").collect();
    
    if (quotes.length === 0) {
      throw new Error("No quotes available");
    }
    
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
  },
});