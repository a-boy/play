import { sql, serve } from "bun";

const server = serve({
  port: 3000,
  routes: {
    "/": () => new Response("Welcome to Bun!"),
    "/api/users": async (req) => {
      const users = await sql`SELECT * FROM users LIMIT 10`;
      return Response.json({ users });
    },
  },
});

console.log(`Listening on localhost:${server.port}`);