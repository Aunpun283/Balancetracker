<script>
    import auth from "./auth"
    import { onAuthStateChanged } from "@firebase/auth"
    import axios from "axios";
    let expensedialog
    export let id;
    
    function changebalance() {
        let money = Number(prompt("What would you like to change your balance to?"))
        axios.get(`https://bltrackerbackenddeploy.onrender.com/changeBalance?trackerid=${id}&money=${money}`) .then(response => {
                // Check if the tracker creation was successful before redirecting
                if (response.data.STATUS === "SUCCESS") {
                    window.location.reload()
                } else {
                    alert(response.data.ERROR);
                }
            })
            .catch(error => {
                console.error("Error creating tracker:", error);
                alert("An error occurred while changing balance.");
            });
    }
    function deletetracker() {
        
        const confirmation = confirm("Are you sure you want to delete this tracker? \nWARNING: THIS IS IRREVERSIBLE!")
        if (confirmation) {
            axios.get(`http://localhost:8000/deletetracker?trackerid=${id}`) .then(response => {
                // Check if the tracker creation was successful before redirecting
                if (response.data.STATUS === "SUCCESS") {
                    window.location.href = "/home"
                } else {
                    alert(response.data.ERROR);
                }
            })
            .catch(error => {
                console.error("Error creating tracker:", error);
                alert("An error occurred while changing balance.");
            });
        }
    }
</script>

<nav class="navbar navbar-dark bg-dark" data-bs-theme="dark">
    <div class="container-fluid">
        <a href="/home" class="navbar-brand">Second try balance tracker</a>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/tracker/incomes?id={id}" class="nav-link active" >Income board</a>
            </li>
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/tracker/expenses?id={id}" class="nav-link active" >Expenses board</a>
            </li>
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/add/expense?id={id}" class="nav-link active" >Add Expense</a>
            </li>
        </ul>

        
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/add/income?id={id}" class="nav-link active" >Add Income</a>            </li>
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link active" on:click={changebalance}>Change  balance</a> </li>
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link active" on:click={deletetracker}>Delete tracker</a> </li>
        </ul>
    </div>
</nav>