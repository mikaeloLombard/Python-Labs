
import os

def fiboNum (Fn):

    if Fn == 0:
        return 0

    elif Fn == 1:
        return 1
    else:
        result = fiboNum(Fn-1) + fiboNum(Fn-2)
        return result

# Ask how many numbers they want
numFibValues = int(input("How many Fibonacci values should be found? "))



# Loop while calling for each new number

i = 1
while i < numFibValues:
    fibValue = fiboNum(i)
     print(fibValue)

    i += 1

print("Task Completed")










