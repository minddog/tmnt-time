# Convex Backend Functions

This directory contains the Convex backend functions for the TMNT API.

## Setup

1. Run `npx convex dev` to start the Convex development server
2. This will prompt you to log in with GitHub and create a project
3. The deployment URL will be saved in `.env.local`

## Functions

- `getTurtles.js` - Query all turtles
- `getTurtle.js` - Query a specific turtle by name
- `getVillains.js` - Query all villains
- `getVillain.js` - Query a specific villain by name
- `getEpisodes.js` - Query episodes with pagination
- `getEpisode.js` - Query a specific episode by ID
- `getQuotes.js` - Query all quotes
- `getRandomQuote.js` - Get a random quote
- `getWeapons.js` - Query all weapons

## Schema

The schema is defined in `schema.ts` with tables for:
- turtles
- villains
- episodes
- quotes
- weapons