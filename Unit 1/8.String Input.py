#8. Write a Python program to perform following operation on given string input.__
#a) Count Number of Vowel in given string
#b) Count Length of string (donot use len() )
#c) Reverse string
#d) Find and replace operation
#e) check whether string entered is a palindrome or not

def count_vowels(text):
    """Counts the number of vowels in the string."""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

def string_length_manual(text):
    """Counts length without using len()."""
    count = 0
    for char in text:
        count += 1
    return count

def reverse_string(text):
    """Reverses the string."""

    return text[::-1] 

def find_and_replace(text, find_text, replace_text):
    """Finds a substring and replaces it with another."""
    return text.replace(find_text, replace_text)

def is_palindrome(text):
    """Checks if the string is a palindrome."""
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def main():
    print("--- String Operations Menu ---")
    input_str = input("Enter a string: ")

    # a) Count Vowels
    v_count = count_vowels(input_str)
    print(f"\na) Number of Vowels: {v_count}")

    # b) Count Length (without len())
    length = string_length_manual(input_str)
    print(f"b) Length of string: {length}")

    # c) Reverse String
    reversed_str = reverse_string(input_str)
    print(f"c) Reversed string: {reversed_str}")

    # d) Find and Replace
    print("d) Find and Replace Operation:")
    to_find = input("   Enter text to find: ")
    to_replace = input("   Enter text to replace it with: ")
    replaced_str = find_and_replace(input_str, to_find, to_replace)
    print(f"   Result: {replaced_str}")

    # e) Palindrome Check
    is_pal = is_palindrome(input_str)
    status = "is" if is_pal else "is not"
    print(f"e) The string '{input_str}' {status} a palindrome.")

if __name__ == "__main__":
    main()
