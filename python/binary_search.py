def binary_search(key, array):
	"""
		Алгоритм бинарного поиска 
	"""
	sorted_array = sorted(array)

	while True:
 		half_list = len(sorted_array) / 2
 		mid_elem = sorted_array[round(half_list)]

 		if mid_elem > key:
 			sorted_array = sorted_array[:round(half_list)]
 			print(sorted_array, mid_elem)
 		elif mid_elem < key:
 			sorted_array = sorted_array[round(half_list)+1:]
 			print(sorted_array, mid_elem)
 		elif mid_elem == key:
 			return "Nice job!"


nums = range(1, 26)

print(binary_search(15, nums))
