var f = require('fs');

var startEyeTracking = function() {
    while (true) {
    var pixelCoordinates = []
    var str_array =  f.readFileSync('eyetrackingdata.txt','utf8').split(',');

    var screenMath = function(array) {
        pixelCoordinates = []
        pixelCoordinates.push(parseFloat(array[0]) * 1920)
        pixelCoordinates.push(parseFloat(array[1]) * 1080)
    }
    var drawRectangle = function() {
        

    screenMath(str_array)
    console.log(pixelCoordinates)
    drawRectangle();
    }

}

startEyeTracking();





//console.log(pixelCoordinates)




//console.log(readIt())
// console.log(array)
// screenMath(array)


// file = "eyetrackingdata.txt"
// var reader = new FileReader();

//     reader.onload = function(e) {
//         var text = reader.result;                 // the entire file
//         var str_array = str.split(',');
//         console.log(str_array)}

