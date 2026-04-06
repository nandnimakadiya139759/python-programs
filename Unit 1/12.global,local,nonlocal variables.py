#12.Write a program to display the use of local, global and nonlocal variables

count = 10 

def outer_function():
    count = 20
    
    def inner_function():
        nonlocal count
        count = 30
        print(f"Inside inner_function (Nonlocal): {count}")

    print(f"Inside outer_function (Before call): {count}")
    inner_function()
    print(f"Inside outer_function (After call):  {count}")

print(f"Global Scope (Start):                {count}")
outer_function()
print(f"Global Scope (End):                  {count}")
