
def synonyms():
	synonyms = {
		'casa': ['hogar', 'vivienda', 'residencia'],
		'perro': ['can', 'chucho', 'perrito', 'canino'],
		'gato': ['minino', 'michino', 'felino', 'félido'],
		'feliz': ['contento', 'alegre', 'gozoso', 'regocijado'],
		'cansado': ['fatigado', 'agotado', 'extenuado', 'reventado']
	}
	word = input('Dame una palabra: ')
	if word in synonyms:
		print(f'Los sinónimos de {word} son:')
		for synonym in synonyms[word]:
			print(synonym)
	else:
		print(f'No tengo sinónimos de {word}')

def main():
	synonyms()

if __name__ == "__main__":
	main()