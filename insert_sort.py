def insert_sort(arr):
	for i in range(1, len(arr)):
		key = arr.pop(i)
		print key, len(arr)
		for j in range(i, 0, -1):		
			if key >= arr[j - 1]:
				arr.insert(j, key)
				break
		else:
			arr.insert(0, key)
	return arr

arr = [5, 8, 5, 3, 0, 1, 3, 9, 4, 6, 7, 2]
print insert_sort(arr)