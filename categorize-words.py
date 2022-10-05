import re

''' Unsued '''


def categorizeByAlphabet(filename):
    folder = 'words/'
    with open(filename, 'r') as inF:

        for word in inF:
            letter = word[0]

            with open(folder + letter, 'a') as outF:
                outF.write(word + '\n')


''' This is used by this program '''


def categorizeByLength(filename):
    folder = 'words/'
    with open(filename, 'r') as inF:

        for word in inF:
            length = str(len(replaceNonAlnum(word)))

            with open(folder + length, 'a') as outF:
                outF.write(word + '\n')


def replaceNonAlnum(s):
    p = re.compile(r'[^a-zA-Z0-9:-]+')
    # p = re.compile(r'\W+') # replace whitespace chars
    new = p.sub(' ', s)
    return new.strip()


categorizeByLength('enable-word-list.txt')
