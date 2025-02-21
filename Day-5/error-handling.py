#-----------------------ERROR HANDLING:
'''
Error handling is a mechanism that allows you to handle errors in your code and continue the execution of the program
'''

try:
   
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Please enter valid integers.")

else:
    print(f"The result is {result}")

finally:
    print("Execution completed.")


#---Custom Exceptions:
'''
Custom exceptions are exceptions that are defined by the user
'''

class InsufficientFundsError(Exception):
    def __init__(self, message="Insufficient funds in your account"):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Attempted to withdraw {amount}, but only {self.balance} is available.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance: {self.balance}")
        
try:
    account = BankAccount(1000)
    account.withdraw(1500) 
except InsufficientFundsError as e:
    print(f"Error: {e}")  

    