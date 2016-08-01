def select_sort(arr):
	for i in range(0, len(arr)):
		key = arr[i]
		tmp = 0
		for j in range(i + 1, len(arr)):
			if key > arr[j]:
				key = arr[j]
				tmp = j
		else:
			if tmp == 0:
				print "no exchange"
			else:
				arr.insert(i, key)
				arr.pop(tmp + 1)
				tmp = 0
	return arr
	
arr = [5, 8, 5, 3, 4, 9, 1, 0, 7, 2, 12]
print select_sort(arr)