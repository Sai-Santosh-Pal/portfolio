/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./index.html",
      "./src/**/*.{js,ts,jsx,tsx}", // Adjust based on your file structure
    ],
    theme: {
      extend: {
        backgroundImage: {
          'gradient-radial': 'radial-gradient(var(--tw-gradient-stops))',
        },
        colors: {
          glowPurple: '#a855f7', // Optional: custom color names
          glowBlue: '#3b82f6',
          glowPink: '#ec4899',
        },
      },
    },
    plugins: [],
  }
  