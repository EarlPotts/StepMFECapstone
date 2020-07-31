function openPage(pageName) 
{
  var i, tabcontent, tablinks;
// Get all the divs with class tabcontent (i.e the pages you want to show)
  tabcontent = document.getElementsByClassName("tabcontent");
// Go through them and hide them all
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
// Show the page with the name of the nav button that was clicked.
  document.getElementById(pageName).style.display = "block";
}
  var tabcontent = document.getElementsByClassName("tabcontent");
// Go through them and hide them all
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
