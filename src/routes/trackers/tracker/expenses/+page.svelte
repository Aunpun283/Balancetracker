 
<script>
    import Trackernav from "../../../../lib/Trackernav.svelte";
    import { page } from "$app/stores"
    const id = $page.data.id
    import { onMount } from "svelte";
    import { onAuthStateChanged } from "@firebase/auth";
    import firebase_auth from "../../../../lib/auth";
    let expenses = []
    let balance
    let currency
    onMount(() => { 
    onAuthStateChanged(firebase_auth, (user) => {
        if (user) {
            fetch(`http://localhost:8000/getTrackerInfo?id=${id}`)
                .then((response) => response.json())
                .then((json) => {
                    const pd = JSON.parse(json.DATA);
                    const expense1 = pd[0].expenses;
                    const balances = pd[0].balance;
                    const currencies = pd[0].currency;

                    console.log(pd, expense1, balances, currencies);

                    if (pd[0].ownerid === user.uid) {
                  
                    } else {
                        window.location.href = "/home"
                    }

                    expenses = expense1;
                    balance = balances;
                    currency = currencies;
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
    <h1 class="text-center">Expenses board</h1>
    {#if balance  >= 0}
    <h1 class="text-center">You have {balance} {currency}</h1>
    {:else}
    <h1 class="text-center"  >You have <span style="color: red;">{balance}</span> {currency}</h1>    {/if}
    <table class="table table-striped"
    >
        <thead>
            <tr>
                <th scope="col">Type</th>
                <th scope="col">Money</th>
                <th scope="col">Need/Want</th>
                <th scope="col">Notes</th>
                <th scope="col">Item (Purchase)</th>
            </tr>
        </thead>

        <tbody>
            {#each expenses as expense}
            <tr> 
                <th scope="row">{expense.type}</th>
                <th scope="row">{expense.money}</th>
                <th scope="row">{expense.needwant}</th>
                <th scope="row">{expense.notes}</th>
                <th scope="row">{expense.item}</th>
            </tr>
            {/each}
            <tr> 
                <th scope="row">Total:</th>
                <th scope="row">⠀</th>
                <th scope="row">⠀</th>
                <th scope="row">{balance}</th>
                <th scope="row">{currency}</th>
            </tr>
        </tbody>
    </table>
</div>