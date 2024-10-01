<!-- frontend/src/routes/DocumentDetails.svelte -->
<script>
    import { onMount } from 'svelte';
    import { get } from 'svelte/store';
    import auth from '../stores/auth.js';

    export let id; // Document ID

    let documentDetails = null;
    let loading = true;
    let error = '';

    onMount(async () => {
        try {
            const response = await fetch(`http://localhost:8000/documents/details/${id}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${get(auth).token}`,
                }
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Failed to fetch document details');
            }

            documentDetails = await response.json();
        } catch (err) {
            console.error("Error fetching document details:", err);
            error = err.message;
        } finally {
            loading = false;
        }
    });
</script>

<main>
    {#if loading}
        <p>Loading document details...</p>
    {/if}

    {#if error}
        <p style="color: red;">{error}</p>
    {/if}

    {#if documentDetails}
        <h1>{documentDetails.title}</h1>
        <p><strong>Description:</strong> {documentDetails.description}</p>
        <p><strong>Summary:</strong></p>
        <pre>{documentDetails.summary}</pre>
        <p><strong>Content:</strong></p>
        <pre>{documentDetails.content}</pre>
        <p><strong>Uploaded By:</strong> {documentDetails.uploader.username} ({documentDetails.uploader.email})</p>
        <p><strong>Upload Date:</strong> {new Date(documentDetails.uploaded_at).toLocaleString()}</p>
        <p><strong>Tags:</strong> {documentDetails.tags.join(', ')}</p>
    {/if}
</main>

<style>
    main {
        padding: 1em;
    }

    h1 {
        margin-bottom: 0.5em;
    }

    pre {
        background-color: #f5f5f5;
        padding: 1em;
        white-space: pre-wrap;
        word-wrap: break-word;
        overflow-x: auto;
    }

    p {
        margin: 0.5em 0;
    }
</style>