
def factorial(n):
	result = 1
	for i in range(1,n+1):
		result *= i
	return result

def factorial_while(n):
	result = 1
	i = 1
	while i <= n:
		result *= i
		i += 1
	return result

def main():
	number = int(input("Ingresa un número: "))
	print(f"El factorial de {number} es (ciclo for): {factorial(number)}")
	print(f"El factorial de {number} es (ciclo while): {factorial_while(number)}")

if __name__ == "__main__":
	main()