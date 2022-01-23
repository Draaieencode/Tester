import time

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
import random
import math
print('Okay! Here we go, pick the range of number i pick from')
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

#Win ? Find monkey picture
#Los? find hypopotamus picture

import requests
import Beautifulsoup
from bs4 import Beautifulsoup

def getdata(url):
	r = requests.get(url)
	return r.text
html = getdata("https://google.com/ape")
soup = Beautifulsoup(htmldata, 'html.parser')
for item in soup.find_all('img'):
	print(item['src'])


#while true:
# usr_input_bole: str = input('Would you like to play a game? Y/N').lower()
#    if usr_input_bole == 'Y'
#  print('Hurray! Lets start!')
#   elif == 'N'
#   print('Such a shame...')
# else
#   print('I asked for Y/N')
