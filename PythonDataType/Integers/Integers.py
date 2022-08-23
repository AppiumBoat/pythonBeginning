# Numbers can be divided into two parts Integers and Floating Point.
# Some Basic Arthimatic Operations like:
x = 15
y = 7
## Sum
print("Sum of x and y: ", x+y)
## Substraction
print("Substract of x and y: ", x-y)
## Multiplication
print("Multiplication of x and y: ", x*y)
## Division
print("Division of x and y: ", x/y)
## Modulo or Mod
print("Modulo of x and y: ", x%y)
## Power
print("Cude of 2: ", 2**3) # Cube of 2
print("Square of 5: ", 5**2) # Square of 5
## BODMAS-Bracket, Order, Division, Multiplication, Addition, and Subtraction
print("BODMAS ((2*3)*(3*3)+10): ", ((2*3)*(3*3)+10))

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
print("Dynamic typing example: ", my_numbers)
print("Variable data type: ", type(my_numbers))
my_numbers = 'Two'
print("Dynamic typing example: ", my_numbers)
print("Variable data type: ", type(my_numbers))

# Example:
my_salary = 25000
print("My Salary: ", my_salary)
my_tax = 0.2
print("Tax on Salary: ", my_tax)
my_onhand = my_salary * my_tax
print("Onhand Salary: ", my_onhand)
print("Variable data type: ",  type(my_onhand))