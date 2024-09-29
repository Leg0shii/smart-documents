<!-- frontend/src/components/Auth/Login.svelte -->
<script>
    import { navigate } from 'svelte-routing';
    import auth from '../../stores/auth.js';
    let username = '';
    let password = '';
    let error = '';

    const handleLogin = async () => {
        try {
            const response = await fetch('http://localhost:8000/auth/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Login failed');
            }

            const data = await response.json();
            auth.set({
                isAuthenticated: true,
                token: data.access_token,
                user: data.user,
            });

            navigate('/'); // Redirect to home after successful login
        } catch (err) {
            error = err.message;
        }
    };
</script>

<main>
    <h2>Login</h2>
    {#if error}
        <p style="color: red;">{error}</p>
    {/if}
    <form on:submit|preventDefault={handleLogin}>
        <div>
            <label for="username">Username:</label>
            <input id="username" type="text" bind:value={username} required />
        </div>
        <div>
            <label for="password">Password:</label>
            <input id="password" type="password" bind:value={password} required />
        </div>
        <button type="submit">Login</button>
    </form>
</main>

<style>
    main {
        max-width: 400px;
        margin: 0 auto;
    }

    form div {
        margin-bottom: 1em;
    }

    label {
        display: block;
        margin-bottom: 0.5em;
    }

    input {
        width: 100%;
        padding: 0.5em;
        box-sizing: border-box;
    }

    button {
        width: 100%;
        padding: 0.7em;
        background-color: #ff3e00;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }

    button:hover {
        background-color: #e63e00;
    }
</style>
