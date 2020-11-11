##
## A keyboard layout analyzer , give it a file with all the keys and their relative pos
## The script will calculate how much you need to move your fingers in order to write words
##

# IMPORTS AND FILE READING #
import sys
keylayfile = sys.argv[1]
testwordfile = sys.argv[2]
testWords = open(testwordfile)
klay = open(keylayfile)

# VARIABLES #
nRightSide = 0
nWords = 0

# Function for calculating the steps your finger have to move to get to a certain key
# Sums this up for every key and returns it.
def distancetravelled(char, keyMatrix):
    global nRightSide, nWords
    poschar = []
    defaultkeys = [0, 1, 2, 3, 6, 7, 8]
    sumofstrokes = 10
    rightside = 0

    for i, j in enumerate(keyMatrix):
        for k, l in enumerate(j):
            if l == char:
                poschar = [i, k]

    for d in defaultkeys:
        if sumofstrokes > (abs(1 - poschar[0]) + abs(d - poschar[1])):
            sumofstrokes = (abs(1 - poschar[0]) + abs(d - poschar[1]))
            rightside = d

    if rightside > 3:
        nRightSide +=1

    nWords +=1
    return sumofstrokes


# Function generates the matrix of the keyboard layout 
def run():
    totalstrokes = 0

    with klay as f:
        keyMatrix = [[c for c in line] for line in f]

    with testWords as f:
        word = [c for c in testWords]
        for i, j in enumerate(word):
            for k, l in enumerate(j):
                totalstrokes = totalstrokes + distancetravelled(l, keyMatrix)
    print("total times fingers moved: " + str(totalstrokes))
    print("left/right side heavy (%): " + str((nRightSide/nWords)))


run()