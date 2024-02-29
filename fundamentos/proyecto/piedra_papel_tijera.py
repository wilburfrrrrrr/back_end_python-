#create a rock paper scissors game, where the user plays against the computer

import random

def evalue_input(user):
	if user == 1:
		return 'Piedra'
	elif user == 2:
		return 'Papel'
	elif user == 3:
		return 'Tijera'
	else:
		return 'Opcion invalida'
	
def computer_choice():
	options = ['Piedra', 'Papel', 'Tijera']
	computer = random.choice(options)
	return computer

def compare(user, computer):
	if user == 'Piedra':
		if computer == 'Piedra':
			return 'Empate'
		elif computer == 'Papel':
			return 'Perdiste'
		else:
			return 'Ganaste'
	elif user == 'Papel':
		if computer == 'Piedra':
			return 'Ganaste'
		elif computer == 'Papel':
			return 'Empate'
		else:
			return 'Perdiste'
	elif user == 'Tijera':
		if computer == 'Piedra':
			return 'Perdiste'
		elif computer == 'Papel':
			return 'Ganaste'
		else:
			return 'Empate'
	else:
		return 'Opcion invalida'
	
def menu():
	print('Bienvenido a piedra, papel o tijera')
	print('1. Piedra')
	print('2. Papel')
	print('3. Tijera')

def main():
	menu()
	user = int(input('Elige una opcion: '))
	user = evalue_input(user)
	computer = computer_choice()
	print(f'La computadora eligio: {computer}')
	result = compare(user, computer)
	print(result)

if __name__ == '__main__':
	main()
