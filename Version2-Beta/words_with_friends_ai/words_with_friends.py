import random
from collections import Counter, deque

letter_values = {"A": 1, "B": 4, "C": 4, "D": 2, "E": 1, "F": 4, "G": 3, "H": 3, "I": 1, "J": 10, "K": 5, "L": 2,
                 "M": 4, "N": 2, "O": 1, "P": 4, "Q": 10, "R": 1, "S": 1, "T": 1, "U": 2, "V": 5, "W": 4, "X": 8,
                 "Y": 3, "Z": 10, "?": 0}

letter_counts = {"A": 9, "B": 2, "C": 2, "D": 5, "E": 13, "F": 2, "G": 3, "H": 4, "I": 8, "J": 1, "K": 1, "L": 4,
                 "M": 2, "N": 5, "O": 8, "P": 2, "Q": 1, "R": 6, "S": 5, "T": 7, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2,
                 "Z": 1, "?": 2}

modifiers = [[None, None, None, "TW", None, None, "TL", None, "TL", None, None, "TW", None, None, None],
             [None, None, "DL", None, None, "DW", None, None, None, "DW", None, None, "DL", None, None],
             [None, "DL", None, None, "DL", None, None, None, None, None, "DL", None, None, "DL", None],
             ["TW", None, None, "TL", None, None, None, "DW", None, None, None, "TL", None, None, "TW"],
             [None, None, "DL", None, None, None, "DL", None, "DL", None, None, None, "DL", None, None],
             [None, "DW", None, None, None, "TL", None, None, None, "TL", None, None, None, "DW", None],
             ["TL", None, None, None, "DL", None, None, None, None, None, "DL", None, None, None, "TL"],
             [None, None, None, "DW", None, None, None, None, None, None, None, "DW", None, None, None],
             ["TL", None, None, None, "DL", None, None, None, None, None, "DL", None, None, None, "TL"],
             [None, "DW", None, None, None, "TL", None, None, None, "TL", None, None, None, "DW", None],
             [None, None, "DL", None, None, None, "DL", None, "DL", None, None, None, "DL", None, None],
             ["TW", None, None, "TL", None, None, None, "DW", None, None, None, "TL", None, None, "TW"],
             [None, "DL", None, None, "DL", None, None, None, None, None, "DL", None, None, "DL", None],
             [None, None, "DL", None, None, "DW", None, None, None, "DW", None, None, "DL", None, None],
             [None, None, None, "TW", None, None, "TL", None, "TL", None, None, "TW", None, None, None]]

board_size = len(modifiers[0])


def create_empty_2d_board(dimension, default_val):
    return [[default_val for _ in range(dimension)] for _ in range(dimension)]


class BadPlayError(Exception):
    pass


