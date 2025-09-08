import { H3, serve } from "h3";

const app = new H3().get("/", (event) => "⚡️ Tadaa!");

serve(app, { port: 3000 });
