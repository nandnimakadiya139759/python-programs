# 2. Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input"

num1=float(input('Enter 1st Number: '))
num2=float(input('Enter 2nd Number: '))
op = input("Enter Operator (+, -, *, /,): ")

if op == "+":
    res = num1 + num2
elif op == "-":
    res = num1 - num2
elif op == "*":
    res = num1 * num2
elif op == "/":
    res = num1 / num2
else:
    print("Invalid Operator");

print("Result is:", res)
