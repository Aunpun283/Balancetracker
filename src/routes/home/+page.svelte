<script>
    import Appnav from "$lib/Appnav.svelte"
    import { firebase_auth } from "$lib"
    import { onAuthStateChanged } from "@firebase/auth"
    import axios from "axios";
    let name = ""
    let currency = "THB"
    function createtracker() {
        onAuthStateChanged(firebase_auth, (user) => {
            axios.get(`https://balancetrackerbackend.onrender.com/createtracker?name=${name}&currency=${currency}&ownerid=${user.uid}`)

          alert("00")
            
            window.location.reload()
        
        })

    }
    import { onMount } from "svelte";
    let trackers = [];
    onMount(() => {
        onAuthStateChanged(firebase_auth, (user) => {
            const xhr = new XMLHttpRequest();
xhr.open("GET", `https://balancetrackerbackend.onrender.com/getTrackerFromOwnerId?ownerid=${user.uid}`);
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
  
      {#each trackers as tracker (tracker._id)}
          <div class="card">
              <div class="card-body">
                  <h3 class="card-title">{tracker.name}</h3>
                  <br><br><br><br><br><br><br>
                  <div class="d-grid gap-2">
                    <a href="/trackers/tracker/board?id={tracker._id.$oid}" class="btn btn-primary">{tracker.name}</a>
                  </div>
              </div>
          </div>
      {/each}
   
  <div class="card">
    <div class="card-body">
        <h5 class="card-title">Create a new tracker</h5>
        <form on:submit|preventDefault={createtracker}>
          <div class="mb-3">
              <label for="ni" class="form-label">Name:</label>
              <input type="text" bind:value={name} required class="form-control" placeholder="Your tracker's name">
          </div>
          <div class="mb-3">
              <label for="nc" class="form-label">Currency:</label>
              <select id="nc" class="form-select" required bind:value={currency}>
                  <option value="USD">United States Dollar (USD)</option>
    <option value="CAD">Canadian Dollar (CAD)</option>
    <option value="MXN">Mexican Peso (MXN)</option>
    <option value="BZD">Belize Dollar (BZD)</option>
    <option value="CRC">Costa Rican Colón (CRC)</option>
    <option value="GTQ">Guatemalan Quetzal (GTQ)</option>
    <option value="HNL">Honduran Lempira (HNL)</option>
    <option value="NIO">Nicaraguan Córdoba (NIO)</option>
    <option value="PAB">Panamanian Balboa (PAB)</option>
    <option value="XCD">Eastern Caribbean Dollar (XCD)</option>
    <option value="ARS">Argentine Peso (ARS)</option>
      <option value="BOB">Bolivian Boliviano (BOB)</option>
      <option value="BRL">Brazilian Real (BRL)</option>
      <option value="CLP">Chilean Peso (CLP)</option>
      <option value="COP">Colombian Peso (COP)</option>
      <option value="PYG">Paraguayan Guarani (PYG)</option>
      <option value="PEN">Peruvian Nuevo Sol (PEN)</option>
      <option value="UYU">Uruguayan Peso (UYU)</option>
      <option value="VEF">Venezuelan Bolivar (VEF)</option>
      <option value="DZD">Algerian Dinar (DZD)</option>
      <option value="AOA">Angolan Kwanza (AOA)</option>
      <option value="BWP">Botswana Pula (BWP)</option>
      <option value="BIF">Burundian Franc (BIF)</option>
      <option value="XAF">Central African CFA Franc (XAF)</option>
      <option value="KMF">Comorian Franc (KMF)</option>
      <option value="DJF">Djiboutian Franc (DJF)</option>
      <option value="EGP">Egyptian Pound (EGP)</option>
      <option value="ERN">Eritrean Nakfa (ERN)</option>
      <option value="SZL">Eswatini Lilangeni (SZL)</option>
      <option value="ETB">Ethiopian Birr (ETB)</option>
      <option value="XOF">West African CFA Franc (XOF)</option>
      <option value="GMD">Gambian Dalasi (GMD)</option>
      <option value="GHS">Ghanaian Cedi (GHS)</option>
      <option value="GNF">Guinean Franc (GNF)</option>
      <option value="XAF">Central African CFA Franc (XAF)</option>
      <option value="XOF">West African CFA Franc (XOF)</option>
      <option value="KES">Kenyan Shilling (KES)</option>
      <option value="LSL">Lesotho Loti (LSL)</option>
      <option value="LRD">Liberian Dollar (LRD)</option>
      <option value="LYD">Libyan Dinar (LYD)</option>
      <option value="MGA">Malagasy Ariary (MGA)</option>
      <option value="MWK">Malawian Kwacha (MWK)</option>
      <option value="MRO">Mauritanian Ouguiya (MRO)</option>
      <option value="MUR">Mauritian Rupee (MUR)</option>
      <option value="MAD">Moroccan Dirham (MAD)</option>
      <option value="MZN">Mozambican Metical (MZN)</option>
      <option value="AUD">AUD (Australian Dollar)</option>
      <option value="NZD">NZD (New Zealand Dollar)</option>
      <option value="NAD">Namibian Dollar (NAD)</option>
      <option value="NGN">Nigerian Naira (NGN)</option>
      <option value="RWF">Rwandan Franc (RWF)</option>
      <option value="STN">São Tomé and Príncipe Dobra (STN)</option>
      <option value="SCR">Seychellois Rupee (SCR)</option>
      <option value="SLL">Sierra Leonean Leone (SLL)</option>
      <option value="SOS">Somali Shilling (SOS)</option>
      <option value="ZAR">South African Rand (ZAR)</option>
      <option value="SSP">South Sudanese Pound (SSP)</option>
      <option value="SDG">Sudanese Pound (SDG)</option>
      <option value="SZL">Swazi Lilangeni (SZL)</option>
      <option value="TZS">Tanzanian Shilling (TZS)</option>
      <option value="TND">Tunisian Dinar (TND)</option>
      <option value="UGX">Ugandan Shilling (UGX)</option>
      <option value="AED">United Arab Emirates Dirham (AED)</option>
      <option value="ZMW">Zambian Kwacha (ZMW)</option>
      <option value="ZWL">Zimbabwean Dollar (ZWL)</option>
      <option value="EUR">Euro (EUR)</option>
      <option value="GBP">British Pound Sterling (GBP)</option>
      <option value="CHF">Swiss Franc (CHF)</option>
      <option value="SEK">Swedish Krona (SEK)</option>
      <option value="NOK">Norwegian Krone (NOK)</option>
      <option value="DKK">Danish Krone (DKK)</option>
      <option value="PLN">Polish Złoty (PLN)</option>
      <option value="HUF">Hungarian Forint (HUF)</option>
      <option value="CZK">Czech Koruna (CZK)</option>
      <option value="ISK">Icelandic Króna (ISK)</option>
      <option value="RUB">Russian Ruble (RUB)</option>
      <option value="BGN">Bulgarian Lev (BGN)</option>
      <option value="HRK">Croatian Kuna (HRK)</option>
      <option value="RON">Romanian Leu (RON)</option>
      <option value="TRY">Turkish Lira (TRY)</option>
      <option value="UAH">Ukrainian Hryvnia (UAH)</option>
      <option value="MKD">Macedonian Denar (MKD)</option>
      <option value="BAM">Bosnia and Herzegovina Convertible Marka (BAM)</option>
      <option value="YTL">Turkish Lira (Old, YTL)</option>
      <option value="AED">AED (United Arab Emirates Dirham)</option>
      <option value="AFN">AFN (Afghan Afghani)</option>
      <option value="AMD">AMD (Armenian Dram)</option>
      <option value="AZN">AZN (Azerbaijani Manat)</option>
      <option value="BHD">BHD (Bahraini Dinar)</option>
      <option value="BDT">BDT (Bangladeshi Taka)</option>
      <option value="BTN">BTN (Bhutanese Ngultrum)</option>
      <option value="BND">BND (Brunei Dollar)</option>
      <option value="KHR">KHR (Cambodian Riel)</option>
      <option value="CNY">CNY (Chinese Yuan)</option>
      <option value="GEL">GEL (Georgian Lari)</option>
      <option value="HKD">HKD (Hong Kong Dollar)</option>
      <option value="INR">INR (Indian Rupee)</option>
      <option value="IDR">IDR (Indonesian Rupiah)</option>
      <option value="IRR">IRR (Iranian Rial)</option>
      <option value="IQD">IQD (Iraqi Dinar)</option>
      <option value="ILS">ILS (Israeli New Shekel)</option>
      <option value="JPY">JPY (Japanese Yen)</option>
      <option value="JOD">JOD (Jordanian Dinar)</option>
      <option value="KZT">KZT (Kazakhstani Tenge)</option>
      <option value="KWD">KWD (Kuwaiti Dinar)</option>
      <option value="KGZ">KGZ (Kyrgyzstani Som)</option>
      <option value="LAK">LAK (Laotian Kip)</option>
      <option value="LBP">LBP (Lebanese Pound)</option>
      <option value="MYR">MYR (Malaysian Ringgit)</option>
      <option value="MVR">MVR (Maldivian Rufiyaa)</option>
      <option value="MNT">MNT (Mongolian Tugrik)</option>
      <option value="MMK">MMK (Myanmar Kyat)</option>
      <option value="NPR">NPR (Nepalese Rupee)</option>
      <option value="KPW">KPW (North Korean Won)</option>
      <option value="OMR">OMR (Omani Rial)</option>
      <option value="PKR">PKR (Pakistani Rupee)</option>
      <option value="PHP">PHP (Philippine Peso)</option>
      <option value="QAR">QAR (Qatari Rial)</option>
      <option value="SAR">SAR (Saudi Riyal)</option>
      <option value="SGD">SGD (Singapore Dollar)</option>
      <option value="KRW">KRW (South Korean Won)</option>
      <option value="LKR">LKR (Sri Lankan Rupee)</option>
      <option value="SYP">SYP (Syrian Pound)</option>
      <option value="TWD">TWD (New Taiwan Dollar)</option>
      <option value="TJS">TJS (Tajikistani Somoni)</option>
      <option value="THB">THB (Thai Baht)</option>
      <option value="TRY">TRY (Turkish Lira)</option>
      <option value="TMT">TMT (Turkmenistan Manat)</option>
      <option value="AED">AED (United Arab Emirates Dirham)</option>
      <option value="UZS">UZS (Uzbekistan Som)</option>
      <option value="VND">VND (Vietnamese Dong)</option>
      <option value="YER">YER (Yemeni Rial)</option>
              </select>
          </div>
          <div class="d-grid gap-2">
              <button type="submit" class="btn btn-primary">Create</button>
          </div>
      </form>
    </div>
</div>
</div>
