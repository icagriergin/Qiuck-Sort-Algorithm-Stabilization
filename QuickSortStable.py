def QuickSort(myArray):
    if len(myArray) <= 1:
        return myArray
    else:
        middleIndex = int(len(myArray) / 2)
        pivot = myArray[middleIndex]
        smallerThanPivot, greaterThanPivot = [], []
        for arrayIndex, arrayVal in enumerate(myArray):
            if arrayIndex != middleIndex:
                if arrayVal < pivot:
                    smallerThanPivot.append(arrayVal)
                elif arrayVal > pivot:
                    greaterThanPivot.append(arrayVal)
                else:
                    if arrayIndex < middleIndex:
                        smallerThanPivot.append(arrayVal)
                    else:
                        greaterThanPivot.append(arrayVal)
        return QuickSort(smallerThanPivot) + [pivot] + QuickSort(greaterThanPivot)

myArray  = [5,2,9,3,12,16,1,22]
sortedArray = QuickSort(myArray)
print("Sorted array is: {}".format(sortedArray))
