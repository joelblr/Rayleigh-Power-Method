#	Program to Find the Eigen value and the Eigen Vector of a given Matrix

import numpy as np

##	To Find the Eigen value and the Eigen Vector of a given Matrix
def eigen(matrix, V = []) :

	if not V :		V = [1 for i in matrix[0]]		#	Eigen	Vector

	v = list(V)
	λ, ƛ = 0, 9999999				#	Eigen	Value
	k = 0

	while True :

		k += 1
		for i in range(len(V)) :
			v[i] = sum(list(np.multiply(matrix[i], V)))
		λ = round(abs(max(v, key = abs)), 4)
		V = list(np.around(np.array(v)/λ, 4))
		if abs(λ-ƛ) <= 0.001 :
			return(λ, V, k)
		ƛ = λ

##	__Main__
def main(matrix, V = []) :
	λ, V, k = eigen(matrix, V)

	print(f"\n{'>'*80}\n\tMatrix\n{'*'*80}")
	for i in matrix :
		ch = '\t'.join(list(map(str, i)))
		print(f"\t\t{ch}")
	print(f"{'*'*80}\n\tEigen Value\t{λ}\n\tEigen Vector\t{V}ᵀ\n{'<'*80}\n")

######################################################################
matrix = [
			[ 2, -1,  0],
			[-1,  2, -1],
			[ 0, -1,  2]	]
main(matrix)

matrix = [
			[ 6, -2,  2],
			[-2,  3, -1],
			[ 2, -1,  3]	]
main(matrix)

matrix = [
			[ 10,  2,  1],
			[  2, 10,  1],
			[  2,  1, 10]	]
main(matrix, V = [0, 0, 1])

matrix = [
			[ 10,  2,  1],
			[  2, 10,  1],
			[  2,  1, 10]	]
main(matrix, V = [1, 1, 1])

matrix = [
			[ 1, -3,  2],
			[ 4,  4, -1],
			[ 6,  3,  5]	]
main(matrix, V = [1, 0, 0])

matrix = [
			[ 2,  0,  1],
			[ 0,  2,  0],
			[ 1,  0,  2]	]
main(matrix, V = [1, 0, 0])

matrix = [
			[ 4,  1, -1],
			[ 2,  3, -1],
			[-2,  1,  5]	]
main(matrix, V = [1, 1, -1])

matrix = [
			[25,  1,  2],
			[ 1,  3,  0],
			[ 2,  0, -4]	]
main(matrix, V = [1, 0, 0])
######################################################################

