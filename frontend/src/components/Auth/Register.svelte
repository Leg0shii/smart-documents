<!-- frontend/src/components/Auth/Register.svelte -->
<script>
    import { navigate } from 'svelte-routing';
    import auth from '../../stores/auth.js';

    let username = '';
    let email = '';
    let password = '';
    let confirmPassword = '';
    let error = '';

    const handleRegister = async () => {
        if (password !== confirmPassword) {
            error = "Passwords do not match.";
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/auth/register/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password, email }),
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Registration failed');
            }

            // automatic login after register
            const loginResponse = await fetch('http://localhost:8000/auth/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (!loginResponse.ok) {
                const data = await loginResponse.json();
                throw new Error(data.detail || 'Login after registration failed');
            }

            const loginData = await loginResponse.json();

            auth.set({
                isAuthenticated: true,
                token: loginData.access_token,
                user: { username }
            });

            // redirect home
            navigate('/');
        } catch (err) {
            error = err.message;
        }
    };
</script>

<main>
    <h2>Register</h2>
    {#if error}
        <p style="color: red;">{error}</p>
    {/if}
    <form on:submit|preventDefault={handleRegister}>
        <div>
            <label for="username">Username:</label>
            <input id="username" type="text" bind:value={username} required />
        </div>
        <div>
            <label for="email">E-Mail:</label>
            <input id="email" type="email" bind:value={email} required />
        </div>
        <div>
            <label for="password">Password:</label>
            <input id="password" type="password" bind:value={password} required />
        </div>
        <div>
            <label for="confirmPassword">Confirm Password:</label>
            <input id="confirmPassword" type="password" bind:value={confirmPassword} required />
        </div>
        <button type="submit">Register</button>
    </form>
</main>

<style>
    main {
        max-width: 400px;
        margin: 0 auto;
        padding: 1em;
    }

    form div {
        margin-bottom: 1em;
    }

    label {
        display: block;
        margin-bottom: 0.5em;
        font-weight: bold;
    }

    input {
        width: 100%;
        padding: 0.5em;
        box-sizing: border-box;
        border: 1px solid #ccc;
        border-radius: 4px;
    }

    button {
        width: 100%;
        padding: 0.7em;
        background-color: #ff3e00;
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        font-size: 1em;
    }

    button:hover {
        background-color: #e63e00;
    }
</style>
