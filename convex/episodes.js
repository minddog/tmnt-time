import { query, mutation } from "./_generated/server";
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

// Add a new episode
export const addEpisode = mutation({
  args: {
    episode_id: v.number(),
    title: v.string(),
    season: v.number(),
    episode_number: v.number(),
    air_date: v.string(),
    synopsis: v.string(),
    cast: v.optional(v.array(v.object({
      character_name: v.string(),
      voice_actor: v.string(),
      role: v.string(),
    }))),
    writer: v.optional(v.string()),
    director: v.optional(v.string()),
    notes: v.optional(v.string()),
    villains_featured: v.optional(v.array(v.string())),
  },
  handler: async (ctx, args) => {
    // Check if episode already exists
    const existing = await ctx.db
      .query("episodes")
      .withIndex("by_episode_id", (q) => q.eq("episode_id", args.episode_id))
      .first();
    
    if (existing) {
      throw new Error(`Episode ${args.episode_id} already exists`);
    }
    
    // Add the episode
    await ctx.db.insert("episodes", args);
    
    return { success: true, episode_id: args.episode_id };
  },
});

// Update episode with cast and production information
export const updateEpisode = mutation({
  args: {
    episode_id: v.number(),
    cast: v.optional(v.array(v.object({
      character_name: v.string(),
      voice_actor: v.string(),
      role: v.string(),
    }))),
    writer: v.optional(v.string()),
    director: v.optional(v.string()),
    notes: v.optional(v.string()),
    villains_featured: v.optional(v.array(v.string())),
  },
  handler: async (ctx, args) => {
    // Find the episode
    const episode = await ctx.db
      .query("episodes")
      .withIndex("by_episode_id", (q) => q.eq("episode_id", args.episode_id))
      .first();
    
    if (!episode) {
      throw new Error(`Episode ${args.episode_id} not found`);
    }
    
    // Update the episode
    const updates = {};
    if (args.cast !== undefined) updates.cast = args.cast;
    if (args.writer !== undefined) updates.writer = args.writer;
    if (args.director !== undefined) updates.director = args.director;
    if (args.notes !== undefined) updates.notes = args.notes;
    if (args.villains_featured !== undefined) updates.villains_featured = args.villains_featured;
    
    await ctx.db.patch(episode._id, updates);
    
    return { success: true, episode_id: args.episode_id };
  },
});

// Delete an episode by its Convex ID
export const deleteById = mutation({
  args: { id: v.id("episodes") },
  handler: async (ctx, args) => {
    await ctx.db.delete(args.id);
    return { success: true };
  },
});