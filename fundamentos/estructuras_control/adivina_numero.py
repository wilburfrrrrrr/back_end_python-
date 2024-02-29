
import random

def main():
	number = random.randint(1,10)
	guess = int(input("Adivina el número entre 1 y 10: "))
	if guess == number:
		print("¡Felicidades! Adivinaste el número")
	elif guess < number:
		print("El número es mayor")
	else:
		print("El número es menor")

if __name__ == "__main__":
	main()


