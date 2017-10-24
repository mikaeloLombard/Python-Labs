import re

# Will look for the word ape and if ape is found, it will print "There is an ape"

if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# Will look for the word ape and it print the word ape
allApes = re.findall("ape", "The ape was at the apex")

for i in allApes:
    print(i)

#  Will look for the word ape and all words that begin with ape. Then it will print the word ape for each finding.

allApes2 = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

    