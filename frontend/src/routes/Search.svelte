<!-- src/routes/Search.svelte -->
<script>
    import SearchBar from '../components/Search/SearchBar.svelte';
    import SearchResult from '../components/Search/SearchResult.svelte';
    import auth from '../stores/auth.js';
    import { onDestroy } from 'svelte';

    let authState;
    let results = [];
    let error = '';
    let loading = false;

    const unsubscribe = auth.subscribe(value => {
        authState = value;
    });

    const handleSearch = async (event) => {
        const { query, topK } = event.detail;
        loading = true;
        error = '';
        results = [];

        try {
            const response = await fetch('http://localhost:8000/search/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${authState.token}`,
                },
                body: JSON.stringify({ query, top_k: topK }),
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Search failed');
            }

            results = await response.json();
        } catch (err) {
            error = err.message;
        } finally {
            loading = false;
        }
    };

    onDestroy(() => {
        unsubscribe();
    });
</script>

<main>
    <h2>Search Documents</h2>
    <SearchBar on:search={handleSearch} />

    {#if loading}
        <p>Loading...</p>
    {/if}

    {#if error}
        <p style="color: red;">{error}</p>
    {/if}

    {#if results.length > 0}
        <ul>
            {#each results as result}
                <SearchResult {result} />
            {/each}
        </ul>
    {:else if !loading && !error}
        <p>No results found.</p>
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
</style>
