#	Program to Find the Eigen value and the Eigen Vector of a given Matrix
import numpy as np

##	To Find the Eigen value and the Eigen Vector of a given Matrix
def eigen(matrix, V = []) :

	if not V :
		V = [1 for i in matrix[0]]		#	Eigen	Vector

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
