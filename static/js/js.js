var navToggled = false;

function toggleNav() {
  if (navToggled) {
    openNav();
    navToggled = false;
  } else {
    closeNav();
    navToggled = true;
  }
}

var x = window.matchMedia("(max-width: 800px)")

/* Set the width of the sidebar to 250px and the left margin of the page content to 250px */
function openNav() {if(x.matches){
  document.getElementById("mySidebar").style.width = "70%";
  document.getElementById("mySidebar").style.marginLeft = "-2.5%";
  document.getElementById("main").style.marginLeft = "0%";
}

else
  {
  document.getElementById("mySidebar").style.width = "12.5%";
  document.getElementById("main").style.marginLeft = "15%";
  document.getElementById("main").style.width = "85%";
}
}

/* Set the width of the sidebar to 0 and the left margin of the page content to 0 */
function closeNav() {if(x.matches){
  document.getElementById("mySidebar").style.width = "0";
document.getElementById("mySidebar").style.marginLeft = "0%";
}
else
  {document.getElementById("mySidebar").style.width = "0";
  document.getElementById("main").style.marginLeft = "2.5%";
  document.getElementById("main").style.width = "97.5%";}
  

}

