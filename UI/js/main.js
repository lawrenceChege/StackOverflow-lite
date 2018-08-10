//navbar
function classToggle() {
    const navs = document.querySelectorAll('.nav-bar-items')
    
    navs.forEach(nav => nav.classList.toggle('nav-bar-toggle-show'));
  }
  document.querySelector('.nav-bar-toggle')
    .addEventListener('click', classToggle);

//carosel
var myIndex = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("index-image");
    for (i = 0; i < x.length; i++) {
       x[i].style.display = "none";  
    }
    myIndex++;
    if (myIndex > x.length) {myIndex = 1}    
    x[myIndex-1].style.display = "block";  
    setTimeout(carousel, 2000); // Change image every 5 seconds
}