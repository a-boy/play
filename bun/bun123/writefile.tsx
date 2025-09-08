const file = Bun.file(import.meta.dir + '/j123.json'); // BunFile

const pkg = await file.json(); // BunFile extends Blob
pkg.name = 'my-package';
pkg.version = '1.2.0';

await Bun.write(file, JSON.stringify(pkg, null, 2));
