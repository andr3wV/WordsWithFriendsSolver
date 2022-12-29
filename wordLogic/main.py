import solver
import tree
import settings
import board
import math
settings.init();

def read_text_file_to_array(file_path):
    # Open the text file in read mode
    with open(file_path, 'r') as f:
        # Read all the lines of the text file into a list
        lines = f.readlines()

    # Create an empty array to store the lines
    array = []

    # Iterate over the list of lines
    for line in lines:
        # Strip the newline character from the end of the line
        line = line.strip()
        # Append the line to the array
        array.append(line.lower())

    return array

# Use the function to read a text file and store the lines in an array
array = read_text_file_to_array('../image-processing/output/tessOutput.txt')    

####creates LetterTree from our dictionary####
def set_dict():
    with open('dictionary.txt', 'rt') as file:
        words = []
        for line in file:
            word = line.strip()
            words.append(word)
    return tree.LetterTree(words)

####change this to what tesseract outputs####
def set_board():
    exclude = ['[', ']', '-', '|']
    result = board.Board(15)
    for i in range(len(array)-1):
         if len(array[i])<=1 and '-' not in array[i] and '[' not in array[i] and ']' not in array[i] and '|' not in array[i]:
             result.set_tile((math.ceil(i/15-1),i%15-1),array[i])
    return result

#Data receieved from teserract will set the user's rack
def set_rack():
    rack = array[-1].split(",")
    return rack

#################TESTER BOARD##############################################
game = solver.SolveState(set_dict(), set_board(), set_rack()) 
print(game.board)
print()
game.find_all_options()
settings.wordList.sort(key=lambda x: x.points, reverse=True) # sorts word list by point value
print(settings.wordList[0].word)