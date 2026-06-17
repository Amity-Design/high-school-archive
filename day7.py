# import random
#create a number guessing program using one user input to guess the correct answer

# password = input("what is the password?")
# if password == "abc":
#       print('Access Granted')
# else:
#       print('Access Denied')
#
# number = int(input('What number you want to pick'))
# number_to_guess = random.randint(0,9)
# if number == number_to_guess:
#     print('You picked the right number!')
# else:
#     print('You have picked the wrong number!')

# print(random.randint(0,9))

#create a program that checks weather user string input has more or less than 5 characters long

string_input = input('What is your name')

if len(string_input) < 5:
    print('Your character is below 5')
elif len(string_input) > 5:
    print('Your character is above 5')
else:
    print('Your character is exaclty 5')

