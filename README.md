
![banner](https://i.imgur.com/7HM68Hj.png?1)

# Words With Friends Solver
Ever wondered what the best possible word to play in Words with Friends is? Well now you can know with this program! Easily generate the best words your letters can play on the board. Simply upload a screenshot of your board, and this program will do the rest for you!

### How It Works
The program uses matrix color gradient recognition to detect the edges of the gameboard, and uses a combination of the Tesseract.js and the ORCAD.js OCRs to read the tiles that have been played. Resizing, grayscaling, and a threshold are applied to newly generated images. Then, a quasi-unique tree structure is utilized for prefix and suffix generation on each of the open tiles on the board (see wordAlgo and tess.js folder for detailed code) and each of these words generated is scored and shown accordingly.  

## Requirements
 - `node` 5.0.0 or greater
 - `npm` 
 - `python3` 
 - Words With Friends 2: v16.30.3

 **Note**: Install the latest version `node` and `npm` from [here](https://nodejs.org/en/download/) and python3 from [here](https://www.python.org/downloads/).
   
## Install

 Install `pytest` to your system path using `pip3`:

 ```bash
 $ pip3 install pytest
  ```
 **Note**: you may have to force permissions (e.g. `sudo` on MacOS)

Install Javascript dependencies: 
```bash
 $ npm install
  ```
## Running
Clone this repo. 

Make an `images` directory by running: 
```back
$ mkdir images
```

Take a screenshot of your board and place it in the `images` directory.  A proper image should have the entire board fully in view (NOT zoomed in) like so: 


<img src="https://i.imgur.com/StMkF0Q.png?1" height="25%" width="25%">


Next, run the following in your command line interface:
 ```bash
 $ npm start
 ```
 Provide the image file name of your screenshot. Hit enter. Then letters in your rack separated by spaces. Hit enter.

## Error Handling
There are a few reasons why this program may fail:
- Your screenshot image is zoomed in, blurry, or modified.
- You do not have Words with Friends 2 or the supported version.
- You have tile styles enabled (disable them in Settings)
- I haven't updated the program in a while (please submit an issue [here](https://github.com/andr3wV/words_with_friends_solver/issues))

## TODO:
- Automate rack so user doesn't have to input.
- Support Blank Tiles
- Add boost tile support
