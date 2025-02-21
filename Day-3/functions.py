#--------------------------------FUNCTIONS:
'''
Functions are defined using the def keyword.
They can take parameters and can return values.
'''

#---Basic
def greet(name):
    print(f"Hello {name}! How are you?")

greet("Ahmed")

#---Multiple parameters and also return statement
def data(name, age, country):
    return f"The person who applied for this job is {name}, {age} years old, and is from {country}"
print(data("Ali", 26, "Pakistan"))
print(data("Hammad", 30, "India"))
print(data("Zahid", 28, "Greece"))
print(data("Laraib", 32, "Turkey"))

#---Default parameter
def greet(name = "David"):
    print(f"Hello {name}! What's going on?")

greet()
greet("Warner")
greet("William")

#---Variable-Length Arguments (Arbitrary Arguments)

#---args
'''
Allows you to pass a variable number of non-keyword arguments (tuple)
'''

def addition(*args):
    return sum(args)

print(addition(23, 45, 36, 54, 21))
print(addition(1, 2, 3,4 , 5, 6, 7))
print(addition(23.7, 87.2, 21.3, 33.2))

#---kwargs
'''
Allows you to pass a variable number of keyword arguments (dictionary)
'''

def data(**kwargs):
    # return kwargs
    for key, value in kwargs.items():
        print(f"{key} : {value}")

print(data(name = "David", roll_no = 1, total_marks = 87))
print(data(name = "John", roll_no = 2, total_marks = 82))
print(data(name = "Mili", roll_no = 3, total_marks = 79))

#---Variable number of arguments
'''
Allows you to pass a variable number of arguments to a function
'''
def greet(*names):
    for name in names:
        print(f"Hello {name}")

greet("Ali","Jawwad", "Wasif")

#---Lambda 
'''
A small anonymous function that can have any number of arguments, but can only have one expression
'''
def square(num):
    return num * num

square = lambda num : num * num
print(square(5))

#---Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))
#---add
add = lambda a, b ,c: a + b + c
print(add(2, 3, 5))
#---map
numbers = [(1, 4), (2, 5), (5, 6)]
result = list(map(lambda x:x[0] + x[1], numbers))
print(result)                                                                                               
#---filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
#---reduce
'''
Applies a function to each element of the list and return a single value     
'''
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum =  reduce(lambda x, y: x + y, numbers)
print(sum)


#---Global and local scope
'''
Variables declared outside of all functions are global scope variables
Variables declared inside a function are local to that function
'''
x = 14 # global

def function():
    x = 10 # local
    print(x)

function()
print(x)

