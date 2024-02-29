
def main():
	list1 = input("Ingrese la primera lista de elementos separados por comas: ").split(",")
	list2 = input("Ingrese la segunda lista de elementos separados por comas: ").split(",")
	print(f"La concatenación de las listas es: {list1 + list2}")

if __name__ == "__main__":
	main()