// frontend/src/stores/auth.js
import { writable } from 'svelte/store';

// Function to load auth state from localStorage
const loadAuth = () => {
    const storedAuth = localStorage.getItem('auth');
    return storedAuth ? JSON.parse(storedAuth) : { isAuthenticated: false, token: null, user: null };
};

// Initialize the auth store
const auth = writable(loadAuth());

// Subscribe to store changes and persist to localStorage
auth.subscribe(value => {
    localStorage.setItem('auth', JSON.stringify(value));
});

export default auth;
