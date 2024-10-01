<!-- Inside src/components/Search/SearchResult.svelte -->
<script>
    export let result;
</script>

<li>
    <h3>{result.title}</h3>
    <p>{result.description}</p>
    <p><strong>Summary:</strong> {result.summary}</p>
    <a href={`/document/${result.document_id}`}>View Document</a>
</li>