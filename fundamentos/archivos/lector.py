
def run():
	with open('text/poema.txt', 'r') as f:
		for line in f:
			print(line.strip().center(50))

if __name__ == '__main__':
	run()


