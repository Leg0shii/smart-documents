<!-- frontend/src/routes/Summary.svelte -->
<script>
    import { onMount } from 'svelte';
    import { get } from 'svelte/store';
    import auth from '../stores/auth.js';

    export let id; // Accept 'id' as a prop

    let summary = '';
    let loading = false;
    let error = '';

    const fetchSummary = async (documentId) => {
        loading = true;
        error = '';
        summary = '';

        try {
            const response = await fetch(`http://localhost:8000/summaries/${documentId}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${get(auth).token}`,
                }
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Failed to fetch summary');
            }

            const data = await response.json();
            summary = data.summary;
        } catch (err) {
            console.error("Error fetching summary:", err);
            error = err.message;
        } finally {
            loading = false;
        }
    };

    onMount(() => {
        if (!id) {
            error = 'Invalid document ID.';
            return;
        }
        fetchSummary(id);
    });
</script>

<main>
    {#if loading}
        <p>Loading summary...</p>
    {/if}

    {#if error}
        <p style="color: red;">{error}</p>
    {/if}

    {#if summary}
        <h2>Summary</h2>
        <p>{summary}</p>
    {/if}
</main>

<style>
    main {
        padding: 1em;
    }

    h2 {
        margin-bottom: 0.5em;
    }
</style>