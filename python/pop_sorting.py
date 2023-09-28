def pop_sorting(array):
	"""
		Алгоритм cортировки пузырьком
	"""

	result = array

	for j in result:
		for i in range(0, len(result)-1):
			if result[i] > result[i+1]:
				result[i], result[i+1] = result[i+1], result[i]
			elif result[i] < result[i+1]:
				continue
			else:
				continue

	return result

print(pop_sorting([4, 3, 7, 0, 5]))
print(pop_sorting([10, 64, 23, 23, 0]))
print(pop_sorting([1000, 523, 32, 111, 53]))
print(pop_sorting([65, 12, 54, 12, 52]))
print(pop_sorting([636, 2431, 235, 2535,]))
