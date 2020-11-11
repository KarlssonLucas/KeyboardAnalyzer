##
## A keyboard layout analyzer , give it a file with all the keys and their relative pos
## The script will calculate how much you need to move your fingers in order to write words
##

#klay = open("dvorak.txt")
klay = open("colemak.txt")
#klay = open("qwerty.txt")

testWords = open("randoms.txt")


def distancetravelled(char, keyMatrix):
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

    return sumofstrokes


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
    #print("left/right side heavy (%): " + -- + " / " + --)
    #print("total words counted      : " + str(totalstrokes))


run()

#TODO - Right/left side heavy
#TODO - counter for words
#TODO - cleanup and comment the code
#TODO - Modularity for what file to run
