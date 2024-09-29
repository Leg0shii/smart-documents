<!-- frontend/src/App.svelte -->
<script>
    import { Router, Route } from 'svelte-routing';
    import Navbar from './components/Navbar.svelte';
    import Home from './routes/Home.svelte';
    import Login from './routes/Login.svelte';
    import Register from './routes/Register.svelte';
    import Upload from './routes/Upload.svelte';
    import Search from './routes/Search.svelte';
    import Summary from './routes/Summary.svelte';
</script>

<Navbar />

<Router>
    <Route path="/" component={Home} />
    <Route path="/login" component={Login} />
    <Route path="/register" component={Register} />
    <Route path="/upload" component={Upload} />
    <Route path="/search" component={Search} />
    <Route path="/summary/:id" component={Summary} />
</Router>

<style>
    /* Global styles can go here */
</style>
