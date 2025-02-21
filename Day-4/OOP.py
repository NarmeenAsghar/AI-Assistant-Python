#------------------------OBJECT ORIENTED PROGRAMMING (OOP):
'''
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around objects 
and data, rather than functions and logic. Python supports OOP, and the core concepts which define below
'''

#---Class:
'''
A class is a blueprint or template for creating object
'''

#---Object:
'''
An object is an instance of a class. It is created from a class and contains its data and behavior
'''

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

car1 = Car("Toyota", "Corolla", 2024)
print(car1.make)
print(car1.model)
print(car1.year)                        


#---Encapsulation:
'''
Encapsulation is the practice of restricting access to the internal details of an object
'''

class Bank_account:
    def __init__(self, balance):
        self.__balance = balance 

    def deposit(self, amount):
        self.__balance += amount 

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount 
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account = Bank_account(1000)


account.deposit(int(input("Enter the amount to deposit: ")))
print(account.get_balance())

account.withdraw(int(input("Enter the amount to withdraw: ")))
print(account.get_balance())


#---Inheritance:
'''
Inheritance is a mechanism that allows a class to inherit attributes and methods from another class
'''

class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal): 
    def speak(self):
        print("Woof")

dog = Dog()
dog.speak() 


#---Polymorphism:
'''
Polymorphism is the ability of objects to take on multiple forms or behaviors
'''

class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

animals = [Cat(), Dog()]
for animal in animals:
    animal.speak() 


#---Abstraction:
'''
Abstraction is the practice of hiding the implementation details of an object and showing only the essential features
'''

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
print(circle.area())


#---Magic Methods:
'''
Magic methods are special methods in python that are used to define the behavior of objects
'''

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old."

person = Person("Alice", 30)
print(person) 
