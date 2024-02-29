
def main():
	word = input("Ingresa una frase: ")
	vowels = 0
	for letter in word:
		if letter in "aeiouAEIOU":
			vowels += 1
	print(f"La frase '{word}' tiene {vowels} vocales")

if __name__ == "__main__":
	main()