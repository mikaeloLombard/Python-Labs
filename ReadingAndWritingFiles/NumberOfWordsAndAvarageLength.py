
import os

with open("mydata.txt", encoding="utf-8") as myFile:

    lineNum = 1

    while True:

        line = myFile.readline()

        if not line:
            break

        print("Line", lineNum)


        #split()
        wordList = line.split()

        #len()
        print("Numbers of Words:", len(wordList))

        #loop count characters in the word list
        charCount = 0

        for word in wordList:
            for char in word:
                charCount += 1


        # Avarege length by Divide character count / len word list
        avgNumChars = charCount/len(wordList)
        print("Avg Word Lenght : {:.2}" .format(avgNumChars))

        lineNum += 1

