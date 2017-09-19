
myTuple = (1,2,3,5,8)

print("1st Value:", myTuple[0])

print(myTuple[0:3]) #it will not include the 3 which is 5

print("Tuple Lenght:" , len(myTuple))

moreFibs = myTuple + (13, 21, 34)

print("32 in Tuple : ", 34 in moreFibs)

for i in moreFibs:
    print(i)

aList = [55, 89, 144]        # list

aTuple = tuple(aList)       # from list to tuple

aList = list(aTuple)        # from tuple to list

print("Min :", min(aTuple))

print("Max :", max(aTuple))

