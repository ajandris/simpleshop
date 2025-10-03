
function profileListeners(){
    tablinks = document.getElementsByClassName("tablink");
    for (let i = 0; i < tablinks.length; i++) {
      tablinks[i].addEventListener('click', function(e) {
        openTab(e.currentTarget);
      });
    }
}
