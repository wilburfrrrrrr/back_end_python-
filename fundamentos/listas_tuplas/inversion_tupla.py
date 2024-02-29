
def invertir_tupla(tupla):
	return tupla[::-1]

def main():
	tupla = (1,2,3,4,5)
	print(f"Tupla original: {tupla}")
	print(f"Tupla invertida: {invertir_tupla(tupla)}")

if __name__ == "__main__":
	main()

