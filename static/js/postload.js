
function profileListeners(){
    // sets listeners for each tab menu item
    tablinks = document.getElementsByClassName("tablink");
    for (let i = 0; i < tablinks.length; i++) {
      tablinks[i].addEventListener('click', function(e) {
        openTab(e.currentTarget);
      });

      // select the first tab after page is loaded
      if (i === 0) {
          document.addEventListener("DOMContentLoaded", function(e) {
            tablinks[i].click();
          });
      }
    }
}
