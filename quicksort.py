def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

#array = raw_input("please input array:")
array = [1,4,2,7,0,3,5,1,3,7,2,9,3,6,1]
print quicksort(array)