import { query } from "./_generated/server";
import { v } from "convex/values";

// Get all turtles
export const getAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("turtles").collect();
  },
});

// Get a specific turtle by name
export const getByName = query({
  args: { name: v.string() },
  handler: async (ctx, args) => {
    const turtle = await ctx.db
      .query("turtles")
      .withIndex("by_name", (q) => q.eq("name", args.name))
      .first();
    
    if (!turtle) {
      throw new Error(`Turtle '${args.name}' not found`);
    }
    
    return turtle;
  },
});