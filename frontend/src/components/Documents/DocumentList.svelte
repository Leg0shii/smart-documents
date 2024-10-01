<!-- frontend/src/components/Documents/DocumentList.svelte -->
<script>
    import {onMount} from 'svelte';
    import auth from '../../stores/auth.js';
    import {get} from 'svelte/store';
    import SearchResult from "../Search/SearchResult.svelte";

    let documents = [];
    let error = '';
    let loading = false;

    onMount(async () => {
        loading = true;
        try {
            const response = await fetch('http://localhost:8000/documents/', {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${get(auth).token}`,
                },
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Failed to fetch documents');
            }

            documents = await response.json();
        } catch (err) {
            error = err.message;
        } finally {
            loading = false;
        }
    });
</script>

<main>
    <h2>Your Documents</h2>
    {#if loading}
        <p>Loading documents...</p>
    {/if}

    {#if error}
        <p style="color: red;">{error}</p>
    {/if}

    {#if documents.length > 0}
        <ul>
            {#each documents as doc}
                <li>
                    <h3>{doc.title}</h3>
                    <p>{doc.description}</p>
                    <a href={`/summary/${doc.id}`}>View Summary</a>
                    <a href={`/document/${doc.id}`}>View Document</a>
                </li>
            {/each}
        </ul>
    {:else if !loading && !error}
        <p>No documents found.</p>
    {/if}
</main>

<style>
    main {
        padding: 1em;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    li {
        border: 1px solid #ccc;
        padding: 1em;
        border-radius: 5px;
        margin-bottom: 1em;
    }

    h3 {
        margin: 0 0 0.5em 0;
    }
</style>
