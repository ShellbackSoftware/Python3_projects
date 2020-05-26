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

def mergeSort(arr):
    arrLength = len(arr)
    if arrLength > 1:
        mid =  arrLength // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]
        # Sort both halves
        mergeSort(leftArr)
        mergeSort(rightArr)

        leftIndex = rightIndex = index = 0
        # Utilize the two temp arrays
        while leftIndex < len(leftArr) and rightIndex < len(rightArr):
            if(leftArr[leftIndex] < rightArr[rightIndex]):
                arr[index] = leftArr[leftIndex]
                leftIndex += 1
            else:
                arr[index] = rightArr[rightIndex]
                rightIndex += 1
            index += 1

        # Check for remaining items
        while leftIndex < len(leftArr):
            arr[index] = leftArr[leftIndex]
            leftIndex += 1
            index =+ 1

        while rightIndex < len(rightArr):
            arr[index] = rightArr[rightIndex]
            rightIndex += 1
            index =+ 1


def insertSort(arr):
    start = time.time()
    print('Beginning Insertion Sort . . . ( N = ', len(arr), ')')
    for idx in range (1, len(arr)):
        target = idx
        while target > 0 and arr[target-1] > arr[target]:
            arr[target-1] = arr[target]
            target =- 1
        idx =+ 1
    end = time.time()
    print('Insertion Sort finished in ', end-start ,'seconds')

def selectSort(arr):
    start = time.time()
    print('Beginning Selection Sort . . . ( N = ', len(arr), ')')
    end = time.time()
    print('Selection Sort finished in ', end-start ,'seconds')

def quickSort(arr):
    start = time.time()
    print('Beginning Quick Sort . . . ( N = ', len(arr), ')')
    end = time.time()
    print('Quick Sort finished in ', end-start ,'seconds')

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        if not is_int(arg):
            sys.exit("Both Array Size and Array Limit must be integers")
    arr = generateList(int(sys.argv[1]), int(sys.argv[2]))
    if not arr:
        sys.exit("The first parameter must be smaller than the second.")
    else:
        #bubbleSort(arr)
        print('Beginning Merge Sort . . . ( N = ', len(arr), ')')
        start = time.time()
        mergeSort(arr)
        end = time.time()
        print('Merge Sort finished in ', end-start ,'seconds')
        insertSort(arr)