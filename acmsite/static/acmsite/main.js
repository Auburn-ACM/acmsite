function showMenu() {
    const menu = document.getElementById("nav-dropdown-content");
    console.log(menu)
    if (menu.style.display === "block") {
        menu.style.display = "none";
    } else {
        menu.style.display = "block";
    }
}