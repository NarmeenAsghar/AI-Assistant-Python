#---Table of 2
# for loop is used to print the table of 2
# range is used to print the table of 2 from 1 to 10
print("Table of 2")

for i in range(1,11):
    print(f"2 * {i} = {i * 2}")



#---for random number table
table = int(input("Enter the table number: "))

for i in range(1,11):
    print(f"{table} * {i} = {i * table}")