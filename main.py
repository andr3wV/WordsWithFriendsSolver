import sys
import re
import Word as w


def main():
    global debug, wildcard
    ''' Wildcard is represented as this character '''
    wildcard = '?'
    debug = False

    try:
        letters = sys.argv[1]
    except IndexError:
        print('Please enter letters')
        exit(0)
    ''' Get all the possible words '''
    words = getWords(letters)

    ''' Score all of the possible words '''
    scoredWords = []
    for i in words:
        s = w.Word(i, score(i))
        scoredWords.append(s)

    ''' Sort the words in decending order based on their points '''
    newlist = sorted(scoredWords, key=lambda i: i.points, reverse=True)

    for i in newlist:
        print (i.word + ': ' + str(i.points))
    if len(newlist) > 0:
        print('\nHighest point word: ' +
              newlist[0].word + ' (' + str(newlist[0].points) + ' points)')
        print('Total possible words: ' + str(len(newlist)))
    else:
        print('No possible words.')


def score(word):
    ''' Define what each letter is worth in the game '''
    letterPoints = {
        'a': 1,
        'b': 4,
        'c': 4,
        'd': 2,
        'e': 1,
        'f': 4,
        'g': 3,
        'h': 3,
        'i': 1,
        'j': 10,
        'k': 5,
        'l': 2,
        'm': 4,
        'n': 2,
        'o': 1,
        'p': 4,
        'q': 10,
        'r': 1,
        's': 1,
        't': 1,
        'u': 2,
        'v': 5,
        'w': 4,
        'x': 8,
        'y': 3,
        'z': 10
    }
    ''' Calculate the score '''
    score = 0
    for ch in word:
        score = score + letterPoints[ch]
    return score


def getWords(letters):
    '''
    The words are categorized and saved in the folder based on their length.
    This is done for efficiency of the program.
    '''
    filepath = 'words/'
    possibleWords = []
    '''
    Starting from words of length 2. The last file to open will be the
    length of the letters string.
    '''
    for filename in range(2, len(letters) + 1):
        try:
            with open(filepath + str(filename)) as inF:
                for line in inF:
                    ''' Remove characters like the new line character '''
                    line = replaceNonAlnum(line)

                    '''
                    Only check the words that are less than or equal
                    to the length of the letters
                    '''
                    if len(line) <= len(letters):
                        good = False
                        ''' Copy the original letters string '''
                        tmp = letters
                        for char in line:
                            if char in tmp:
                                if (debug):
                                    print('Found: ' + char)
                                good = True
                                '''
                                Every time a letter from the tmp string is checked,
                                it is removed from the string. This is useful if the
                                letters string has duplicate letters.
                                '''
                                tmp = removeLetter(tmp, char)

                            elif hasWildcard(tmp):
                                '''
                                If letter from the word was not found in the tmp
                                letters, then check if there is a wildcard present. If
                                so, simply pass the letter as good.
                                '''
                                if (debug):
                                    print('Used Wildcard: ' + char)
                                good = True
                                tmp = removeLetter(tmp, '?')

                            else:
                                good = False
                                break

                        if good:
                            possibleWords.append(line)
        except FileNotFoundError:
            continue
    return possibleWords


def replaceNonAlnum(s):
    p = re.compile(r'[^a-zA-Z0-9:-]+')
    # p = re.compile(r'\W+') # replace whitespace chars
    new = p.sub(' ', s)
    return new.strip()


def removeLetter(s, c):
    indxToRemove = s.find(c)
    newStr = ''
    for i in range(len(s)):
        if i != indxToRemove:
            newStr = newStr + s[i]
    return newStr


def hasWildcard(s):
    return wildcard in s


if __name__ == '__main__':
    main()
