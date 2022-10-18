import solver
import tree
import settings
import board

settings.init();

#creates LetterTree from our dictionary
def set_dict():
    with open('dictionary.txt', 'rt') as file:
        words = []
        for line in file:
            word = line.strip()
            words.append(word)
    return tree.LetterTree(words)

#creates the board
def set_board():
    result = board.Board(15)
    result.set_tile((8, 7), 'g')
    result.set_tile((8, 8), 'o')
    result.set_tile((8, 9), 'a')
    result.set_tile((8, 10), 't')
    return result

#Data receieved from teserract will set the user's rack
def set_rack():
	return


#################TESTER BOARD##############################################
game = solver.SolveState(set_dict(), set_board(), ['f','r','i','h','l','s','o']) 
print(game.board)
print()
game.find_all_options()
settings.wordList.sort(key=lambda x: x.points, reverse=True) # sorts word list by point value
print(settings.wordList[0].word)