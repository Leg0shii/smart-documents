<!-- Inside src/components/Search/SearchResult.svelte -->
<script>
    import { Link } from 'svelte-routing';
    export let result;
</script>

<li>
    <h3>{result.title}</h3>
    <p>{result.description}</p>
    <p><strong>Summary:</strong> {result.summary}</p>
    <a href={`/summary/${result.document_id}`}>View Summary</a>
    <a href={`/document/${result.document_id}`}>View Document</a>
</li>