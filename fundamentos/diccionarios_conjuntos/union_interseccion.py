
def main():
	set1 = set(input("Ingresa el primer conjunto: ").split(', '))
	set2 = set(input("Ingresa el segundo conjunto: ").split(', '))
	print(f"La interseccion de los conjuntos es: {set1 & set2}")
	print(f"La union de los conjuntos es: {set1 | set2}")

if __name__ == "__main__":
	main()