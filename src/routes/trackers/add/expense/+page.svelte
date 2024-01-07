 
<script>
    import Trackernav from "../../../../lib/Trackernav.svelte";
    import { page } from "$app/stores"
    import firebase_auth from "../../../../lib/auth";
    import axios from "axios"
    import { onAuthStateChanged } from "@firebase/auth";
    import { onMount } from "svelte";
    const id = $page.data.id
    let expenseType = "Fee"
    let money = 0.00
    let notes = "-"
    let item = "-"
    let needwant = "Need"
    onMount(() => { 
    onAuthStateChanged(firebase_auth, (user) => {
        if (user) {
            fetch(`https://bltrackerbackenddeploy.onrender.com/getTrackerInfo?id=${id}`)
                .then((response) => response.json())
                .then((json) => {
                    const pd = JSON.parse(json.DATA);


                    if (pd[0].ownerid === user.uid) {
                  
                    } else {
                        window.location.href = "/home"
                    }

                })
                .catch((error) => {
                    console.error("Error fetching tracker information:", error);
                });
        } else {
           window.location.href = "/"
        }
    });
});
    function AddExpense() {
        axios.get(`https://bltrackerbackenddeploy.onrender.com/addExpense?et=${expenseType}&em=${money}&en=${notes}&nw=${needwant}&i=${item}&trackerid=${id}`)
        .then(response => {
                // Check if the tracker creation was successful before redirecting
                if (response.data.STATUS === "SUCCESS") {
                    window.location.href = "/trackers/tracker/expenses?id=" + id;
                } else {
                    alert(response.data.ERROR);
                }
            })
            .catch(error => {
                console.error("Error creating tracker:", error);
                alert("An error occurred while creating the tracker.");
            });
        
    }
</script>

<Trackernav id={id}/>

<div id="div-center">
    <form on:submit|preventDefault={AddExpense}>
        <h1>Add income</h1>
        <div class="mb-3">
            <label for="ti" class="form-label">Type of Income:</label>
            <select id="ti" class="form-select" bind:value={expenseType}>
                <option value="Fee">Fee</option>
                <option value="Paying off debt">Paying off debt</option>
                <option value="Purchase">Purchase</option>
            </select>
            
             
        </div>
        <div class="mb">
            <label for="mi" class="form-label">Modify type:</label>
            <input type="text" class="form-control" id="mi" bind:value={expenseType}>
        </div>
        <div class="mb">
            <label for="mi2" class="form-label">Amount of Money:</label>
            <input type="number" class="form-control" id="mi2"  step="0.01" bind:value={money}>
        </div>
        <div class="mb">
            <label for="ni" class="form-label">Notes:</label>
            <input type="text" class="form-control" id="ni" placeholder="Your notes" bind:value={notes}>
        </div>
        <div class="mb">
            <label for="nwi" class="form-label">Need/Want:</label>
            <select id="nwi" bind:value={needwant} class="form-select">
                <option value="Need">Need</option>
                <option value="Want">Want</option>
            </select>
        </div>
        {#if expenseType == "Purchase"}
        <div class="mb">
            <label for="ii" class="form-label">Item (Sales):</label>
            <input type="text" class="form-control" id="ii" placeholder="Your item" bind:value={item}>
        </div>
        {/if}
        <br>
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary">Add</button>
        </div>
    </form>
</div>