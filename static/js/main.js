function openTab(elem) {
  let i, x, tablinks;

  // connects link ids with text ids
  const tabs = {
    general_info_link: "general_info",
    security_link: "security",
  }

  x = document.getElementsByClassName("tab");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
    tablinks[i].classList.remove("tablink_active");
  }

  elem.classList.add("tablink_active");
  document.getElementById(tabs[elem.id]).style.display = "block";
}
