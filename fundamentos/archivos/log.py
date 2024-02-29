
def run():
	with open('text/log.txt', 'r') as f:
		for line in f:
			if 'ERROR' in line:
				print(line.strip())

if __name__ == '__main__':
	run()