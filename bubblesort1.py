def bubblesort(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        for i in range(low, high):
            print low, high
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        for j in range(high, low, -1):
            print high, low
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

        high = high - 1
        low = low + 1
    return arr

array = [1,4,2,7,0,3,5,1,3,7,2,9,3,6,1]
print bubblesort(array)
