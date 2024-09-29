// src/main.js
import App from './App.svelte';
import '../public/global.css'; // Import global styles

const app = new App({
  target: document.body,
  props: {
    name: 'User'
  }
});

export default app;