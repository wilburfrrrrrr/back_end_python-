
def main():
	numbers = [int(x) for x in input("Ingrese una lista de números separados por comas: ").split(",")]
	print(f"El número mayor es: {max(numbers)}")
	print(f"El número menor es: {min(numbers)}")

if __name__ == "__main__":
	main()