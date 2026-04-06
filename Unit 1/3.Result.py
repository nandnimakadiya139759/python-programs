# 3.Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

m1 = int(input("Enter 1st Subject Mark:"))
m2 = int(input("Enter 2nd Subject Mark:"))
m3 = int(input("Enter 3rd Subject Mark:"))
m4 = int(input("Enter 4th Subject Mark:"))
Total = m1+m2+m3+m4
Per = float((m1+m2+m3+m4)/4)

if Per >= 80:
    result = "O"
elif Per >= 70:
    result = "A+"
elif Per >= 60:
    result = "A"
elif Per >= 45:
    result = "Pass"
elif Per >= 35:
    result = "Fail"

print("Total Marks:",Total)
print("Your Total Percentage is:", Per)
print("Your Grade is:", result)
