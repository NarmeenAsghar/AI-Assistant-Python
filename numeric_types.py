#------------------------------NUMERIC TYPES:
'''
Numeric Types represent numbers, and they allow you to perform mathematical operations
1. Integer
2. Float
3. Complex
'''

#---Integer:
'''Integer type, used to represent whole numbers'''

x = 42
y = 78
print( x + y)
print( x - y)
print( x / y)
print( x * y) 
print(type(x))

print( 3 ** 3)
print(4 + 8 * 7)
print((4 - 2) + 10)


#---Float:
'''Floating-point number type, used for decimal or real numbers'''

print(3.45 + 54.8)
print(-0.25 + 1.25)
print(2.4 * (1.2 / 1.5))

#---Interger with float
print(4 - 2.4)
print(10.5 + 5)


#---Complex Numbers:
'''
A complex number has two parts: a real part and an imaginary part.
Complex numbers are represented as a + bj, where a is the real part, and b is the imaginary part. 
In Python, the imaginary part is represented using a lowercase j
'''

x = 2 + 2j
y = 4 + 8j
print( x + y )
print( x - y )
print( x / y )
print( x * y )

x = 10
y = float(x)
z = complex(x)
