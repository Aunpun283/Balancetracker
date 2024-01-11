<script>
    import { firebase_auth } from "$lib"
    import { signInWithEmailAndPassword } from "@firebase/auth"
    let emi = ""
    let pwi = ""
    function signin() {
        signInWithEmailAndPassword(firebase_auth, emi, pwi)
            .then((usercred) => {
                window.location.href = "/home"
            }).catch((error) => {
                if (error.message == "Firebase: Error (auth/invalid-credential).") { alert("Incorect credentials, Please try again.")}
                else { alert("login error " + error.messagegi) }
            })
    }
</script>

<div id="div-center">
    <h1 class="text-center">Sign in to balance tracker using KACCOUNT</h1>
    <form  on:submit|preventDefault={signin}>
        <div class="mb-3">
            <label for="emi" class="fcoorm-label">Email:</label>
            <input type="email" required placeholder="Your email"  bind:value={emi} class="form-control">
        </div>
        <div class="mb-3">
            <label for="pwi" class="form-label">Password:</label>
            <input type="password" required placeholder="Your password" bind:value={pwi}  class="form-control">
        </div>
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-success">Sign in</button>
        </div>
        <hr>
        <div class="d-grid gap-2">
            <a class="btn btn-primary" href="https://authenthication-2ba09.firebaseapp.com/" target="_blank">Sign up (KAccount)</a>
        </div>
    </form>
</div>
