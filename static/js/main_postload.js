/**
 * Postload scripts that requires DOM to be loaded
 */

function openSidebar() {
    document.getElementById("mobileSidebar").style.display = "block";
    document.getElementById("sidebarOverlay").style.display = "block";
}

function closeSidebar() {
    document.getElementById("mobileSidebar").style.display = "none";
    document.getElementById("sidebarOverlay").style.display = "none";
}

function toggleMobileDropdown() {
    var x = document.getElementById("mobileProductsDrop");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}
