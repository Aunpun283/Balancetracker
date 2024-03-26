 
<script>
    import Trackernav from "../../../../lib/Trackernav.svelte";
    import { page } from "$app/stores"
    import axios from "axios";
    import { onAuthStateChanged } from "@firebase/auth";
    import firebase_auth from "../../../../lib/auth";
    import { onMount } from "svelte";
    const id = $page.data.id
    let incomeType = " "
    let money = 0.00
 
    onMount(() => { 
    onAuthStateChanged(firebase_auth, (user) => {
        if (user) {
            fetch(`https://balancetrackerbackend.onrender.com/getTrackerInfo?id=${id}`)
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
        axios.get(`https://balancetrackerbackend.onrender.comaddIncome?trackerid=${id}&it=${incomeType}&im=${money}`)
        .then(response => {
                // Check if the tracker creation was successful before redirecting
                if (response.data.STATUS === "SUCCESS") {
                    window.location.href = "/trackers/tracker/board?id=" + id;
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
    
            <input type="text" class="form-control" id="mi" bind:value={incomeType}>
        </div>
       
        <div class="mb">
            <label for="mi2" class="form-label">Amount of Money:</label>
            <input type="number" class="form-control" id="mi2"  step="0.01" bind:value={money}>
        </div>
      
        <br>
        <div class="d-grid gap-2">
            <button type="submit" class="btn btn-primary">Add</button>
        </div>
    </form>
</div>