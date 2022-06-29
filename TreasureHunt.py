def start():
	#to start the game
	print("welcome to the game")
	print("You are standing in a dark room.")
	while True:
		print("There is a door to your left and right, which one do u take?press l for left and r for right:")
		ans=input()	
		if (ans.lower()=='l'):
			snake_room()
			break
		elif(ans.lower()=='r'):
			monster_room()
			break
		print("Please Enter the correct input")

	
def snake_room():
	print("\nYou are in snake room")
	print("There is a huge snake here")
	print("Behind the snake is another door")
	print("There are some eggs also")
	while True:
		print("what would you do?(1 or 2)")
		print("1. Take the eggs")
		print("2. Taunt the snake")
		ans=input()
		if ans =='1':
			game_over('snake')
			break
		elif ans=='2':
			treasure_room()
			break
		print("Please Enter the correct input")

	
def monster_room():
	print("\nNow you have entered the Monster's room.There is a Monster here")
	print("There is another door behind the Monster")
	while True:
		print("What would you do?(1 or 2)")
		print("1.Go through the door silently.")
		print("2.Kill the Monster and show your courage")
		ans = input()
		if ans=='1':
			treasure_room()
			break
		elif ans=='2':
			game_over('monster')
			break
		print("Please Enter the correct input")


def treasure_room():
	print("You are now in a room filled with Diamonds")
	print("And there is a door too")
	while True:
		print("What would you do?(1 or 2)")
		print("1. Take some Diamonds and go through the door")
		print("2. Go through the door without taking the Diamonds")
		ans= input()
		if ans=='1':
			win()
			break
		elif ans=='2':
			game_over('diamonds')
			break
		print("Please Enter the correct input")


def game_over(reason):
	#when game over
	print("Game Over")
	if reason=='snake':
		print("You tried to take the eggs and the snake ate you.")
	elif reason=='monster':
		print("The Monster Killed you.")
	elif reason =='diamonds':
		print("You ran away without taking the diamonds.")
	lets_play_again()

	
def win():
	#when player won the game
	print("Well Played")
	print("You won the game")
	lets_play_again()


def lets_play_again():
	#to play again
	while True:
		print("Do you want to play again?(y or n)")
		ans = input()
		if ans.lower()=='y':
			start()
			break
		elif ans.lower()=='n':
			exit()
			break
		print("Please Enter the correct input")


# Main Starting of the Game
start()					