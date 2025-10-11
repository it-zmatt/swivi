# React + Vite + Tailwind CSS Setup Guide

## Prerequisites
- Node.js 18+ and npm 9+ installed
- Basic knowledge of React and terminal commands

## Step-by-Step Instructions

### 1. Create Vite Project
```bash
npm create vite@latest my-react-app -- --template react
```
Or with TypeScript:
```bash
npm create vite@latest my-react-app -- --template react-ts
```

### 2. Navigate to Project Directory
```bash
cd my-react-app
```

### 3. Install Dependencies
```bash
npm install
```

### 4. Install Tailwind CSS and Dependencies
```bash
npm install -D tailwindcss postcss autoprefixer
```

### 5. Initialize Tailwind CSS
```bash
npx tailwindcss init -p
```
This creates `tailwind.config.js` and `postcss.config.js` files.

### 6. Configure Tailwind CSS
Update `tailwind.config.js`:
```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

### 7. Add Tailwind Directives to CSS
Replace contents of `src/index.css`:
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### 8. Clean Up Default Files
Remove default Vite styling from `src/App.css` or delete it entirely and remove the import from `App.jsx`.

### 9. Test Tailwind Setup
Replace `src/App.jsx` with:
```jsx
function App() {
  return (
    <div className="min-h-screen bg-gradient-to-r from-blue-500 to-purple-600 flex items-center justify-center">
      <h1 className="text-4xl font-bold text-white">
        React + Vite + Tailwind CSS
      </h1>
    </div>
  )
}

export default App
```

### 10. Start Development Server
```bash
npm run dev
```
Your app will be available at `http://localhost:5173`

## Optional Enhancements

### Add React Router
```bash
npm install react-router-dom
```

### Add Component Library (shadcn/ui)
```bash
npx shadcn@latest init
```

### Add Icons
```bash
npm install lucide-react
# or
npm install react-icons
```

### Add State Management
```bash
npm install @reduxjs/toolkit react-redux
# or
npm install zustand
```

### Add Forms Management
```bash
npm install react-hook-form zod
```

## Project Structure
```
my-react-app/
├── node_modules/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   ├── App.jsx
│   ├── index.css
│   └── main.jsx
├── .gitignore
├── index.html
├── package.json
├── postcss.config.js
├── tailwind.config.js
└── vite.config.js
```

## Build for Production
```bash
npm run build
```
This creates optimized production files in the `dist` folder.

## Preview Production Build
```bash
npm run preview
```

## Useful Scripts
Add to `package.json`:
```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  }
}
```

## Environment Variables
Create `.env` file in root:
```
VITE_API_URL=https://api.example.com
```
Access in code:
```javascript
const apiUrl = import.meta.env.VITE_API_URL
```

## Tips
- Vite uses ES modules by default
- Hot Module Replacement (HMR) works out of the box
- Use `className` instead of `class` in JSX
- Install Tailwind CSS IntelliSense VSCode extension for better DX
- Use `@apply` directive in CSS for reusable component styles

## Common Issues & Solutions
- **Port already in use**: Change port in `vite.config.js`
- **Tailwind not working**: Ensure `index.css` is imported in `main.jsx`
- **Build errors**: Clear node_modules and reinstall: `rm -rf node_modules && npm install`