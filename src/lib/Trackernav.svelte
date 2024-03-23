<script>
  
    export let id;
    
  
</script>

<nav class="navbar navbar-primary bg-primary" data-bs-theme="dark">
    <div class="container-fluid">
         
        <a href="/home" class="navbar-brand">
            <img src="/logo.svg" height="50"width="100" alt="">Balance tracker</a>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/tracker/board?id={id}" class="nav-link active" >Payment/Income board</a>
            </li>
        </ul>
   
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/add/payment?id={id}" class="nav-link active" >Add Payment</a>
            </li>
        </ul>

        
        <ul class="navbar-nav">
            <li class="nav-item">
                <a href="/trackers/add/income?id={id}" class="nav-link active" >Add Income</a>            </li>
        </ul>
        <ul class="navbar-nav">
            <li class="nav-item">
                <a class="nav-link active" >Settings</a> </li>
        </ul>
       
    </div>
</nav>