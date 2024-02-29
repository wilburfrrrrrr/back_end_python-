
def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)
	
def main():
	number = int(input("Ingresa un número: "))
	print(f"El número en la posición {number} de la serie de Fibonacci es: {fibonacci(number)}")

if __name__ == "__main__":
	main()