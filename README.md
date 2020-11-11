## KeyboardAnalyzer
Python script for counting strokes your fingers have to move on a selectable keyboard layout to type a given txt file.

## Installation
1. Navigate to where you want to clone the repo.
2. `git clone https://github.com/KarlssonLucas/KeyboardAnalyzer `
3. Remember the path!

## How to use?
1. Navigate to the given path using your CLI of choice
2. To run it: `python KeyboardAnalyzer.py [keylayout] [txt file] ` ex. `python KeyboardAnalyzer.py dvorak.txt 10000words.txt ` 

## Creating your own keylayout and txtfiles
You can create your own keylayout files using the structure below, fill out all the empty places in the file with any specialcharachter (And no whitespaces)
example of this is the dvorak.txt file. It needs to be equal amount of charachters on every line:  
`___pyfgcrl `  
`aoeuidhtns `    
`_qjkxbmwvz `

Creating txtfiles for reading words is equally easy, you need to structure the file with a single word on each line without special charachters. Example below:  
`the`  
`as`  
`you`  
`fire`  
`asdasd`  
`wersvd`  
