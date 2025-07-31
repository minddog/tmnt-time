import { query } from "./_generated/server";

// Get all weapons
export const getAll = query({
  args: {},
  handler: async (ctx) => {
    return await ctx.db.query("weapons").collect();
  },
});