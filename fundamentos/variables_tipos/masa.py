
def imc(weight, height):
	return weight / height ** 2

def main():
	weight = float(input("Ingrese peso en Kg: "))
	height = float(input("Ingrese altura en metros: "))
	print(f"Your IMC is: {imc(weight, height):.2f}")

if __name__ == "__main__":
	main()



