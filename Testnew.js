// giblets = "eyetrackingdata.json"

// var parsedText = JSON.parse("eyetrackingdata.json");
// coordinates = []
// coordinates.push(parseFloat(parsedText.xCoordinate))
// coordinates.push(parseFloat(parsedText.yCoordinate))
// conosle.log(coordinates)


// function readSingleFile(e) {
//   var file = e.target.files[0];
//   if (!file) {
//     return;
//   }
//   var reader = new FileReader();
//   reader.onload = function(e) {
//     var contents = e.target.resu

var info;

function preload() {
info = loadJSON("eyetrackingdata.json");

}




function setup() {
createCanvas(400,400);

}

function draw() {
background(0);

text(info.xCoordinate, 10, 50);
text(info.yCoordinate, 10, 50);


}

preload();
setup();
draw();



// $.getJSON("http://127.0.0.1/eyetrackingdata.json", function(json) {
//         console.log(json); // access the response object
//         console.log(json.data); // access the array
//         console.log(json.data[0]); // access the first object of the array
//         console.log(json.data[0].number); // access the first object proprty of the array
//     });

//     // Create the XHR object.
// function createCORSRequest(method, url) {
//   var xhr = new XMLHttpRequest();
//   if ("withCredentials" in xhr) {
//     // XHR for Chrome/Firefox/Opera/Safari.
//     xhr.open(method, url, true);
//   } else if (typeof XDomainRequest != "undefined") {
//     // XDomainRequest for IE.
//     xhr = new XDomainRequest();
//     xhr.open(method, url);
//   } else {
//     // CORS not supported.
//     xhr = null;
//   }
//   return xhr;
// }

// // Helper method to parse the title tag from the response.
// function getTitle(text) {
//   return text.match('<title>(.*)?</title>')[1];
// }

// // Make the actual CORS request.
// function makeCorsRequest() {
//   // This is a sample server that supports CORS.
//   var url = '127.0.0.1/hello.html';

//   var xhr = createCORSRequest('GET', url);
//   if (!xhr) {
//     alert('CORS not supported');
//     return;
//   }

//   // Response handlers.
//   xhr.onload = function() {
//     var text = xhr.responseText;
//     var title = getTitle(text);
//     alert('Response from CORS request to ' + url + ': ' + title);
//   };

//   xhr.onerror = function() {
//     alert('Woops, there was an error making the request.');
//   };

//   xhr.send();
// }