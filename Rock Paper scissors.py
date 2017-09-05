import random
import sys
import time
import getpass

gameOver = False


def Win(x,y,z):
	if clientTurn == x and computerTurn == y:
		print("_________________________________________________________")
		print('|player chooses {} player 2 chooses {}, {} wins|'.format(x,y,z))
		print("_________________________________________________________")

def main():
	try:
		while not gameOver:
			global clientTurn
			global computerTurn
			global cT

			cT = getpass.getpass('choose 1 for Rock,  2 for Paper,  3 for Scissors and 4 to quit: ')	
			computerRand = getpass.getpass('choose 1 for Rock,  2 for Paper,  3 for Scissors and 4 to quit: ')
			cT = int(cT)
			clientTurn = ''
			computerTurn = ''
			computerRand = 'random.randint(0,2)'

			if cT == 4:
				gameOver == True
				sys.exit()

			computerRand = random.randint(0,2)

			if computerRand == 0:
				computerTurn = 'Rock'

			if computerRand == 1:
				computerTurn = 'Paper'

			if computerRand == 2:
				computerTurn = 'Scissors'
			
			if cT == 1:
				clientTurn = 'Rock'

			if cT == 2:
				clientTurn = 'Paper'

			if cT == 3:
				clientTurn = 'Scissors'

			if clientTurn == computerTurn:
				print("_________________________________________________________")
				print('| player chooses {} player 2 chooses {}  its a draw.|'.format(computerTurn, clientTurn))
				print("_________________________________________________________")

			Win('Rock', 'Paper', 'player 2')
			Win('Paper', 'Scissors', 'player 2')
			Win('Scissors', 'Rock', 'player 2')

			Win('Paper', 'Rock', 'Player')
			Win('Scissors', 'Paper', 'Player')
			Win('Rock', 'Scissors', 'Player')

			clientTurn = ''
			computerTurn = ''

	except NameError:
		print("_________________________________________________________")
		print('| put a legit number |')
		print("_________________________________________________________")
		main()
	except SyntaxError:
		print("_________________________________________________________")
		print('| put a legit number |')
		print("_________________________________________________________")
		main()
	except ValueError:
		print("_________________________________________________________")
		print('| put a legit number |')
		print("_________________________________________________________")
		main()



main()
