#Create a program that gives the user four choices if the user input any of the choices the program prints a certain message

# number = input('Please choose a option from a to d')
#
# if number == 'a'  or number == 'A':
#     print('You have chosen the letter a')
# elif number == 'b' or number == 'B':
#     print('You have chosen the letter b')
# elif number == 'c' or number == 'C':
#     print('You have chosen the letter c')
# elif number == 'd' or number == 'D':
#     print('You have chosen the letter d')
# else:
#     print('that not a number')
#

#2.Age checker.
#Below 18 is minor above 18 is adult 65 and older is senior user input age
# age = int(input('What is your age?'))
#
# if age >= 65:
#     print('You are over 65!')
# elif age >= 18:
#     print('You are 18')
#
# else:
#     print('You are not 18')





#3.Month of the year.
#User input a number according to the month of the year after inputing the number the program prints out corresponding month.

# year = int(input('What is your month'))
#
# if year == 1:
#     print('January')
# elif year == 2:
#     print('February')
# elif year == 3:
#     print('March')
# elif year == 4:
#     print('April')
# elif year == 5:
#     print('May')
# elif year == 6:
#     print('June')
# elif year == 7:
#     print('July')
# elif year == 8:
#     print('August')
# elif year == 9:
#     print('September')
# elif year == 10:
#     print('October')
# elif year == 11:
#     print('November')
# elif year == 12:
#     print('December')





#4.Create a simple calculator
#Program ask what kind of operation does the user want
#The user inputs two number in division remainder should be printed.
#Result should be printed properly

# operator = input('Specify the math operation here (+, -, *, /, %): ')
# first_number = int(input('Add the first number here: '))
# second_number = int(input('Add the first number here: '))
#
# if(operator == '+'):
#     print(first_number + second_number)
# elif(operator == '-'):
#     print(first_number - second_number)
# elif(operator == '*'):
#     print(first_number * second_number)
# elif(operator == '/'):
#     print(first_number / second_number)
# elif(operator == '%'):
#     print(first_number % second_number)
# else:
#     print('Sorry, but I cannot understand your operation')


#5.Print a half triangle using nested loop
#program will ask you what symbol to use

# star = input('Please choose what symbol you want to use ')
# shape = star
# i = 1
# print(shape)
# while i == 1:
#     if len(shape) == 13:
#         break
#     elif len(shape) < 13:
#         shape += star
#         print(shape)
#
# while i == 1:
#     if len(shape) == 3:
#         break
#     elif len(shape) >= 3:
#         shape = shape[:-3]
#         print(shape)