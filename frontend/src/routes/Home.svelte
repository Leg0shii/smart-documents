<!-- src/routes/Home.svelte -->
<script>
    import { onDestroy } from 'svelte';
    import auth from '../stores/auth.js';
    import { get } from 'svelte/store';

    let authState;

    const unsubscribe = auth.subscribe(value => {
        authState = value;
    });

    onDestroy(() => {
        unsubscribe();
    });
</script>

<main>
    <h1>Welcome to Smart Documents</h1>
    {#if authState.isAuthenticated && authState.user}
        <p>Welcome back, {authState.user.username}!</p>
    {:else}
        <p>Please <a href="/login">login</a> or <a href="/register">register</a> to continue.</p>
    {/if}
</main>

<style>
    main {
        padding: 1em;
        text-align: center;
    }

    a {
        text-decoration: none;
        color: #ff3e00;
    }
</style>
