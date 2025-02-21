#----------------------------DICTIONARY:
'''
A dictionary in python  is a key-value pair data structure that is unordered, mutable and indexed
'''

data = {
    'name': 'David',
    'age': 24,
    'contact-_no': 345652345,
    'address': '01 flat, abc street, xyz pakistan'
}
print(data)
print(f"My name:", data['name'])
print(data['age'])
print(data['contact-_no'])
print(data['address'])
print(f"The name of our first student is '{data['name']}'")

#---updating
data['age'] = 26
print(data)

#---loop
for key,value in data.items():
    print(f"{key} : {value}")


#---nested dictionary
Student_1 = {'Name': 'Ali', 'Total_marks': 250}
Student_2 = {'Name': 'Wasif', 'Total_marks': 230}
Student_3 = {'Name': 'Zubair', 'Total_marks': 244}
Student_4 = {'Name': 'Haider', 'Total_marks': 235}

Students = [Student_1, Student_2, Student_3, Student_4]

for student in Students:
    print(student)


#---list in dictionary
pizza = {'crust': 'thick',
         'toppings': ['mushrooms', 'extra-cheese']
         }

print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(topping)