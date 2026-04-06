#2) Write a program to execute user defined exception in python.

class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise AgeError("You are not eligible!")
    
    print("You are eligible.")

except AgeError as e:
    print("Custom Exception:", e)

except ValueError:
    print("Invalid input! Please enter a number.")
