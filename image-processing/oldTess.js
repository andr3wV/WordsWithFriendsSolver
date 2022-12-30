const fs = require("fs");
const imageToSlices = require('image-to-slices');
const Jimp = require('jimp');
const { createWorker } = require('tesseract.js');
const PSM = require('tesseract.js/src/constants/PSM.js'); 
const OCR = require('tesseract.js/src/constants/OEM.js');

const imageSlicingOpts = {
  lineYArray: [],
  lineXArray: [787, 1952, 2077, 2250],
  source: './images/image05.png',
  saveToDir: './images/slicedImages',
};

const boardSlicingOpts = {
  lineXArray: [79, 156, 233, 310, 387, 464, 541, 618, 695, 772, 849, 926, 1003, 1080, 1157],
  lineYArray: [83, 160, 237, 314, 391, 468, 545, 622, 699, 776, 853, 930, 1007, 1084],
  source: './images/slicedImages/section-2.png',
  saveToDir: './images/slicedImages',
};

var rack = [];
var yellowFlags = []; // Initialize array with all values set to false

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
}

async function playedTile(){
  try{
      for(let i = 1; i < 226; i++) {
        var source = './images/slicedImages/section-' + i + '.png';
        const image = await Jimp.read(source);
        let hasYellow = false;
        await image.scan(0, 0, image.bitmap.width, image.bitmap.height, function(x, y, idx) {
          const red = this.bitmap.data[idx + 0];
          const green = this.bitmap.data[idx + 1];
          const blue = this.bitmap.data[idx + 2];
          const alpha = this.bitmap.data[idx + 3];        
          if(red == 242 && green == 181 && blue ==95) hasYellow = true;
        });
        if (hasYellow) yellowFlags.push(i);
      }
      console.log('Found all tiles on board that were played.');
  }
  catch(error){
    console.log(error)
  }
}

async function applyThreshold() {
  try{
    for(let i = 0; i < yellowFlags.length; i++) {
      var source = './images/slicedImages/section-' + yellowFlags[i] + '.png';
      const image = await Jimp.read(source); 
      await image.scan(0, 0, image.bitmap.width, image.bitmap.height, function(x, y, idx) {
        const red = this.bitmap.data[idx + 0];
        const green = this.bitmap.data[idx + 1];
        const blue = this.bitmap.data[idx + 2];
        const alpha = this.bitmap.data[idx + 3];
        if (red === 65 && green === 33 && blue === 21 || red === 255 && green === 255 && blue === 255) {
          this.bitmap.data[idx + 0] = 0;
          this.bitmap.data[idx + 1] = 0;
          this.bitmap.data[idx + 2] = 0;
        } else {
          this.bitmap.data[idx + 0] = 255;
          this.bitmap.data[idx + 1] = 255;
          this.bitmap.data[idx + 2] = 255;
        }
      }, function(){
        image.resize(Jimp.AUTO, 0.5 * image.bitmap.height, 'hermite')
        .grayscale()
        .write(source);
      });
    } 
  } catch(error) {
        console.error(`Error reading or writing image: ${error}`);
  }
  console.log('Grid successfully set to desired threshold and downscaled');
}

async function tesseract(outputFileName) {
  const worker = await createWorker({
  logger: () => {}
  });

  await worker.loadLanguage('eng');
  await worker.initialize('eng');
  await worker.setParameters({
    tessedit_char_whitelist: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ lio|[]()',
    tessedit_pageseg_mode: PSM.SINGLE_WORD
  });

  //make output it doesn't exist
  if (!fs.existsSync('output')) fs.mkdirSync('output');
   // create a new file or overwrite the file if it already exists
  fs.writeFileSync(`./output/${outputFileName}`, '');

  //loops through photos photos
  for(var i = 0; i<yellowFlags.length; i++){
    const { data: { text } } = await worker.recognize('./images/slicedImages/section-' + yellowFlags[i] + '.png'); //PATH!**
    fs.appendFileSync(`./output/${outputFileName}`, text||'-'+'\n');
  }  
  console.log('Tesseract successfully read the board!');

  //reads rack photo into rack array
  const { data: { text } } = await worker.recognize('./images/slicedImages/rack.png');
  for(i in text) rack.push(text[i]); // add letters to rack array
  rack = rack.filter(function(str) {return /\S/.test(str);}); //remove white space
  fs.appendFileSync(`./output/${outputFileName}`, rack.toString());
  console.log('Tesseract successfully read the rack!');

  console.log('Terminating Tesseract.');
  await worker.terminate();
}

async function main(){
  await sliceImage();
  await playedTile();
  await applyThreshold();
  await tesseract('tessOutput.txt');
}

main();