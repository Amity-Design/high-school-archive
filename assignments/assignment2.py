#Typecasting in python
#Casting, also known as type conversion, is a process that converts a variable's data type into another data type.
#These conversions can be implicit (automatically interpreted) or explicit (using built-in functions).
#
#Implicit conversion
#An implicit conversion exists from the null literal to any reference type or nullable value type.
# This conversion produces a null reference if the target type is a reference type,
#or the null value (§8.3. 12) of the given nullable value type.
#
#Explicit conversion
#An explicit conversion uses a type conversion keyword. Visual Basic provides several such keywords,
# which coerce an expression in parentheses to the desired data type. These keywords act like functions,
# but the compiler generates the code inline, so execution is slightly faster than with a function call.
#
# Explicit typecasting functions

# a = 10
# b = 2
# c = 2.03
#
# aa = int(c)
# bb = float(b)
# cc = str(a)
# print(aa)
# print(type(aa))
# print(bb)
# print(type(bb))
# print(cc)
# print(type(cc))

# type casting = The process of converting a value of one data type to another
#                          (string, integer, float, boolean)
#                          Explicit vs Implicit
#
# name = "Amit"
# age = 17
# gpa = 3.1
# student = True
# #
# print(type(name))
# print(type(age))
# print(type(gpa))
# print(type(student))
# #
# print('My name is ' + name + ' nice to meet you')
# print('i am ' + str(age) + ' years old')
# print('i have an gpa of ' + str(gpa) + ' it is cool')
# print('user is online = ' + str(student))


# age = float(age)
# print(age)
#
# gpa = int(gpa)
# print(gpa)
#
# student = str(student)
# print(student)
#
# name = bool(name)
# print(name)