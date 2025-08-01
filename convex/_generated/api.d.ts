/* eslint-disable */
/**
 * Generated `api` utility.
 *
 * THIS CODE IS AUTOMATICALLY GENERATED.
 *
 * To regenerate, run `npx convex dev`.
 * @module
 */

import type {
  ApiFromModules,
  FilterApi,
  FunctionReference,
} from "convex/server";
import type * as episodes from "../episodes.js";
import type * as mutations from "../mutations.js";
import type * as quotes from "../quotes.js";
import type * as turtles from "../turtles.js";
import type * as villains from "../villains.js";
import type * as weapons from "../weapons.js";

/**
 * A utility for referencing Convex functions in your app's API.
 *
 * Usage:
 * ```js
 * const myFunctionReference = api.myModule.myFunction;
 * ```
 */
declare const fullApi: ApiFromModules<{
  episodes: typeof episodes;
  mutations: typeof mutations;
  quotes: typeof quotes;
  turtles: typeof turtles;
  villains: typeof villains;
  weapons: typeof weapons;
}>;
export declare const api: FilterApi<
  typeof fullApi,
  FunctionReference<any, "public">
>;
export declare const internal: FilterApi<
  typeof fullApi,
  FunctionReference<any, "internal">
>;
