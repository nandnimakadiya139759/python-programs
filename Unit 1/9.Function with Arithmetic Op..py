#9. Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.

def perform_operation(num1, num2, operator):
    """
    Accepts two numbers and an operator (+, -, *, /, %, **)
    and returns the calculated result.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 == 0:
            return "Error: Cannot divide by zero."
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Invalid Operator"

def main():
    try:
        number1 = float(input("Enter first number: "))
        number2 = float(input("Enter second number: "))
        op = input("Enter operator (+, -, *, /, %, **): ")

        result = perform_operation(number1, number2, op)

        print(f"Result: {result}")

    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
