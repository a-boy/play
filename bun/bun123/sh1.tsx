import { $ } from 'bun';

// Run a shell command (also works on Windows!)
await $`echo "Hello, world!"`;

const response = await fetch("https://bing.com");

// Pipe the response body to gzip
const data = await $`gzip < ${response}`.arrayBuffer();