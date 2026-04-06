#11.Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.

def calculate_total(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

result1 = calculate_total(10, 20, 30)
print(f"Total of 10, 20, 30 is: {result1}")

result2 = calculate_total(5, 5, 5, 5, 5)
print(f"Total of five 5s is: {result2}")

result3 = calculate_total(1.5, 2.5, 4.0)
print(f"Total of 1.5, 2.5, 4.0 is: {result3}")
