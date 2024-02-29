
def add(a, b):
	return a + b

def substract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	return a / b

def main():
	a = int(input("Ingresa el primer número: "))
	b = int(input("Ingresa el segundo número: "))
	print(f"{a} + {b} = {add(a, b)}")
	print(f"{a} - {b} = {substract(a, b)}")
	print(f"{a} * {b} = {multiply(a, b)}")
	print(f"{a} / {b} = {divide(a, b)}")

if __name__ == "__main__":
	main()
