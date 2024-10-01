<!-- src/components/Documents/DocumentUpload.svelte -->
<script>
    import auth from '../../stores/auth.js';
    import { onDestroy } from 'svelte';

    let selectedFile = null;
    let uploadStatus = '';
    let error = '';
    let authState;
    let title = '';
    let description = '';
    let tags = '';

    const unsubscribe = auth.subscribe(value => {
        authState = value;
    });

    const handleFileChange = (event) => {
        selectedFile = event.target.files[0];
    };

    const handleUpload = async () => {
        uploadStatus = '';
        error = '';

        if (!selectedFile) {
            error = "Please select a file to upload.";
            return;
        }

        if (!title.trim()) {
            error = "Please provide a title for the document.";
            return;
        }

        const formData = new FormData();
        formData.append('file', selectedFile);
        formData.append('title', title);
        formData.append('description', description);

        // assume comma-separated input
        const tagsArray = tags.split(',').map(tag => tag.trim()).filter(tag => tag);
        tagsArray.forEach(tag => formData.append('tags', tag));

        try {
            const response = await fetch('http://localhost:8000/documents/upload/', {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${authState.token}`,
                    // Do NOT set 'Content-Type' header when sending FormData
                },
                body: formData,
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Upload failed');
            }

            uploadStatus = "Document uploaded successfully!";

            selectedFile = null;
            title = '';
            description = '';
            tags = '';
        } catch (err) {
            error = err.message;
        }
    };

    onDestroy(() => {
        unsubscribe();
    });
</script>

<main>
    <h2>Upload Document</h2>
    {#if error}
        <p style="color: red;">{error}</p>
    {/if}
    {#if uploadStatus}
        <p style="color: green;">{uploadStatus}</p>
    {/if}
    <div>
        <label for="file">Select File:</label>
        <input type="file" id="file" on:change={handleFileChange} />
    </div>
    <div>
        <label for="title">Title:</label>
        <input type="text" id="title" bind:value={title} required />
    </div>
    <div>
        <label for="description">Description:</label>
        <textarea id="description" bind:value={description}></textarea>
    </div>
    <div>
        <label for="tags">Tags (comma separated):</label>
        <input type="text" id="tags" bind:value={tags} />
    </div>
    <button on:click={handleUpload}>Upload</button>
</main>

<style>
    /* Add your styles here */
    main {
        padding: 1em;
    }

    div {
        margin-bottom: 1em;
    }

    label {
        display: block;
        margin-bottom: 0.5em;
    }

    input, textarea {
        width: 100%;
        padding: 0.5em;
        box-sizing: border-box;
    }

    button {
        padding: 0.7em 1.5em;
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
