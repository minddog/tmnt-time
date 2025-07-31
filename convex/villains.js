import { query } from "./_generated/server";
import { v } from "convex/values";

// Get all villains
export const getAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("villains").collect();
  },
});

// Get a specific villain by name
export const getByName = query({
  args: { name: v.string() },
  handler: async (ctx, args) => {
    const villain = await ctx.db
      .query("villains")
      .withIndex("by_name", (q) => q.eq("name", args.name))
      .first();
    
    if (!villain) {
      throw new Error(`Villain '${args.name}' not found`);
    }
    
    return villain;
  },
});