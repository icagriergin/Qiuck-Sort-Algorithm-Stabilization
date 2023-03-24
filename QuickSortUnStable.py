def PartitionArray(myArray, lowestIndex, highestIndex):
    i = (lowestIndex - 1)
    pivot = myArray[highestIndex]

    for j in range(lowestIndex, highestIndex):
        if myArray[j] <= pivot:
            i = i + 1
            myArray[i], myArray[j] = myArray[j], myArray[i]

    myArray[i + 1], myArray[highestIndex] = myArray[highestIndex], myArray[i + 1]
    return (i + 1)

def QuickSort(myArray, lowestIndex, highestIndex):
    if len(myArray) == 1:
        return myArray
    if lowestIndex < highestIndex:
        partionIndex = PartitionArray(myArray, lowestIndex, highestIndex)
        QuickSort(myArray, lowestIndex, partionIndex - 1)
        QuickSort(myArray, partionIndex + 1, highestIndex)


myArray = [5,2,9,3,12,16,1,22]
lengthOfArray = len(myArray)
QuickSort(myArray, 0, lengthOfArray - 1)
print("Sorted array is: {}".format(myArray))
