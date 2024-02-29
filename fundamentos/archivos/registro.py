
def run():
	name = input('Nombre: ')
	age = input('Edad: ')
	with open('text/registros.txt', 'a') as f:
		f.write(f"{name}: {age}\n")
	print('Datos guaradados con exito :D')

if __name__ == '__main__':
	run()