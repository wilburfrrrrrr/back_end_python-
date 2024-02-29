
agenda = {
	"Juan": 123456789,
	"Pedro": 987654321,
	"Maria": 123123123,
	"Pizza": 555555555,
	"Drogueria": 444444444
}

def add_contact(name, number):
	agenda[name] = number
	print(f"Contacto {name} agregado")

def delete_contact(name):
	if name in agenda:
		del agenda[name]
		print(f"Contacto {name} eliminado")
	else:
		print(f"Contacto {name} no existe")

def modify_contact(name, number):
	if name in agenda:
		agenda[name] = number
		print(f"Contacto {name} modificado")
	else:
		print(f"Contacto {name} no existe")

def show_agenda():
	print("Agenda:")
	for name, number in agenda.items():
		print(f"{name}: {number}")

def main():
	while True:
		print("1. Agregar contacto")
		print("2. Eliminar contacto")
		print("3. Modificar contacto")
		print("4. Mostrar agenda")
		print("5. Salir")
		option = int(input("Opción: "))

		if option == 1:
			name = input("Nombre: ")
			number = int(input("Número: "))
			add_contact(name, number)
		elif option == 2:
			name = input("Nombre: ")
			delete_contact(name)
		elif option == 3:
			name = input("Nombre: ")
			number = int(input("Número: "))
			modify_contact(name, number)
		elif option == 4:
			show_agenda()
		elif option == 5:
			break
		else:
			raise ValueError("Opción no válida")

if __name__ == "__main__":
	try:
		main()
	except ValueError as ve:
		print(ve)