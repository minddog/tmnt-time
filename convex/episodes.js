import { query } from "./_generated/server";
import { v } from "convex/values";

// Get episodes with optional filtering and pagination
export const getAll = query({
  args: {
    season: v.optional(v.number()),
    limit: v.optional(v.number()),
    offset: v.optional(v.number()),
  },
  handler: async (ctx, args) => {
    const limit = args.limit || 10;
    const offset = args.offset || 0;
    
    let episodesQuery = ctx.db.query("episodes");
    
    // Filter by season if provided
    if (args.season !== undefined) {
      episodesQuery = episodesQuery.withIndex("by_season", (q) => 
        q.eq("season", args.season)
      );
    }
    
    // Get all episodes and apply pagination
    const allEpisodes = await episodesQuery.collect();
    const paginatedEpisodes = allEpisodes.slice(offset, offset + limit);
    
    return paginatedEpisodes;
  },
});

// Get a specific episode by ID
export const getById = query({
  args: { episode_id: v.number() },
  handler: async (ctx, args) => {
    const episode = await ctx.db
      .query("episodes")
      .withIndex("by_episode_id", (q) => q.eq("episode_id", args.episode_id))
      .first();
    
    if (!episode) {
      throw new Error(`Episode ${args.episode_id} not found`);
    }
    
    return episode;
  },
});