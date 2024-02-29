
def count_words(string):
	words = string.split()
	count = {}
	for word in words:
		if word in count:
			count[word] += 1
		else:
			count[word] = 1
	return count

def main():
	string = input("Ingresa una frase: ")
	print(count_words(string))

if __name__ == "__main__":
	main()