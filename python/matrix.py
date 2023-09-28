def spiral_matrix(m, n):
	"""
		Заполнение матрицы по спирали
	"""

	matrix = []

	for i in range(n):
		matrix.append([0]*m)

	return matrix

print(*spiral_matrix(3, 3), sep="\n")