# Example of a nested if program
# Grade input program

# grade = float(input("Enter student's grade: "))
#
# if grade >= 90:
#     letter_grade = 'A'
#     # print("The letter grade is A.")
#     if grade >= 100:
#         print("WAW! SSSSSS++. Smart!")
#     elif grade >= 95:
#         print("Excellent work. Keep it up! A+")
#     else:
#         print("The letter grade is A.")
# elif grade >= 80:
#     letter_grade = 'B'
#     if grade >= 85:
#         letter_grade = 'B+'
#         print(f"You got a {letter_grade}!")
#     else:
#         print("The letter grade is B.")
# elif grade >= 70:
#     letter_grade = 'C'
#     if grade >= 75:
#         letter_grade = 'C+'
#         print(f"You got a {letter_grade}!")
#     else:
#         print("The letter grade is C.")
# elif grade >= 60:
#     letter_grade = 'D'
#     if grade >= 65:
#         letter_grade = 'D+'
#         print(f"You got a {letter_grade}!")
#     else:
#         print("The letter grade is D.")
# elif grade >= 50:
#     letter_grade = 'E'
#     if grade >= 55:
#         letter_grade = 'E+'
#         print(f"You got a {letter_grade}!")
#     else:
#         print("The letter grade is E.")
# elif grade >= 40:
#     letter_grade = 'F'
#     if grade >= 45:
#         print('you are an failure')
#         letter_grade = 'F+'
#         print(f"You got a {letter_grade}!")
#     else:
#         print("The letter grade is F.")
# # Make conditions for 70 (C), and 60 (D), and 50 (E), lesser than 50 (F)
# else:
#     print("Error.")
#
# # First way to declare List
# my_list = ["bmw", "ferrari", "toyota"]
# print(my_list)
#
# # Second way
# my_list2 = list(("bmw", "ferrari", "toyota"))
# print(my_list2)


# people = ['Bob', 'Mary']
# print(people[0])

# number = [1,2,3,4,5]
#
# print(1 in number)
# print(1 in number)
# print(6 not in number)


#create a list of 5 letters print the first and last element
# my_letter = ["A","B","C","D","Z"]
#
# my_letter.remove('D')
# print(my_letter)

# my_letter.append('F')
# print(my_letter)

# print ("The seceond element is B")
# print (my_letter[2])
# my_letter[2] = "J"
# print ("New value is this J")
# print (my_letter[2])


#
# print(1 in number)
# print(1 in number)
# print(6 not in number)
#######################################################################################################################
# 14.0.1.1 Empty Tuple
# people = ()

# 14.0.1.2 Tuple with initial values
# people = ('Bob', 'Mary')

# 14.0.2 Adding in a Tuple
# Tuples are immutable. This means that if you try to add an item, you will see an error.
# people = ('Bob', 'Mary')
# people[2] = 'Sarah'


# 14.0.3 Updating in a Tuple
# Update an item will also return an error.
# But there is a trick: you can convert into a list, change the item, and then
# convert it back to a tuple.
# people = ('Bob', 'Mary')
# people_list = list(people)
# people_list[1] = 'Sarah'
# people = tuple(people_list)
# print(people)
# ('Bob', 'Sarah')

# 14.0.4 Deleting in a Tuple
# For the same reason you can't add an item, you also can't delete an item,
# since they are immutable.

# 14.0.5 Retrieving in a Tuple
# Use the index to reference an ite
# people = ('Bob', 'Mary')
# print(people[1])
# Mary

# 14.0.6 Check if a given item already exists in a Tuple
# people = ('Bob', 'Mary')
# if 'Bob' in people:
# print('Bob exists!')
# else:
# print('There is no Bob!')

###################EXERCISE######################

#CREATE A TUPLE AND ACCESS THE 3 ELEMENTS

# magic = ('black magic', 'white magic', 'ye')
# print(magic[0])
# print(magic[2])

#UNPACKING TUPLES
# (green, yellow, red) = magic
#
# print(green)
# print(yellow)
# print(red)

# green = magic[0]
# yellow = magic[1]
# red = magic[2]
#
# print(green)
# print(yellow)
# print(red)

#Tuple concatenation create another tuple with 2 elements and add them to your main topic
# magic3 = ('water magic', 'fire magic')
# magic2 = (f'{magic + magic3}')
# print(magic2)