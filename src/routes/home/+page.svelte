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

<Appnav />

<div id="div-center">
    <ul class="list-group">
        {#if trackers.length > 0}
            {#each trackers as tracker (tracker._id)}
                <li class="list-group-item">
                  <a href="/trackers/tracker/board?id={tracker._id.$oid}">{tracker.name}</a>
                </li>
            {/each}
            {:else}
            <h1>No trackers found</h1>
        {/if}

    </ul>
</div>

