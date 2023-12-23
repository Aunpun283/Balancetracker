<script>
    import auth from "./auth"
    import { signOut, onAuthStateChanged } from "@firebase/auth"
  
    function signout() {
        signOut(auth)
        window.location.href = "/"
    }
</script>

<nav class="navbar navbar-dark bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
        <a href="/home" class="navbar-brand">Second try balance tracker</a>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/create" class="nav-link active" active>Create a new tracker</a>
            </li>
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
                <button class="nav-link active" on:click={signout}>Sign out</button>
            </li>
        </ul>
    </div>
</nav>