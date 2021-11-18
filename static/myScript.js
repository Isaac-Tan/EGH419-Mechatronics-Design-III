

function dropDownFunction() {
  var x = document.getElementById("myMap");
  if (x.style.display == "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
};
function sessionFunction(){
  var x=document.getElementById("start-btn");
    if (x.innerHTML=="End Session") {

      x.innerHTML = "Start Session";
      document.getElementById("modal-title").innerHTML="Session Ending";
      document.getElementById("modal-body").innerHTML="Please return the item to the locker and firmly close the door." + "<br />" +"Thank you!";
      // document.getElementById("modal-button").onclick=null;

      // clearInterval(myTimer);
      // $( "#myModal" ).modal( "hide" );
      // CloseModal();
      // document.getElementById("modal-button").onclick=CloseModal();
      
    }
    else if (x.innerHTML == "Start Session") {
      x.innerHTML = "End Session";
      document.getElementById("modal-title").innerHTML="Initialising Session";
      document.getElementById("modal-body").innerHTML="When the locker opens please take your equipment and close the door";
      // CloseModal();
      // $( "#myModal" ).modal( "hide" );
      // showSimpleDialog();
      clock();

    }
  };

function stopwatch(){
  var x=document.getElementById("start-btn");
  if (x.innerHTML=="Start Session") {
    document.getElementById("sessionDisp").innerHTML="Not Running";
    document.getElementById("doorDisp").innerHTML="Close";
    clearInterval(myTimer);
  }
  else if (x.innerHTML == "End Session") {
    document.getElementById("sessionDisp").innerHTML="Running";
    document.getElementById("doorDisp").innerHTML="Open";
    // clock();
  }
  $( "#myModal" ).modal( "hide" );
};

$("#start-btn").click(function(e) {
  e.preventDefault();
  sessionFunction();
  $.ajax({
      type: "POST",
      url: "/session",
      data: { 
        id: this.innerHTML,
      },  
      success: function(result) {
        stopwatch();
        // sessionFunction();
        // console.log(result);
          // alert('ok');
      },
      error: function(result) {
          alert('error');
      }
  });
});
// function Confirm() {
//   var r = confirm("Go back to home page?");
//   if (r == true){
//     document.getElementById("brand-icon").href=("home.html");
//   }
//   else{
//     document.getElementById("brand-icon").href=("checkin.html");
//   }
// }


var myTimer;
function clock() {
  myTimer = setInterval(myClock, 1000);
  var time = 0;

  function myClock() {
    time++;
    var hours = Math.floor(time/3600);
    var minutes = Math.floor(time/60);
    var second = time-minutes*60;
    minutes = checkTime(minutes);
    second = checkTime(second);
    document.getElementById("timerDisp").innerHTML =   hours + ":" + minutes + ":" + second;
    ;
  }
}
function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

//#region Dialogs
function showSimpleDialog() {
  $( "#myModal" ).modal();
}

function CloseModal() {
  $( "#myModal" ).modal( "hide" )
}
//#endregion Dialogs

