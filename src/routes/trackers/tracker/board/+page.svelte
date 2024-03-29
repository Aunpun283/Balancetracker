 
<script>
    import Trackernav from "../../../../lib/Trackernav.svelte";
    import firebase_auth from "../../../../lib/auth";
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
            fetch(`https://balancetrackerbackend.onrender.com/getTrackerInfo?id=${id}`)
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
<div id="div-center">
    <h1 class="text-center">{tracker}</h1>
    <h1 class="text-center">Payment/Income board</h1>
    {#if balance  >= 0}
    <h1 class="text-center">You have {balance} {currency}</h1>
    {:else}
    <h1 class="text-center"  >You have <span style="color: red;">{balance}</span> {currency}</h1>    {/if}
    <table class="table table-striped"
    >
        <thead>
            <tr>
                <th scope="col">Payment/Income</th>
                <th scope="col">Money</th>
            
            </tr>
        </thead>

        <tbody>
            {#each acts as act}
            <tr> 
                <th scope="row">{act.t}</th>
                <th scope="row">{act.money}</th>
            
               
            </tr>
            {/each}
            <tr> 
                <th scope="row">Total:</th>
            
                <th scope="row">{balance} {currency}</th>
              
            </tr>
        </tbody>
    </table>
</div>