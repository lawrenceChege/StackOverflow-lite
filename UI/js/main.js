//navbar
function classToggle() {
    const navs = document.querySelectorAll('.nav-bar-items')
    
    navs.forEach(nav => nav.classList.toggle('nav-bar-toggle-show'));
  }
  document.querySelector('.nav-bar-toggle')
    .addEventListener('click', classToggle);

// carosel
// var myIndex = 0;
// carousel();

// function carousel() {
//     var i;
//     var x = document.getElementsByClassName("index-image");
//     for (i = 0; i < x.length; i++) {
//        x[i].style.display = "none";  
//     }
//     myIndex++;
//     if (myIndex > x.length) {myIndex = 1}    
//     x[myIndex-1].style.display = "block";  
//     setTimeout(carousel, 2000); // Change image every 5 seconds
// }

function editfunction() {
    var x = document.getElementsByClassName("editprofile")[0].style.display = "block";
}
function myFunction(id) {
    var x = document.getElementById(id);
    if (x.className.indexOf("show") == -1) {
        x.className += " show";
    } else { 
        x.className = x.className.replace(" show", "");
    }
}