//works better not color edited
const OCRAD = require('async-ocrad');
const fs = require('fs');
const imageToSlices = require('image-to-slices');

const imageSlicingOpts = {
  lineYArray: [],
  lineXArray: [787, 1952, 2077, 2250],
  source: './images/image03.png',
  saveToDir: './images/slicedImages/',
};

const boardSlicingOpts = {
  lineXArray: [79, 156, 233, 310, 387, 464, 541, 618, 695, 772, 849, 926, 1003, 1080, 1157],
  lineYArray: [83, 160, 237, 314, 391, 468, 545, 622, 699, 776, 853, 930, 1007, 1084],
  source: './images/slicedImages/section-2.png',
  saveToDir: 'images/slicedImages/',
};

imageToSlices.configure({
    clipperOptions: {
        canvas: require('canvas')
    }
});


async function sliceImage() {
  return new Promise((resolve, reject) => {
    if (!fs.existsSync(imageSlicingOpts.saveToDir)) fs.mkdirSync(imageSlicingOpts.saveToDir); //makes slicedImages dir
    // Slice image horizontally
    imageToSlices(imageSlicingOpts.source, imageSlicingOpts.lineXArray, imageSlicingOpts.lineYArray, {
      saveToDir: imageSlicingOpts.saveToDir
    }, function() {
      console.log('The source image has been sliced horizontally into chunks!');

      // rename section-4.png to rack.png
      fs.renameSync('./images/slicedImages/section-4.png', './images/slicedImages/rack.png');

      imageToSlices(boardSlicingOpts.source, boardSlicingOpts.lineXArray, boardSlicingOpts.lineYArray, {
        saveToDir: boardSlicingOpts.saveToDir
      }, function() {
        console.log('The grid has been sliced into a 15x15 grid!');
        resolve();
      });
    });
  });
};

async function ocrad(outputFileName){
  
  //make output directory
  if (!fs.existsSync('output')) fs.mkdirSync('output');
  // create a new file or overwrite the file if it already exists
  fs.writeFileSync(`./output/${outputFileName}`, '');

  // loops through all board photos
  for (var i = 1; i < 226; i++) {
    var text = await OCRAD('./images/slicedImages/section-' + i + '.png');
    //only include these chars
    text = text.replace(/[^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzlIi01| ]/g, ''); 
    fs.appendFileSync(`./output/${outputFileName}`, text + " -- " + i + '\n');
  }  
  console.log('OCRAD successfully read the board!');

  // reads rack photo into rack array
  var rack = await OCRAD('./images/slicedImages/rack.png');
  //only include these chars
  rack = rack.replace(/[^ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzlIi0 ]/g, '');
  fs.appendFileSync(`./output/${outputFileName}`, 'My Rack: ' + rack + '\n');
  console.log('OCRAD successfully read the rack!');
};

async function main(){
  await sliceImage();
  await ocrad('outputOCR.txt');
}

main();

