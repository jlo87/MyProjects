from random import randint
# print("Rock...")
# print("Paper...")
# print("Scissors...")

player = input("Player, make your move: ")
rand_num = randint(0,2)
if rand_num == 0:
	computer = "rock"
elif rand_num == 1:
	computer = "paper"
else:
	compter = "scissors"
	
# f string concatenates. this string will now show computer plays
print(f"Computer plays {computer}" ) 

if player == computer:
	print("It's a tie!")
elif player == "rock":
	if computer == "scissors":
		print("player wins!")
	elif computer == "paper":
		print("computer wins!")
elif player == "paper":
	if computer == "rock":
		print("player wins!")
	elif computer == "scissors":
		print("computer wins!")
elif player == "scissors":
	if computer == "paper":
		print("player wins!")
	elif computer == "rock":
		print("computer wins!")
else:
	print("something went wrong")
