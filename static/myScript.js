function dropDownFunction() {
  var x = document.getElementById("myMap");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
};
function sessionFunction(){
  var x=document.getElementById("start-btn")
    if (x.innerHTML=="End Session") {
      x.innerHTML = "Start Session";
      document.getElementById("sessionDisp").innerHTML="Not Running";
      document.getElementById("modal-title").innerHTML="Session Ending";
      document.getElementById("modal-body").innerHTML="Please return the item to the locker and firmly close the door." + "<br />" +"Thank you!"
      document.getElementById("button-link").href="checking/html/session/on";
    }


    else {
      x.innerHTML = "End Session";
      document.getElementById("sessionDisp").innerHTML="Running";
      document.getElementById("modal-title").innerHTML="Session Started";
      document.getElementById("modal-body").innerHTML="Have a great time!"
      document.getElementById("button-link").href="checking/html/session/off";
    }
};
function Confirm() {
  var r = confirm("Go back to home page?");
  if (r == true){
    document.getElementById("brand-icon").href=("home.html");
  }
  else{
    document.getElementById("brand-icon").href=("checkin.html");
  }
}