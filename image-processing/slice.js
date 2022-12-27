const fs = require("fs");
var imageToSlices = require('image-to-slices');
imageToSlices.configure({
    clipperOptions: {
        canvas: require('canvas')
    }
});


if (!fs.existsSync('./slicedImages')) fs.mkdirSync('./slicedImages'); //makes slicedImages dir


//Constants for slicing
var lineYArray = [];
var lineXArray = [787, 1952, 2077, 2250];
var source = './images/image02.png'; 
 
imageToSlices(source, lineXArray, lineYArray, {
    saveToDir: './slicedImages/'
}, function() {
    console.log('The source image has been sliced into chunks!');
});


//rename the rack photo so it isn't overwritten 
setTimeout(()=>{
    fs.rename('./slicedImages/section-4.png', './slicedImages/rack.png', function(err) {
       if ( err ) console.log('ERROR: ' + err);
    });
}, 5000)

/* This slices the gameboard screenshot vertically and horizontally into each tile piece
    Each piece is labeled 'section-1.png' through 'section-225.png'. The images are stored row by row */
setTimeout(()=>{
    var lineXArray = [79,  156,  233, 310, 387,  464,  541, 618, 695,  772,  849, 926, 1003, 1080, 1157];
    var lineYArray = [83,  160, 237, 314, 391,  468, 545, 622, 699,  776, 853, 930, 1007, 1084]
    var source = './slicedImages/section-2.png'; 
     
    imageToSlices(source, lineXArray, lineYArray, {
        saveToDir: './slicedImages/'
    }, function() {
        console.log('The grid has been sliced into a 15x15 grid!');
    });

 } , 10000);



   


