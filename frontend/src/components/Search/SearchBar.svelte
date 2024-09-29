<!-- src/components/Search/SearchBar.svelte -->
<script>
    import { createEventDispatcher } from 'svelte';

    let query = '';
    let topK = 5;

    const dispatch = createEventDispatcher();

    const handleSearch = () => {
        if (query.trim() === '') return;
        dispatch('search', { query, topK });
    };
</script>

<div>
    <input
        type="text"
        placeholder="Search documents..."
        bind:value={query}
        on:keydown={(e) => e.key === 'Enter' && handleSearch()}
    />
    <input
        type="number"
        min="1"
        max="100"
        bind:value={topK}
        placeholder="Top K"
    />
    <button on:click={handleSearch}>Search</button>
</div>

<style>
    /* Add your styles here */
    div {
        display: flex;
        gap: 0.5em;
        margin-bottom: 1em;
    }

    input {
        padding: 0.5em;
        flex: 1;
    }

    button {
        padding: 0.5em 1em;
    }
</style>
