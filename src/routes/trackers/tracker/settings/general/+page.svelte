 
<script>
    import Trackernav from "../../../../../lib/Trackernav.svelte";
    import firebase_auth from "../../../../../lib/auth";
    import { page } from "$app/stores"
    const id = $page.data.id
    import { onMount } from "svelte";
    import { onAuthStateChanged } from "@firebase/auth";
    let acts = []
    let balance
    let currency
    let tracker
    onMount(() => { 
    onAuthStateChanged(firebase_auth, (user) => {
        if (user) {
            fetch(`https://bltrackerbackenddeploy.onrender.com/getTrackerInfo?id=${id}`)
                .then((response) => response.json())
                .then((json) => {
                    const pd = JSON.parse(json.DATA);
                    const act = pd[0].act;
                    const balances = pd[0].balance;
                    const currencies = pd[0].currency;
                    const name = pd[0].name
                    console.log(pd, act, balances, currencies);

                    if (pd[0].ownerid === user.uid) {
                  
                    } else {
                        window.location.href = "/home"
                    }

                    acts = act;
                    balance = balances;
                    currency = currencies;
                    tracker = name
                })
                .catch((error) => {
                    console.error("Error fetching tracker information:", error);
                });
        } else {
           window.location.href = "/"
        }
    });
});


    
</script>

<Trackernav id={id}/>

<div class="container">
    <br>
    <div class="row">
        <div class="col-md-3">
            <ul class="list-group">
                <li class="list-group-item">General</li>
            </ul>
        </div>
        <div class="col-md-4 border rounded" style="width: 32rem;">
            <h1>{tracker} - Settings</h1>
        </div>
    </div>
</div>
