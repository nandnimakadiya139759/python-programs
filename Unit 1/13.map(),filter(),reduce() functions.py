#13.Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.

from functools import reduce

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Original List: {numbers}")
    print("-" * 30)

    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print(f"1. MAP (Squared):      {squared_numbers}")

    big_numbers = list(filter(lambda x: x > 5, numbers))
    print(f"2. FILTER (> 5):       {big_numbers}")

    total_sum = reduce(lambda acc, val: acc + val, numbers)
    print(f"3. REDUCE (Total Sum): {total_sum}")

if __name__ == "__main__":
    main()
