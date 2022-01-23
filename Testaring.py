import time
import webbrowser
import random
import math


usr_input = input('Hi, what would your name be?')
print('Hello' + " " + usr_input + ' \nHow old are you?')
Usr_input_age = input()
print('Wow !!!!' + ' ' + usr_input + ', ' + Usr_input_age + ' ' + 'is quite old... ><')
# Wait response
time.sleep(1)
print('Sorry! Just a joke... Lets play a game!')
usr_answ = input('Want to play? Y/N').lower()
while True:
	if usr_answ == 'yes' or usr_answ == 'y':
		print('Yes! Lets go')
		break
	elif usr_answ == 'no' or usr_answ == 'n':
		print('Hey! Thats the wrong answer')
		break
	else:
		print('I asked yes or no, no ifs or buts')
		break
time.sleep(1)

print('Okay! Here we go, pick the range of numbers that i will pick from')
#Taking low input
lower = int(input('Enter lowest number:-'))
#Taking high input
upper = int(input('Enter highest number:-'))
#Generating number
x = random.randint(lower,upper)
print("\n\tYou've only ",
	  round(math.log(upper - lower + 1, 2)),
	  " chances to guess the right number!\n")
# Initializing the number of guesses.
count = 0

# for calculation of minimum number of
# guesses depends upon range
while count < math.log(upper - lower + 1, 2):
	count += 1

	# taking guessing number as input
	guess = int(input("Guess a number:- "))

	# Condition testing
	if x == guess:
		print("Congratulations you did it in ",
			  count, " try")
		input("Your price is ready! are you?")
		time.sleep(1)
		webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/4/4e/Macaca_nigra_self-portrait_large.jpg')
		# Once guessed, loop will break
		break
	elif x > guess:
		print("You guessed too small!")
	elif x < guess:
		print("You Guessed too high!")

# If Guessing is more than required guesses,
# shows this output.
if count >= math.log(upper - lower + 1, 2):
	print("\nThe number is %d" % x)
	print("\tBetter Luck Next time!")
	print("Thats a bummer! Here is a present")
	input('Are you ready for your present?')
	time.sleep(1)
	webbrowser.open('https://media.istockphoto.com/photos/grown-hippopotamus-aged-30-years-on-a-white-background-picture-id93216623?s=612x612')



#Win ? Find monkey picture
#Los? find hypopotamus picture



