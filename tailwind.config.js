/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './task_manager/templates/**/*.html',
    './task_manager/**/*.py',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}