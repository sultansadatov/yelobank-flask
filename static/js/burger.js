$(document).ready(function () {
    const burgerBtn = $('.hamburger-btn')
    const body = $('body');
    const menu = $('.hamburger-menu');
    $(burgerBtn).click(function (e) { 
        e.preventDefault();
        $(burgerBtn).toggleClass('active');
        $(menu).toggleClass('active');
        $(body).toggleClass('active');
    });
}); 


// const menu = document.querySelector(".hamburger-menu");
// const menuItems = document.querySelectorAll(".menuItem");
// const hamburger= document.querySelector(".hamburger");
// const closeIcon= document.querySelector(".closeIcon");
// const menuIcon = document.querySelector(".menuIcon");

// function toggleMenu() {
//   if (menu.classList.contains("showMenu")) {
//     menu.classList.remove("showMenu");
//     closeIcon.style.display = "none";
//     menuIcon.style.display = "block";
//   } else {
//     menu.classList.add("showMenu");
//     closeIcon.style.display = "block";
//     menuIcon.style.display = "none";
//   }
// }

// hamburger.addEventListener("click", toggleMenu());