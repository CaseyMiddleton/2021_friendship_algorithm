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
		total_points = 0

		## QUESTION 1
		answer_one = input('Select Option!\n1.I have a pet.\n2. I do not have a pet.\n\nYour Selection: ')
		if answer_one == 1:
			total_points=+5
			answer_one_b = input('Select Option!\n1.I have a dog.\n2. I have another type of pet.\n\nYour Selection: ')
			if answer_one_b == 1:
				total_points=+5
			else
				break
		else
			answer_one_c = input('Select Option!\n1.I like dogs\n2. I do not like dogs.\n\nYour Selection: ')
			if answer_one_b == 1:
				total_points=+3
			else
				break

		## QUESTION 2
		answer_two = input('Select Option!\n1.I like sports.\n2. I do not like sports.\n\nYour Selection: ')
		if answer_two == 1:
			total_points = +5
			answer_two_b = input('Select Option!\n1.I like to play sports.\n2. I only like to watch sports.\n\nYour Selection: ')
			if answer_two_b == 1:
				total_points = +5
			else
				break
		else
			answer_two_c = input('Select Option!\n1.I tolerate sports\n2. I hate sports.\n\nYour Selection: ')
			if answer_two_c == 1:
				total_points = +3
			else
				break
		## QUESTION 3
		answer_two = input('Select Option!\n1.I like to play video games.\n2. I do not like to play video games.\n\nYour Selection: ')
		if answer_two == 1:
			total_points = +5
			answer_two_b = input('Select Option!\n1.I like to play computer games.\n2. I like to game on other consoles.\n\nYour Selection: ')
			if answer_two_b == 1:
				total_points = +5
			else
				break
		else
			answer_two_c = input('Select Option!\n1.I like to play other type of games\n2. I hate any type of games.\n\nYour Selection: ')
			if answer_two_c == 1:
				total_points = +3
			else
				break

		if total_points >= 20
			print("Great Friends!")
		elif total_points >= 15
			print("Friends!")
		else
			print("Maybe we can be friends later...")
	


	
## Function call to play friendship algorithm game
play_game()
