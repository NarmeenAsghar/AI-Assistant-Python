#------------------------------OPERATORS:
'''
operators are special symbols or keywords that are used to perform operations on variables and values.
'''

#---Arithmetic Operators:

a = 10
b = 3

print(a + b)
print(a - b) 
print(a * b) 
print(a / b) 
print(a // b)
print(a % b) 
print(a ** b) 


#---Comparison Operators:

X = 5
Y = 3

print(X == Y)  # Output: False
print(X != Y)  # Output: True
print(X > Y)   # Output: True
print(X < Y)   # Output: False
print(X >= Y)  # Output: True
print(X <= Y)  # Output: False


#---Logical Operators:

x = True
y = False

print(x and y)
print(x or y)
print(not x)   


#---Assignment Operators:

a = 5

#add
a += 3
print(a)

#subtract
a -= 2 
print(a) 

#multiply
a *= 1 
print(a)

#divide
a /= 5 
print(a)

#floor division
a //= 4 
print(a)

#modulus
a %= 3 
print(a)

#exponential
a **= 4 
print(a)


#---Identity Operators:
a = [1, 2, 3]
b = a

print(a is b) 

c = [1, 2, 3]
print(a is c)

print(a is not c) 


#---Membership Operators:
list = [1, 2, 3, 4]

print(3 in list)
print(5 not in list) 

