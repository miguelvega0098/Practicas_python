"""
Este codigo pretende construir la famosa sucesion de Fibonacci.
Donde F(n) = F(n-1) + F(n-2)
Ademas F(0) = 1 y F(1) = 1
1; 1; 2; 3, 5; 8; 13; 21; 34; 55; 89
"""
# Para que la funcion no use tantos recursos definimos un diccionario
fibo_dict = dict()

#Funcion recursiva de Fibonacci
def fibonacci(num:int) -> int:
	num =  int(num)
	if num == 0 or num == 1:
		print("{} -> 1".format(num))
		return 1
	elif num < 0:
		raise Exception("La sucecion de Fibonacci solo es valida para numeros naturales y el 0")

# Hay que verificar si el valor de la serie ya se encuentra en el diccionario y si no se encuentra habra que agregarlo

	if num in fibo_dict:
		print("Fibonacci({}) se encuentra en el diccionario".format(num))
		return fibo_dict[num]

	print("{} -> {}, {}".format(num, num-1, num-2))
	res = fibonacci(num - 1) + fibonacci(num - 2)
	fibo_dict[num] = res
	return res 
numero = input("Introduce un numero ")
print("el valor de Fibonacci({}) = {}".format(numero, fibonacci(numero)))


