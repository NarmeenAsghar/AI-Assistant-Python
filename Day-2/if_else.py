#-------------------------IF, ELIF, ELSE STATEMENTS:
'''
if, elif, and else are used for conditional statements to control the flow of execution based on certain conditions
'''
#---if
'''
Used to check if a condition is True. If it is, the code inside the if block will execute
'''
#---elif
'''
Short for "else if", it allows you to check multiple conditions if the previous ones are False. You can have multiple elif blocks
'''
#---else
'''
Used to define what should happen if none of the previous conditions are True. There can only be one else block at the end
'''

#--Marksheet of student
print ("Marksheet of Student 1")

name = input("Student Name: ")
roll_no = input("Roll no: ")
math = int(input("Enter Maths Marks: "))
english = int(input("Enter English Marks: "))
urdu = int(input("Enter Urdu Marks: "))
islamiat = int(input("Enter Islamiat Marks: "))
computer = int(input("Enter Computer Marks: "))
science = int(input("Enter Science Marks: "))

Total = math + english + urdu + islamiat + computer + science
print("Total Marks: ", Total)

percentage = (Total / 600) * 100
print("Percentage: ", percentage)

#---using if, elif, else statement
if percentage >= 90:
    print("Grade : A+")
elif percentage >= 80:
    print("Grade : A")
elif percentage >= 70:
    print("Grade : B")
elif percentage >= 60:
    print("Grade : C")
elif percentage >= 50:
    print("Grade : D")
else:
    print("Failed")
    print("Work Hard! Be successful next time")