#5) Write a program to read a file and display its contents. At the end it shall also display no. of words available in file.

def process_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            
            print("--- File Contents ---")
            print(content)
            print("----------------------")
            words = content.split()
            total_words = len(words)
            
            print("Total number of words in the file: {}".format(total_words))
            
    except FileNotFoundError:
        print("Error: The file '" + filename + "' was not found.")
    except Exception as e:
        print("An error occurred: " + str(e))

process_file("data.txt")
