
def eliminar_duplicados(lista):
	lista_sin_duplicados = []
	for i in lista:
		if i not in lista_sin_duplicados:
			lista_sin_duplicados.append(i)
	return lista_sin_duplicados

def main():
	lista = input("Ingresa una lista de números separados por comas: ")
	lista = lista.split(",")
	lista = [int(i) for i in lista]
	print(f"La lista sin duplicados es: {eliminar_duplicados(lista)}")

if __name__ == "__main__":
	main()