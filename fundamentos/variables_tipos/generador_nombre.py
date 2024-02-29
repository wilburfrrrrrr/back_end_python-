
def main():
	name = input("Ingrese nombre: ")
	last_name = input("Ingrese apellido: ")
	birth_year = input("Ingrese año de nacimiento: ")
	print(f"Nuevo nombre de usuario: {name[:3]}{last_name[:3]}{birth_year[-2:]}")

if __name__ == "__main__":
	main()