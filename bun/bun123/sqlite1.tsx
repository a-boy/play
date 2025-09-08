import { Database } from "bun:sqlite";

const db = new Database("db.sqlite");

console.log(db.query("SELECT 1 as x").get()); 
// { x: 1 }
db.exec("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT);");
db.exec("INSERT INTO users (name) VALUES (?)", ["Alice"]);
db.exec("INSERT INTO users (name) VALUES (?)", ["Bob"]);
console.log(db.query("select * from users LIMIT 3").get());