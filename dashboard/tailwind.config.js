/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'trading-black': '#0a0a0a',
        'trading-dark': '#121212',
        'trading-green': '#00ff41', 
      }
    },
  },
  plugins: [],
}