import random
import sys
import time

# Validate the user inputs actual numbers
def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def generateList(numItems, arrayLimit):
    if numItems > arrayLimit:
        print('The number of items must be lower than the array limit.')
        return False
    arrayToSort = random.sample(range(1, arrayLimit), numItems)
    return arrayToSort

def bubbleSort(arr):
    start = time.time()
    print('Beginning Bubble Sort . . . ( N = ', len(arr), ')')
    while not arr == sorted(arr):
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                pass    # Skip if it's already sorted
            else:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    end = time.time()
    print('Bubble Sort finished in ', end-start ,'seconds')

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if not is_int(arg):
            sys.exit("Both Array Size and Array Limit must be integers")
    arr = generateList(int(sys.argv[1]), int(sys.argv[2]))
    if not arr:
        print('TODO')
    else:
        bubbleSort(arr)