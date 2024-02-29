
def convert(amount, rate, margin=0):
	return amount * rate * (1 + margin)

def main():
	amount = float(input("Ingresa la cantidad de dinero: "))
	rate = float(input("Ingresa el tipo de cambio: "))
	margin = float(input("Ingresa el margen de ganancia: "))
	print(f"El monto final es: {convert(amount, rate, margin)}")

if __name__ == "__main__":
	main()

