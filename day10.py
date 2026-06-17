# Functions - blocks of code that you can use or re-use inside your program.
# Good example - arrow keys or WASD movements in game

# def my_function(first_name, last_name): #Parameter
#     print(f"Hi {first_name} {last_name}")
#     print("Welcome aboard")
#
#
# print("Start")
# # Argument
# my_function("Poblador", "John")
# print("End")
####################################
# def square(number):
#     result = number * number
#     return result
#
#     # if return no declared, default value of function will be: None
#
# # CONVENTION
# result_func = square(10)
# print(result_func)

# Arbitrary Arguments

# def my_function(*kids):
#     print("The youngest child is " + kids[0])
#
#
# my_function("Jann", "Amit", "Shan")
# def my_function():
#     print('Hello world')
# my_function()

#Create a functions that prints the three starter pokemon emerald

# def my_function(pokemons):
#     print(f'One of the three pokemons of emerald is {pokemons}')
# my_function("Mudkip")
# my_function("Torchik")
# my_function("Treecko")

#Create a function that sums up two number use two user input to get desired argument. Create a third variable for result.
# def function(number, number1):
#     return number + number1
# a = int(input("Choose a number"))
# b = int(input("Choose a number"))
# result = function(a,b)
# print(result)

#Since you have your sum function create a seperate function for substraction, multiplication division (and remainder) and lastly exponent
# def function(number, number1):
#     return number - number1
# a = int(input("Choose a number"))
# b = int(input("Choose a number"))
# result = function(a,b)
# print(result)
#
# def function2(multiplication, multiplication1):
#     return multiplication * multiplication1
# a = int(input("Choose a number"))
# b = int(input("Choose a number"))
# result = function2(a,b)
# print(result)
#
# def function3(division, division1):
#     return division / division1
# a = int(input("Choose a number"))
# b = int(input("Choose a number"))
# result = function3(a,b)
# print(result)
#
# def function4(remainder, remainder1):
#     return remainder % remainder1
# a = int(input("Choose a number"))
# b = int(input("Choose a number"))
# result = function4(a,b)
# print(result)
#
# def function5(exponent, exponent1):
#     return exponent ** exponent1
# a = int(input("Choose a number"))
# b = int(input("Choose a number"))
# result = function5(a,b)
# print(result)

#Challenge number 3### one by one using for loop hint:the list is an argument to be passed inside your parameter
#Create a function that prints out a list argument
# def function(number):
#     for x in number:
#         print(x, end=" ")
#
# wowie = ['wow', 'wowe','wower']
#
# function(wowie)
