# Words With Friends Solver
Ever wondered what the best possible word to play in Words with Friends or Scrabble is? Well now you can know with this python based program! Easily get an entire list of the best words your letters can play. 

>Note: The method is currently brute forced and works decently fast. See Possible TODO section for more efficient future implementation ideas 

### Requirements
  - `python3` or greater
  - Command Line Interface (CLI) like terminal
## Install

 Install `pytest` to your system path using `pip3`:

 ```bash
 $ pip3 install pytest
  ```
 **Note**: you may have to force permissions (e.g. `sudo` on MacOS)
## Running

 Using `python3` command, enter the following:

 ```bash
 $ python3 main.py <letters>
 ```

 **letters** : enter the the letters the user has available to them in a row without spaces. A blank letter is respresented by a '?' and order does not matter (e.g `w?ihoud`).
### Possible Future Improvements/Contributions:

- Screenshot your current WWF board
  -  Upload the screenshot to the prgram
  - Scan the empty spots, the current words on the board & your letters
  - Application will then decide which words are best to be played
- Increase efficiency by using alternative method to brute force
  - A faster approach involving [The World's Fastest Scrabble Program](https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf)
  - Possibility of using RegEx

![Screenshot](https://github.com/andr3wV/words_with_friends_solver/blob/main/screenshot.png)
