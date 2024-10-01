// frontend/src/stores/auth.js
import { writable } from 'svelte/store';

// load auth state from localStorage
const loadAuth = () => {
    const storedAuth = localStorage.getItem('auth');
    return storedAuth ? JSON.parse(storedAuth) : { isAuthenticated: false, token: null, user: null };
};

const auth = writable(loadAuth());
auth.subscribe(value => {
    localStorage.setItem('auth', JSON.stringify(value));
});

export default auth;
