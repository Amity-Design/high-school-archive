from nltk.chat.util import Chat, reflections

pairs = [
    ["hi|hello", ["Hello!", "Hi there!"]],
    ["how are you?", ["I'm fine, thanks!", "Doing well, what about you?"]],
    ["quit", ["Goodbye!", "See you later!"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()


#this is my 1st comment exercise
# print('hello world')
# print('hello')
# print('world')

#data types
# print(type('hello world')) #String
# print(type(1)) #Integer
# print(type(1.5)) #Float
# print(type(False)) #Boolean
#
# # Expression/s
#print('Hello' * 100)

# 3 Types of Errors
# Syntax error
# print('Hello world!)

# Run-time error
# print('I can be displayed')
# print(1/0)
# print('I cannot be displayed')

# Logical error
# print('The sum of 5 and 10 is ', (5+10))

#Name Email Birthdate Age Contact Number Address Hobby Favorite color Favorite food and Motto
# print('Amteshwar S Chahal')
# print('Oct 2 2006')
# print(17)
# print('09997912889')
# print('Las villas via tuscany')
# print('Sleeping')
# print('Light blue')
# print('Chicken nuggets')
# print('Hi')

# Variables
#variable_name = value#
# greeting = 'hello world'
# print(greeting)
# num1 = 1
# print(num1)
# my_money = 1.5
# print(my_money)
# is_active = True
# print(is_active)

# print(type(greeting))
# print(type(num1))
# print(type(my_money))
# print(type(is_active))

# Concatenation
# Assignment operator
# first_word = 'Hello'
# second_word = 'World'
#
# combined_words = first_word + ' ' + second_word
#
# print(combined_words)
#
#I want you to create two variables named first name and last name
#Then concatenate both variable and display
# first_word = 'Amteshwar'
# second_word = 'Chahal'
# my_age = 1
# full_name = first_word + ' ' + second_word
# print('Welcome to python' , full_name, 'my age is' , my_age)
#
# Formatted String Literal
# print(f'Welcome to python {full_name} my age is {my_age}')

#variable_name = value
# full_name = 'Amteshwar S Chahal'
# email_address = 'amtesh.777@gmail.com'
# date_of_birth = 'October 2, 2006'
# age = 17
# phone_number = '09997912889'
# address = 'Las villas via tuscany'
# hobby = 'Sleeping'
# color = 'Light blue'
# food = 'Chicken nuggets'
# motto = "Hi"
#
# print(f'''
#
#  Your name is: {full_name}
#  The email you registered is: {email_address}
#  Your birthday is on {date_of_birth}
#  You are currently {age}
#  Your contact number is: {phone_number}
#  Your current address is: {address}
#  You love {hobby}
#  Your favorite color is {color}
#  Your favorite food is {food}
#  Your motto in life is {motto}
#
# ''')

