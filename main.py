import sys 
sys.path.append('./wordAlgo')
from wordAlgo import solver
from wordAlgo import tree
from wordAlgo import settings
from wordAlgo import board
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
array = read_text_file_to_array('./output/tessOutput.txt') 

####creates LetterTree from our dictionary####
def set_dict():
    with open('dictionary.txt', 'rt') as file:
        words = []
        for line in file:
            word = line.strip()
            words.append(word)
    return tree.LetterTree(words)

def set_board():
    #exclude = ['[', ']', '-', '|']
    result = board.Board(15)
    for i in range(len(array)-1):
        if i%2==0: 
            tileNum = array[i+1]
            result.set_tile((math.ceil(int(tileNum)/15-1),int(tileNum)%15-1),array[i])
    return result

# Data receieved from teserract will set the user's rack
def set_rack():
    rack = array[-1].split(",")
    return rack

# User input rack
def set_rack2():
    # Prompt the user to enter their rack
    rack = input("Enter your rack with spaces in between each letter: ")
    # Split the input string into a list of tiles
    rack = rack.split(" ")
    return rack

#################TESTER BOARD##############################################
#game = solver.SolveState(set_dict(), set_board(), set_rack2())
game = solver.SolveState(set_dict(), set_board(), ['m', 'o', 't', 'r', 'p', 'a', 'i'])
print(game.board)
print()
game.find_all_options()