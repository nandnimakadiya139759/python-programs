#10.Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.

def main():

    add = lambda x, y: x + y
    sub = lambda x, y: x - y
    mul = lambda x, y: x * y
    div = lambda x, y: x / y if y != 0 else "Error: Division by Zero"

    operations = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator in operations:
            result = operations[operator](n1, n2)
            print(f"Result: {result}")
        else:
            print("Invalid Operator selected.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()
