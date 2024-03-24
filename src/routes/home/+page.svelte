<script>
    import Appnav from "$lib/Appnav.svelte"
    import { firebase_auth } from "$lib"
    import { onAuthStateChanged } from "@firebase/auth"

    import { onMount } from "svelte";
    let trackers = [];
    onMount(() => {
        onAuthStateChanged(firebase_auth, (user) => {
            const xhr = new XMLHttpRequest();
xhr.open("GET", `https://bltrackerbackenddeploy.onrender.com/getTrackerFromOwnerId?ownerid=${user.uid}`);
xhr.send();
xhr.responseType = "json";
xhr.onload = () => {
  if (xhr.readyState == 4 && xhr.status == 200) {
    const respones = JSON.parse(xhr.response.DATA)
      
    trackers = respones
    console.log(trackers)
  } else {
    console.log(`Error: ${xhr.status}`);
  }
};


        })
      
    })
    
</script>

<!-- Import statements and script omitted for brevity -->

<style>
  #container {
      display: grid;
      grid-template-columns: repeat(4, 1fr); /* 4 columns */
      gap: 20px; /* Gap between cards */
      margin-top: 50px; /* Ensure space below navbar */
  }

  .card {
      width: 100%; /* Each card takes up full width of its grid cell */
  }
</style>

<Appnav />

<div id="container">
  {#if trackers.length > 0}
      {#each trackers as tracker (tracker._id)}
          <div class="card">
              <div class="card-body">
                  <h5 class="card-title">{tracker.name}</h5>
                  <div class="d-grid gap-2">
                    <a href="/trackers/tracker/board?id={tracker._id.$oid}" class="btn btn-primary">{tracker.name}</a>
                  </div>
              </div>
          </div>
      {/each}
  {:else}
      <div id="div-center">
        <h1>No trackers found</h1>
      </div>
  {/if}
</div>