class Board():
    def __init__(self, dict_path):
        self.tiles = create_empty_2d_board(board_size, None)
        self.modifiers = modifiers
        self.expended_modifiers = create_empty_2d_board(board_size, False)
        self.bag = deque(Counter(letter_counts).elements())
        self.letter_values = letter_values
        with open(dict_path) as f:
            self.dictionary = set(line.strip() for line in f)

    def grab_tile(self):
        random.shuffle(self.bag)
        return self.bag.pop()

    def print_board(self):
        for row in range(len(self.tiles)):
            print('+' + '---+' * len(self.tiles[0]))
            print('|', end='')
            for col in range(len(self.tiles[row])):
                if self.tiles[row][col] is None:
                    print("\t", end='|')
                else:
                    print(" " + self.tiles[row][col] + "\t", end='|')
            print(' ')  # To change lines
        print('+' + '---+' * len(self.tiles[0]))

    def play_word(self, word, rack: Counter, location: (int, int), direction, debug=False):
        """Plays a word in the direction given. Will see if you can play that word.
            If the word can be played, it plays it and returns the score of that word.
            If it cannot be played, raises a BadPlayError"""

        if location[0] < 0 or location[0] > board_size - 1 or location[1] < 0 or location[1] > board_size - 1:
            raise BadPlayError("Location out of bounds")

        word = word.upper().strip()
        if word not in self.dictionary:
            raise BadPlayError("Passed word not in dictionary")

        if direction == 'right':
            if not (location[1] == 0 or self.tiles[location[0]][location[1] - 1] is None):
                raise BadPlayError("Location given cannot be the start of the word")
        elif direction == 'down':
            if not (location[0] == 0 or self.tiles[location[0] - 1][location[1]] is None):
                raise BadPlayError("Location given cannot be the start of the word")
        else:
            raise BadPlayError("Bad direction")

        score, played_letters = self._get_score(direction, word, rack, [], location, 0, 1, [])

        # Mark multipliers as used and place tiles
        if not debug:
            rack.subtract(played_letters)
            if direction == 'down':
                for row in range(location[0], location[0] + len(word)):
                    self.tiles[row][location[1]] = word[row - location[0]]
                    self.expended_modifiers[row][location[1]] = True
            elif direction == 'right':
                for col in range(location[1], location[1] + len(word)):
                    self.tiles[location[0]][col] = word[col - location[1]]
                    self.expended_modifiers[location[0]][col] = True

        return score

    # TODO: Consider a faster approach that involves https://www.cs.cmu.edu/afs/cs/academic/class/15451-s06/www/lectures/scrabble.pdf
    def _get_score(self, direction, word, rack, played_letters, location, this_score, multiplier, other_scores):
        """
        :param direction: The direction of the play
        :param word: The remaining letters in the word to check
        :param rack: The contents of the rack to possibly use to build the word
        :param played_letters: The letters in the rack that have been used so far
        :param location: The currently checked location
        :param this_score: The sum of the currently checked tiles in word
        :param multiplier: A multiplier to apply at the end, based on DW and TW tiles we've passed
        :param other_score: The sum of the words that intersect with this word - every other word other than the one passed
        :return: The score that the original word will play for, and a list of all letters played to create that word
        """
        if len(word) == 0:  # We've gotten to the end of this word
            bonus = 0
            rack.update(played_letters)
            if rack - Counter(played_letters) == Counter():  # Bonus points for using the whole rack
                bonus += 35
            return self._calculate_score(bonus, multiplier, other_scores, this_score), played_letters
        this_letter = word[0]
        if self.tiles[location[0]][location[1]] is None:  # The tile needs to be placed from the rack
            # Play the tile
            if this_letter not in rack.elements():
                if '?' not in rack.elements():
                    rack.update(played_letters)  # Add back the played letters before bailing
                    raise BadPlayError("Needed letter not in rack")
                else:
                    rack['?'] -= 1
                    played_letters.append('?')
                    using_wildcard = True
            else:
                rack[this_letter] -= 1
                played_letters.append(this_letter)
                using_wildcard = False

            self.tiles[location[0]][location[1]] = this_letter

            # Validate the play's cross words
            # TODO: Simplify this mess lmao
            if (direction == 'down' and ((self.tiles[location[0]][location[1] - 1] is not None) or (
                    self.tiles[location[0]][location[1] + 1] is not None))) or (direction == 'right' and (
                    (self.tiles[location[0] - 1][location[1]] is not None) or (
                    self.tiles[location[0] + 1][location[1]] is not None))):
                if direction == 'down':
                    current_tile = self._get_cross_beginning_location(location, "horizontal")
                elif direction == 'right':
                    current_tile = self._get_cross_beginning_location(location, "vertical")

                cross_multiplier, cross_val, cross_word = self._get_cross_word(direction, current_tile, location,
                                                                               this_letter)

                if cross_word not in self.dictionary:
                    self.tiles[location[0]][location[1]] = None  # Reset the tile
                    rack.update(played_letters)  # Add back the played letters before bailing
                    raise BadPlayError("Secondary word not in dict", cross_word)
                else:  # It is in the dictionary! Add points
                    other_scores.append((cross_val, cross_multiplier))

            # Update score
            letter_score = self.letter_values[this_letter]
            if using_wildcard:
                letter_score = self.letter_values['?']
            if self._get_mod_info(location) is not None:
                mod_type, mod_val = self._get_mod_info(location)
                if mod_type == "word":
                    multiplier *= mod_val
                elif mod_type == "letter":
                    letter_score *= mod_val

            # Remove the tile in case of future error
            self.tiles[location[0]][location[1]] = None

            # Recurse
            if direction == 'down':
                return self._get_score(direction, word[1:], rack, played_letters, (location[0] + 1, location[1]),
                                       this_score + letter_score, multiplier, other_scores)
            elif direction == 'right':
                return self._get_score(direction, word[1:], rack, played_letters, (location[0], location[1] + 1),
                                       this_score + letter_score, multiplier, other_scores)

        else:  # The tile already exists, so the neighbors should already be valid, and we can ignore multipliers
            if self.tiles[location[0]][location[1]] != this_letter:
                rack.update(played_letters)
                raise BadPlayError("Existing letters down in the way")

            if direction == 'down':
                return self._get_score(direction, word[1:], rack, played_letters, (location[0] + 1, location[1]),
                                       this_score + self.letter_values[this_letter], multiplier, other_scores)
            elif direction == 'right':
                return self._get_score(direction, word[1:], rack, played_letters, (location[0], location[1] + 1),
                                       this_score + self.letter_values[this_letter], multiplier, other_scores)

    def _get_cross_word(self, direction, current_tile, location, this_letter):
        """
        Return the cross word and its value for a given location
        :param direction:
        :param current_tile:
        :param location:
        :param this_letter:
        :return:
        """
        cross_word = ''
        cross_val = 0
        cross_multiplier = 1
        # For every tile in the cross word
        while self.tiles[current_tile[0]][current_tile[1]] is not None:
            cross_word += self.tiles[current_tile[0]][current_tile[1]]
            # Check for modifiers if we are on the square we are placing
            if current_tile[0] == location[0] and current_tile[1] == location[1]:
                if self._get_mod_info(current_tile) is not None:
                    mod_type, mod_val = self._get_mod_info(current_tile)
                    if mod_type == "letter":
                        # Letter multiplier
                        cross_val += (self.letter_values[this_letter] * mod_val)
                    elif mod_type == "word":
                        # Add a secondary word multiplier to this cross word
                        cross_val += self.letter_values[this_letter]
                        cross_multiplier = mod_val
                else:
                    cross_val += self.letter_values[this_letter]
            else:
                cross_val += self.letter_values[self.tiles[current_tile[0]][current_tile[1]]]
            if direction == 'down':
                current_tile = (current_tile[0], current_tile[1] + 1)
            elif direction == 'right':
                current_tile = (current_tile[0] + 1, current_tile[1])

        return cross_multiplier, cross_val, cross_word

    def _calculate_score(self, bonus, multiplier, other_scores, this_score):
        return (this_score * multiplier) + sum(other_score * other_multiplier for other_score, other_multiplier in
                                               other_scores) + bonus

    def _get_cross_beginning_location(self, location, direction):
        if direction == 'horizontal':
            if location[1] == 0:
                return location
            if self.tiles[location[0]][location[1]] is None:
                return (location[0], location[1] + 1)
            return self._get_cross_beginning_location((location[0], location[1] - 1), direction)
        elif direction == 'vertical':
            if location[0] == 0:
                return location
            if self.tiles[location[0]][location[1]] is None:
                return (location[0] + 1, location[1])
            return self._get_cross_beginning_location((location[0] - 1, location[1]), direction)

    def _get_mod_info(self, location):
        invalid = self.expended_modifiers[location[0]][location[1]]
        if not invalid:
            modifier = self.modifiers[location[0]][location[1]]
            if modifier == 'DW':
                return "word", 2
            elif modifier == 'TW':
                return "word", 3
            elif modifier == 'DL':
                return "letter", 2
            elif modifier == 'TL':
                return "letter", 3
            else:
                return None
        else:
            return None
