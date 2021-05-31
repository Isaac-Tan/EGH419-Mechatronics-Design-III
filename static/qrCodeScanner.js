// Software used is from Dmitri Lau
// on https://www.sitepoint.com/create-qr-code-reader-mobile-website/
// and was altered for use in this EGH419 project

const qrcoder = window.qrcode;

const video = document.createElement("video");
const canvasElement = document.getElementById("qr-canvas");
const canvas = canvasElement.getContext("2d");

const qrResult = document.getElementById("qr-result");
const outputData = document.getElementById("outputData");
const btnScanQR = document.getElementById("qrcode-btn");
const home_container = document.getElementById("home-container");

let scanning = false;

qrcode.callback = res => {
  if (res) {
    outputData.innerText = res;
    scanning = false;

    video.srcObject.getTracks().forEach(track => {
      track.stop();
    });

    qrResult.hidden = false;
    canvasElement.hidden = true;

    btnScanQR.hidden = false;
    // window.location.href = outputData.innerText;
    window.location.href = "../selectionpage.html";  
  }
};

btnScanQR.onclick = () => {
  navigator.mediaDevices
  .getUserMedia({ video: { facingMode: "environment" } })
  .then(function(stream) {
    scanning = true;
    qrResult.hidden = true;
    btnScanQR.hidden = true;
    home_container.hidden = true;
    canvasElement.hidden = false;
    // myMap.hidden = true;
    video.setAttribute("playsinline", true); // required to tell iOS safari we don't want fullscreen
    video.srcObject = stream;
    video.play();
    tick();
    scan();
  });
}

function tick() {
  canvasElement.height = video.videoHeight;
  canvasElement.width = video.videoWidth;
  canvas.drawImage(video, 0, 0, canvasElement.width, canvasElement.height);

  scanning && requestAnimationFrame(tick);
}

function scan() {
  try {
    qrcode.decode();
  } catch (e) {
    setTimeout(scan, 300);
  }
}
