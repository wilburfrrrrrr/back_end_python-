
def celcius_to_farenheit(celcius):
	return celcius * 9/5 + 32

def farenheit_to_celcius(farenheit):
	return (farenheit - 32) * 5/9

def main():
	print("Selecciona la conversión que deseas realizar:")
	print("1. Celcius a Farenheit")
	print("2. Farenheit a Celcius")
	option = int(input("Elige una opción:"))

	if option == 1:
		celcius = float(input("Ingresa la temperatura en Celcius: "))
		print(f"La temperatura en Farenheit es: {celcius_to_farenheit(celcius)}")
	elif option == 2:
		farenheit = float(input("Ingresa la temperatura en Farenheit: "))
		print(f"LA temperatura en Celcius es: {farenheit_to_celcius(farenheit)}")
	else:
		raise ValueError("Opción no válida")

if __name__ == "__main__":
	try:
		main()
	except ValueError as ve:
		print(ve)
	
