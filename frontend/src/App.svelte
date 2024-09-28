<!-- frontend/src/App.svelte -->
<script>
    import {onMount} from 'svelte';

    export let name;
    let apiMessage = "Loading...";

    // Fetch the message when the component is mounted
    onMount(async () => {
        try {
            const response = await fetch('http://localhost:8000/api/message');
            const data = await response.json();
            apiMessage = data.message;
        } catch (error) {
            console.error('Error fetching API message:', error);
            apiMessage = "Failed to load message.";
        }
    });
</script>

<main>
    <h1>Hello {name}!</h1>
    <p>{apiMessage}</p>
    <p>Visit the <a href="https://svelte.dev/tutorial">Svelte tutorial</a> to learn how to build Svelte apps.</p>
    <p>This is some text ye</p>
</main>

<style>
    main {
        text-align: center;
        padding: 1em;
        max-width: 240px;
        margin: 0 auto;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>