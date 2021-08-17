import sys

## Function to play friendship algorithm game  
def play_game():
	## START GAME

	# initialize the user input to 0
	user_entry = 0
	user_entry = int(user_entry)
	# ask the user to make their own input (1 to play or 2 to exit):
	while user_entry != 1 and user_entry != 2: user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
	# if the user selects 1, they want to play! Ask them questions and wait for their answers.
	while user_entry == 1:
		## STEP 1 HERE
		total_points = 0
		answer_one = int(input('Would you ever skinny dip in an alpine lake?\n1. Yes\n2. No\nYour answer: '))
		answer_two = int(input('Does your last name start with a letter before G (in the alphabet)?\n1. Yes\n2. No\nYour anser: '))
		answer_three = int(input('If you were playing rock-paper-scissors, what would you choose?\n1. Rock\n2. Paper\n3. Scissors\nYour answer: '))
		answer_four = int(input('Can you do a cartwheel?\n1. Yes\n2. No\nYour answer: '))
		answer_five = int(input('Do you like late night snacks?\n1. Yes\n2. No\nYour answer: '))
		answer_six = int(input('Do you like listening to electronic music?\n1. Yes\n2. No\nYour answer: '))
		answer_seven = int(input('Do you like a tasty IPA?\n1. Yes\n2. No\nYour answer: '))
		answer_eight = int(input('Who would win in a fight, a t-rex vs a pigeon?\n1. t-rex\n2. pigeon\nYour answer: '))
		answer_nine = int(input('Is cereal considered a soup?\n1. Yes\n2. No\nYour answer: '))
		answer_ten = int(input('Imagine a man biking (on a normal bike), with a third spare wheel in his hand. Is he technically riding a tricycle?\n1. Yes\n2. No\nYour answer: '))
		answer_eleven = int(input('Are plates actually just wide bowls?\n1. Yes\n2. No\nYour answer: '))

		## STEP 2&3 HERE
        #Q1 skinny dip
		if answer_one == 1: total_points += 5
		else: total_points -= 2
		#Q2 late letter
		if answer_two == 1: total_points += 2
		else: total_points -= 2
		#Q3 rock paper scissors
		if answer_three == 1: total_points += 5
		elif answer_three == 2: total_points += -2
		elif answer_three == 3: total_points += -2
		else: total_points += -5
		#Q4 cartwheel
		if answer_four == 1: total_points += 5
		else: total_points += 10
		#Q5 late snacks
		if answer_five == 1: total_points += 12
		else: total_points -= 2
		#Q6 edm
		if answer_six == 1: total_points += 4
		else: total_points -= 2
		#Q7 tasty ipa
		if answer_seven == 1: total_points += 3
		else: total_points -= 1
		#Q8 trex vs pigeon
		if answer_eight == 1: total_points += 3
		else: total_points -= 0
		#Q9 cereal soup
		if answer_eight == 1: total_points += 5
		else: total_points -= 2
		#Q10 bike
		if answer_eight == 1: total_points -= 5
		else: total_points += 10
		#Q11 plate
		if answer_eight == 1: total_points += 10
		else: total_points -= 5
		## STEP 4 HERE
		print("You received % points!",total_points)
		if total_points >= 50: print("Whaddup friend\n\n\n\n")
		elif total_points > 30: print("We can be really good friends, for sure.\n\n\n\n")
		elif total_points > 10: print("Sure, we can hang.\n\n\n\n")
		else: print("Frenemies? lol jk these weren't real questions ;)\n\n\n\n")
		
	user_entry = int(input('Select Option!\n1. Play Game\n2. Exit Game\n\nYour Selection: '))
	user_entry = int(user_entry)
	
	
## Function call to play friendship algorithm game
play_game()
