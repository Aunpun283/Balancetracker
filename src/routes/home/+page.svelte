<script>
  import { onMount } from "svelte";
  import { firebase_auth } from "$lib";
  import { onAuthStateChanged } from "@firebase/auth";
  import axios from "axios";

  let name = "";
  let currency = "THB";
  let trackers = [];

  async function fetchTrackers() {
    const user = firebase_auth.currentUser;
    if (!user) return;

    try {
      const response = await axios.get(`https://balancetrackerbackend.onrender.com/getTrackerFromOwnerId?ownerid=${user.uid}`);
      trackers = response.data;
    } catch (error) {
      console.error("Error fetching trackers:", error);
    }
  }

  async function createTracker() {
    const user = firebase_auth.currentUser;
    if (!user) return;

    try {
      await axios.get(`https://balancetrackerbackend.onrender.com/createtracker?name=${name}&currency=${currency}&ownerid=${user.uid}`);
      await fetchTrackers();
    } catch (error) {
      console.error("Error creating tracker:", error);
    }
  }

  onMount(() => {
    onAuthStateChanged(firebase_auth, async (user) => {
      if (user) {
        await fetchTrackers();
      }
    });
  });
</script>

<!-- Import statements and styles omitted for brevity -->

<Appnav />

<div id="container" class="grid grid-cols-4 gap-20 mt-8">
  <div class="card">
    <div class="card-body">
      <h5 class="card-title">Create a new tracker</h5>
      <form on:submit|preventDefault={createTracker}>
        <div class="mb-3">
          <label for="name" class="form-label">Name:</label>
          <input type="text" id="name" bind:value={name} required class="form-control" placeholder="Your tracker's name">
        </div>
        <div class="mb-3">
          <label for="currency" class="form-label">Currency:</label>
          <select id="currency" class="form-select" bind:value={currency}>
            <!-- Currency options here -->
          </select>
        </div>
        <div class="d-grid gap-2">
          <button type="submit" class="btn btn-primary">Create</button>
        </div>
      </form>
    </div>
  </div>

  {#each trackers as tracker (tracker._id)}
    <div class="card" style="height: 10rem;">
      <div class="card-body">
        <h3 class="card-title">{tracker.name}</h3>
        <br>
        <div class="d-grid gap-2">
          <a href={`/trackers/${tracker._id.$oid}/board`} class="btn btn-primary">{tracker.name}</a>
        </div>
      </div>
    </div>
  {/each}
</div>
