 
<script>
    import Trackernav from "../../../../lib/Trackernav.svelte";
    import { page } from "$app/stores"
    import axios from "axios";
    import { onAuthStateChanged } from "@firebase/auth";
    import firebase_auth from "../../../../lib/auth";
    import { onMount } from "svelte";
    const id = $page.data.id
    let incomeType = "Salary"
    let money = 0.00
    let notes = "-"
    let item = "-"
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
    function addIncome() {
        axios.get(`https://bltrackerbackenddeploy.onrender.com/addIncome?trackerid=${id}&it=${incomeType}&im=${money}&in=${notes}&item=${item}`)
        .then(response => {
                // Check if the tracker creation was successful before redirecting
                if (response.data.STATUS === "SUCCESS") {
                    window.location.href = "/trackers/tracker/incomes?id=" + id;
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
    <form on:submit|preventDefault={addIncome}>
        <h1>Add income</h1>
        <div class="mb-3">
            <label for="ti" class="form-label">Type of Income:</label>
            <select id="ti" class="form-select" bind:value={incomeType}>
                <option value="Salary">Salary</option>
                <option value="Allowance Raise">Allowance Raise</option>
                <option value="Loan">Loan</option>
                <option value="Borrowing money">Borrowing money</option>
                <option value="Sale">Sale</option>
            </select>
            
             
        </div>
        <div class="mb">
            <label for="mi" class="form-label">Modify type:</label>
            <input type="text" class="form-control" id="mi" bind:value={incomeType}>
        </div>
        <div class="mb">
            <label for="mi2" class="form-label">Amount of Money:</label>
            <input type="number" class="form-control" id="mi2"  step="0.01" bind:value={money}>
        </div>
        <div class="mb">
            <label for="ni" class="form-label">Notes:</label>
            <input type="text" class="form-control" id="ni" placeholder="Your notes" bind:value={notes}>
        </div>
        {#if incomeType == "Sale"}
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