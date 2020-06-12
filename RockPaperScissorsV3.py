# Rock, Paper, Scissors + Sleep function to delay the computer

import random, time, sys # time module for the mini pauses in the sleep function.
						 # sys to allow player to exit the game.

print('ROCK, PAPER, SCISSORS')
print('By Jonathan Lo')
print() # Blank line right here
print('- Rock beats scissors.')
print('- Paper beats rocks.')
print('- Scissors beats paper.')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
	while True: # Keep asking until player enters R/P/S/Q.
		print(f'{wins} Wins, {losses} Losses, {ties} Ties')
		print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
		playerMove = input().upper() # Allows player to type either upper or lower case, 
									 # saved to a variable called playerMove.
		if playerMove == 'Q':
			sys.exit() 

		if playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
			break
		else:
			print('Type one of R, P, S, or Q.')

	if playerMove == 'R':
		print('ROCK versus...')
		playerMove = 'ROCK'
	elif playerMove == 'P':
		print('PAPER versus...')
		playerMove = 'PAPER'
	elif playerMove == 'S':
		print('SCISSORS versus...')
		playerMove = 'SCISSORS'

	# Count to three with dramatic pauses:
	time.sleep(0.5)
	print('1...')
	time.sleep(0.25)
	print('2...')
	time.sleep(0.25)
	print('3...')
	time.sleep(0.25)

	# Display what the computer chose:
	randomNumber = random.randint(1, 3)
	if randomNumber == 1:
		computerMove = 'ROCK'
	elif randomNumber == 2:
		computerMove = 'PAPER'
	elif randomNumber == 3:
		computerMove = 'SCISSORS'

	print(computerMove)

	# Display and record the win/lose/tie:
	if playerMove == computerMove:
		print('It\'s a tie!') # \ Tells python that the apostrophe is a part of the str.
		ties += 1 # Increase the value in ties by 1.
	elif playerMove == 'ROCK' and computerMove == 'SCISSORS':
		print('You win!')
		wins += 1 # Increase the value in wins by 1.
	elif playerMove == 'PAPER' and computerMove == 'ROCK':
		print('You win!')
		wins += 1 
	elif playerMove == 'SCISSORS' and computerMove == 'PAPER':
		print('You win!')
		wins += 1 
	elif playerMove == 'ROCK' and computerMove == 'PAPER': # Handling loss cases
		print('You lose!') 
		losses += 1
	elif playerMove == 'PAPER' and computerMove == 'SCISSORS':
		print('You lose!')
		losses += 1
	elif playerMove == 'SCISSORS' and computerMove == 'ROCK':
		print('You lose!') 
		losses += 1


