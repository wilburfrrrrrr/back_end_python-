
def shopping_list():
	shopping = []
	while True:
		item = input('Que vamos a comprar?: ')
		if item == '':
			break
		shopping.append(item)
	shopping.sort()
	print('\nOk, necesitamos comprar estas cosas:')
	for item in shopping:
		print(item)

def main():
	shopping_list()

if __name__ == "__main__":
	main()