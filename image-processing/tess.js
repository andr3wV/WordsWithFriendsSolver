//image01.png is the board, image02.png is your letters
const { createWorker } = require('tesseract.js');
var letters = [];

const worker = createWorker();
const worker2 = createWorker();

//the board
(async () => {
  await worker.load();
  await worker.loadLanguage('eng');
  await worker.initialize('eng');
  const { data: { text } } = await worker.recognize('./images/image03.jpg'); //**EDIT PATH!**
  console.log(text);
  await worker.terminate();
})();

//your letters
(async () => {
  await worker2.load();
  await worker2.loadLanguage('eng');
  await worker2.initialize('eng');
  const { data: { text } } = await worker2.recognize('./images/image02.png'); //**EDIT PATH!**
  console.log(text);

	
	for(i in text) letters.push(text[i]); // add letters to array letters
 	letters = letters.filter(function(str) {return /\S/.test(str);}); //remove white space
 	console.log(letters);


  await worker2.terminate();
})();
