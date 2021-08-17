import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1:
		## STEP 1 HERE
		total_points=0
		answer_one= int(input('Do you enjoy learning about other people/cultures/differences?\n1. Yes\n2. No\nYour answer: '))
		answer_two= int(input('Do you appreciate animals and nature?\n1. Yes\n2. No\nYour answer: '))
		answer_three= int(input('Do you like to laugh?\n1. Yes\n2. No\nYour answer: '))
		answer_four= int(input('Do you like 420?\n1. Yes\n2. No\nYour answer: '))
		## STEP 2&3 HERE
		
		## STEP 4 HERE
		
	
		
		user_entry = input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: ')
		user_entry = int(user_entry)
	


	
## Function call to play friendship algorithm game
play_game()
