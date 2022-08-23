# Numbers can be divided into two parts Integers and Floating Point.
# Some Basic Arthimatic Operations like:
x = 15
y = 7
## Sum
print(x+y)
## Substraction
print(x-y)
## Multiplication
print(x*y)
## Division
print(x/y)
## Modulo or Mod
print(x%y)
## Power
print(2**3) # Cube of 2
print(5**2) # Square of 5
## BODMAS-Bracket, Order, Division, Multiplication, Addition, and Subtraction
print((2*3)*(3*3)+10)

# Rules for Variable Assignment
#	Names can not start with a numbers
#	No Space
#	Can't use symbols(most IDE throws error)
#	Lowercase
#	Avoid identifier like 'list' and 'str' which are part of python key words

# Python uses dynamic typing
# Unlike other languages where int variables cann't be assigned with str or any other data types
# Python have dynamic assignment which mean a variable can hold number and later can be assigned with str
# This have its own disadvantages as changing datatype wont throw error, therefore, one has
# to be careful while assigning values to variables.
my_numbers = 2
print(my_numbers)
my_numbers = 'Two'
print(my_numbers)

# To check type of variables
print(type(my_numbers))

# Example:
my_salary = 25000
my_tax = 0.2
my_onhand = my_salary * my_tax
print(my_onhand)
print(type(my_onhand))