#------------------------------LOOPS:
'''
loops are used to repeat a block of code multiple times.

'''

#---For loop:

word = "Python"
for letter in word:
    print(letter)


#---While loop:

count = 1
while count <= 5:
    print(count)
    count += 1 


#break
count = 2
while count <= 10:
    if count == 5:
        break  # Exit the loop when count is 5
    print(count)
    count += 1

#continue
count = 0
while count <= 10:
    if count == 5:
        count += 1  # Increment before continue to avoid infinite loop
        continue  # Skip the iteration when count is 5
    print(count)
    count += 1


#---else with for loop:

#Checking if number is prime
num = 13
#assuming that the number is prime
is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
else:
    if is_prime:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
