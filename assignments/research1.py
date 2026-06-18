
# 1. Python Arithmetic Operators
# Mathematical operations including addition, subtraction, multiplication,
# and division are commonly carried out using Python arithmetic operators.
# They are compatible with integers, variables, and expressions.
# In addition to the standard arithmetic operators, there are operators for modulus, exponentiation, and floor division.
# Operator	Name	Example
#    +	  Addition	10 + 20 = 30

# 2. Python Comparison Operators
# To compare two values, Python comparison operators are needed.
# Based on the comparison, they produce a Boolean value (True or False).
# Operator	Name	Example
#  ==	   Equal    4 == 5 is not true.

# 3. Python Assignment Operators
# Python assignment operators are used to assign values to variables in Python.
# The single equal symbol (=) is the most fundamental assignment operator.
# It assigns the value on the operator's right side to the variable on the operator's left side.
#Operator	Name	Example
#  =   Assignment   Operator a = 10
#
# 4. Python Bitwise Operators
# Python bitwise operators execute operations on individual bits of binary integers.
# They work with integer binary representations, performing logical operations on each bit location.
# Python includes various bitwise operators, such as AND (&), OR (|), NOT (), XOR (), left shift (), and right shift (>>).
#Operator	 Name	   Example
#   &	   Binary AND	Sets each bit to 1 if both bits are 1
#
#5. Python Logical Operators
# Python logical operators are used to compose Boolean expressions and evaluate their truth values.
# They are required for the creation of conditional statements as well as for managing the flow of execution in programs.
# Python has three basic logical operators: AND, OR, and NOT.
#Operator	        Description	                                                      Example
#and Logical AND	If both of the operands are true then the condition becomes true.	(a and b) is true.
#
# 6. Python Membership Operators
# Python membership operators are used to determine whether or not a certain value occurs within a sequence.
# They make it simple to determine the membership of elements in various
# Python data structures such as lists, tuples, sets, and strings.
# Python has two primary membership operators: the in and not in operators.
#Operator
#in
#Description
#Evaluates to true if it finds a variable in the specified sequence and false otherwise.
#example
#x in y, here in results in a 1 if x is a member of sequence y.
#
# 7. Python Identity Operators
# Python identity operators are used to compare two objects' memory addresses rather than their values.
# If the two objects refer to the same memory address, they evaluate to True; otherwise, they evaluate to False.
# Python includes two identity operators: the is and is not operators.
#Operator
#is
#Description
#Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
#example
#x is y, here are results in 1 if id(x) equals id(y)
#
#
#Python Logical Operators
#Logical operators are used to combine conditional statements:
#
#Operator	Description	                                                   Example
#and 	    Returns True if both statements are true.	                   x < 5 and  x < 10
#or	        Returns True if one of the statements is true.	               x < 5 or x < 4
#not	    Reverse the result, returns False if the result is true	not.   (x < 5 and x < 10)
# x = 5
# print(not(x < 5 and x < 10))