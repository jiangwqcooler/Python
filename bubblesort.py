def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print arr
    return arr
array = [1,4,2,7,0,3,5,1,3,7,2,9,3,6,1]
print bubblesort(array)
