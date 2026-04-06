# 4. Write a program to enter 10 numbers and display all armstrong numbers from those numbers.


print("Enter 10 numbers:")
armstrong_numbers = []

for i in range(10):
    num = int(input())
    temp = num
    digits = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** digits)
        temp = temp // 10

    if sum == num:
        armstrong_numbers.append(num)
        
print("Armstrong number is:", armstrong_numbers)
