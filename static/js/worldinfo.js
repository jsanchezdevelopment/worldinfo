var second = 0;

function incrementSeconds() {
  second += 1;
  document.getElementById('seconds-counter').innerHTML = "Waiting " + second + " seconds.";
}

function second_counter() {
  var cancel = setInterval(incrementSeconds, 1000);  
}


function ds()
{
  document.getElementById('thedata').innerHTML = '<div class="container" style="text-align: center"><div id="thespinner"></div></div>';
  document.getElementById('thespinner').innerHTML = '<br><span class="spinner-border text-primary" role="status" aria-hidden="true"></span><br><br><button class="btn btn-lg btn-light" type="button"><strong> PLEASE WAIT - Getting the data... </strong></button><br><p id="seconds-counter">Waiting 0 seconds.</p>';
  second_counter();
}

function ConfigMenu(p_continentselect,p_countryselect,p_gobtn,p_action) {
    //alert('ConfigMenu')
    // show/hide the nav items, see nav in index.html 
    // action is the form action for the page which is a URL for this app
    var continentselect = document.getElementById("continent");
    var countryselect = document.getElementById("country");
    var gobtn = document.getElementById("gobtn");
    continentselect.style.display = p_continentselect;
    countryselect.style.display = p_countryselect;
    gobtn.style.display = p_gobtn;
  
    // set the form action
    document.getElementById("main-form").action = p_action;
  }
  
  function ConfigCountrySelect() {
    // get the data
    var continent = document.getElementById("continent").value;
    var countries = document.getElementById("app1countries").innerHTML;
    const o_countries = JSON.parse(countries);

    // clear the country select
    var sel = document.getElementById('country');
    var len = sel.length;
    for (var i = 0; i < len; i++) {
        sel.remove(0);
    }

    // populate the country select
    var i;
    for (i = 0; i < o_countries.length; i++) { 
      if (o_countries[i][1] == continent) {
        var sel = document.getElementById('country');
        var opt = document.createElement('option');
        var n = o_countries[i][0];
        opt.innerHTML = n;
        opt.value = n;
        sel.appendChild(opt);
      }
    }

  }