def insertionSort (aList):
    for index in range(1,len(aList)):

        currentValue = aList[index]
        position = index

        while position > 0 and aList[position-1] > currentValue:
            aList[position] = aList[position-1]
            print (aList)
            position = position - 1

        aList[position] = currentValue

aList = [54,26,93,17,77,31,44,55,20]

print ("original: ", aList)
insertionSort(aList)
print (aList)
