# particular para el problema
def mult(n):
	resultado = []
	numeros = range(1, n)
	for num in numeros:
		if ((num % 3 == 0) or (num % 5 == 0)):
			resultado.append(num)
	return resultado

multiplos = mult(1000)
total = sum(multiplos)

print total
