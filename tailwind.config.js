// tailwind.config.js
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
    "./public/index.html"
  ],
  theme: {
    extend: {
      colors: {
        customPurple: {
          light: '#9b59b6', 
          DEFAULT: '#800080', 
          dark: '#4b0082', 
        }, 
      }
    },
  },
  plugins: [],
}
