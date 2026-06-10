# Windows 2000 UI React Component Library

A nostalgic recreation of the Windows 2000 user interface using React and TypeScript. This project includes a reusable component library with authentic Win2000 styling and a demo showcase application.

## Features

- **Authentic Win2000 Styling**: Beveled borders, classic gray color scheme, iconic UI elements
- **Draggable Windows**: Full drag-and-drop window functionality
- **Component Library**: Reusable React components with TypeScript support
- **Taskbar**: System taskbar with window management
- **Responsive Design**: Demo application with multiple interactive windows

## Project Structure

```
win2000/
├── packages/
│   ├── components/          # React component library
│   │   ├── src/
│   │   │   ├── components/  # Individual components (Window, Button, etc.)
│   │   │   ├── styles/      # Global styles
│   │   │   └── index.ts     # Library entry point
│   │   └── package.json
│   └── demo/                # Demo showcase app
│       ├── src/
│       │   ├── App.tsx      # Main demo application
│       │   └── index.css    # Global styles
│       ├── public/
│       │   └── index.html
│       └── package.json
└── package.json (monorepo root)
```

## Installation

```bash
# Install dependencies for all packages
npm install

# Install dependencies for specific package
npm install -w @win2000/components
npm install -w @win2000/demo
```

## Development

```bash
# Run demo app in development mode
npm run dev
# or
npm run demo:dev

# Build component library
npm run components:build

# Build everything
npm run build
```

## Components

### Window
Draggable window component with titlebar and close button.

```tsx
<Window
  title="My Window"
  width={400}
  height={300}
  x={100}
  y={100}
  onClose={() => console.log('closed')}
>
  Window content here
</Window>
```

### Button
Classic Windows 2000 styled button.

```tsx
<Button onClick={() => alert('Clicked!')}>Click Me</Button>
```

### Taskbar
System taskbar component.

```tsx
<Taskbar
  items={[{ id: '1', label: 'Window 1' }]}
  onItemClick={(id) => console.log(id)}
/>
```

## Styling

Components use authentic Windows 2000 styling including:
- Classic gray (#dfdfdf) background
- Beveled borders with highlight and shadow
- Teal (#008080) desktop background
- Blue window titlebars
- System font styling

## Browser Compatibility

Modern browsers (Chrome, Firefox, Safari, Edge)

## License

ISC
