import RPM

##	__Main__
def main(matrix, V = []) :
	λ, V, k = RPM.eigen(matrix, V)

	print(f"\n{'>'*80}\n\tMatrix\n{'*'*80}")
	for i in matrix :
		ch = '\t'.join(list(map(str, i)))
		print(f"\t\t{ch}")
	print(f"{'*'*80}\n\tEigen Value\t{λ}\n\tEigen Vector\t{V}ᵀ\n{'<'*80}\n")


if __name__ == "__main__" :
	import Inputs
	for key in Inputs.OBJ :
		M, V = Inputs.OBJ[key]["M"], Inputs.OBJ[key]["V"]
		main(M, V)