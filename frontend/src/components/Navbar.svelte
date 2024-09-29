<!-- src/components/Navbar.svelte -->
<script>
    import auth from '../stores/auth.js';
    import { onDestroy } from 'svelte';

    let authState;

    const unsubscribe = auth.subscribe(value => {
        authState = value;
    });

    const handleLogout = () => {
        auth.set({
            isAuthenticated: false,
            token: null,
            user: null,
        });
        window.location.href = '/login'; // Redirect to login page
    };

    onDestroy(() => {
        unsubscribe();
    });
</script>

<nav>
    <a href="/">Home</a>
    {#if authState.isAuthenticated}
        <a href="/upload">Upload Document</a>
        <a href="/search">Search</a>
        <button on:click={handleLogout}>Logout</button>
    {:else}
        <a href="/login">Login</a>
        <a href="/register">Register</a>
    {/if}
</nav>

<style>
    nav {
        display: flex;
        gap: 1em;
        padding: 1em;
        background-color: #f0f0f0;
    }

    a {
        text-decoration: none;
        color: #333;
    }

    button {
        background: none;
        border: none;
        color: #333;
        cursor: pointer;
        font: inherit;
    }
</style>
