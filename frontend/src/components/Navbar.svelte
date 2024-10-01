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
        window.location.href = '/login';
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
        align-items: center;
        gap: 1em;
        padding: 1em;
        background-color: #f0f0f0;
    }

    button {
        background: none;
        border: none;
        color: #333;
        cursor: pointer;
        font: inherit;
    }

    a {
        padding: 0.5em;
        border: none;
        border-radius: 4px;
        text-decoration: none;
        color: #333;
    }

    a:hover {
        background-color: #e63e00;
    }
</style>
