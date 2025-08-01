import { defineSchema, defineTable } from "convex/server";
import { v } from "convex/values";

export default defineSchema({
  turtles: defineTable({
    name: v.string(),
    full_name: v.string(),
    color: v.string(),
    weapon: v.string(),
    personality: v.string(),
    favorite_pizza: v.string(),
    catchphrase: v.string(),
    image_url: v.string(),
  }).index("by_name", ["name"]),

  villains: defineTable({
    name: v.string(),
    real_name: v.optional(v.string()),
    description: v.string(),
    abilities: v.array(v.string()),
    first_appearance: v.string(),
    threat_level: v.string(),
    image_url: v.string(),
  }).index("by_name", ["name"]),

  episodes: defineTable({
    episode_id: v.number(),
    title: v.string(),
    season: v.number(),
    episode_number: v.number(),
    air_date: v.string(),
    synopsis: v.string(),
    villains_featured: v.optional(v.array(v.string())),
    cast: v.optional(v.array(v.object({
      character_name: v.string(),
      voice_actor: v.string(),
      role: v.string(),
    }))),
    writer: v.optional(v.string()),
    director: v.optional(v.string()),
    notes: v.optional(v.string()),
  })
    .index("by_episode_id", ["episode_id"])
    .index("by_season", ["season"]),

  quotes: defineTable({
    text: v.string(),
    character: v.string(),
    episode: v.optional(v.string()),
    context: v.optional(v.string()),
  }).index("by_character", ["character"]),

  weapons: defineTable({
    name: v.string(),
    type: v.string(),
    wielder: v.string(),
    description: v.string(),
    special_moves: v.array(v.string()),
  }).index("by_wielder", ["wielder"]),
});