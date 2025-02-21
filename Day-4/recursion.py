#---------------------------------RECURSION:
'''
Recursion is a function that calls itself.
It is a powerful tool in programming that allows us to solve problems by breaking them down into smaller sub-problems
'''
# ----------factorial(4):
# factorial(4) calls factorial(3)
# factorial(3) calls factorial(2)
# factorial(2) calls factorial(1)
# factorial(1) returns 1 (base case)
# Unwinding:
# factorial(2) returns 2 * 1 = 2
# factorial(3) returns 3 * 2 = 6
# factorial(4) returns 4 * 6 = 24


#---Direct Recursion:
'''
Direct recursion occurs when a function calls itself directly. This is the most straightforward type of recursion
'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(4))
print(factorial(3))
print(factorial(5))
print(factorial(6))

#---Indirect Recursion:
'''
Indirect recursion occurs when a function calls another function, which in turn calls the first function
'''
def odd(n):
    if n == 0:
        return 0
    else:
        return even(n - 1)
    
def even(n):
    if n == 0:
        return 1
    else:
        return odd(n - 1)
    
print(odd(2))
print(even(4))


#---Tail Recursion:
'''
Tail recursion is a special case of recursion where the recursive call is the last operation in the function
'''

# The accumulator is a second argument (accumulator=1) in the function, which keeps track of the running product.

def tail_recursion(n, accumulator=1):
    if n == 1:
        return accumulator
    else:
        return tail_recursion(n - 1, n * accumulator)

print(tail_recursion(4))  
print(tail_recursion(3))
print(tail_recursion(5))  
print(tail_recursion(6))


#---Head Recursion:
'''
Head recursion is a type of recursion where the recursive call is the first operationn in the function
'''
def head_recursion(n):
    if n == 0:
        return 0
    else:
        return head_recursion(n -1)
    
print(head_recursion(4))
print(head_recursion(8))
print(head_recursion(6))
print(head_recursion(3))

#---printing in reverse order:
def print_reverse(lst):
    if len(lst) == 0:
        return
    print_reverse(lst[1:])
    print(lst[0]) 

print_reverse([1,2,3,4,5])


#---Tree Recursion(Fibonacci Sequence):
'''
Tree recursion is a type of recursion where a function calls itself multiple times with different parameters
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(5))
print(fibonacci(4))
print(fibonacci(3))
print(fibonacci(2))
print(fibonacci(1))


#---Mutual Recursion:
'''
Mutual recursion occurs when two functions call each other alternatively
'''

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

print(is_even(4))
print(is_odd(4))


#---Binary Search:
'''
Binary search is a more efficient search algorithm that works on sorted arrays
'''

def binary(arr, target):
    if len(arr) == 0:
        return False
    mid = len(arr) // 2
    if arr[mid] == target:
        return True
    elif arr[mid] < target:
        return binary(arr[mid + 1:], target)
    else:
        return binary(arr[:mid], target)
    
print(binary([1,2,3,4,5,6,7,8,9,10], 5))
print(binary([1,2,3,4,5,6,7,8,9,10], 11))


