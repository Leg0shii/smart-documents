<!-- src/routes/Upload.svelte -->
<script>
    import {onDestroy, onMount} from 'svelte';
    import { navigate } from 'svelte-routing';
    import auth from '../stores/auth.js';
    import DocumentUpload from '../components/Documents/DocumentUpload.svelte';

    let authState;

    const unsubscribe = auth.subscribe(value => {
        authState = value;
    });

    onMount(() => {
        if (!authState.isAuthenticated) {
            navigate('/login');
        }
    });

    onDestroy(() => {
        unsubscribe();
    });
</script>

{#if authState.isAuthenticated}
    <DocumentUpload />
{/if}
