
# theArray is just a given array of values.
def cocktail_shaker_sort(theArray):
    swapped = true
    while swapped:
        swapped = false
        # Do swapping in one direction.
        for i in range(0, len(theArray) - 1, 1):
            if theArray[i] > theArray[i + 1]:
                temp = theArray[i]
                theArray[i] = theArray[i + 1]
                theArray[i + 1] = temp
                swapped = true
        if swapped == false:
            break
        swapped = false
        # Do swapping in the other direction.
        for i in range(len(theArray) - 1, 0, -1):
            if theArray[i] > theArray[i + 1]:
                temp = theArray[i]
                theArray[i] = theArray[i + 1]
                theArray[i + 1] = temp
                swapped = true