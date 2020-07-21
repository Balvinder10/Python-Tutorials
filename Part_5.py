# EXCEPTIONS

# Try-Except Display

# try:
#     age = int(input("Age:"))
#     xfactor = 10/age
# except ValueError:  # ValueError Exception if user enters non-numeric value
#     print("You didn't enter a valid age")
# except ZeroDivisionError:
#     print("Age cannot be zero")
# else:
#     print("No exceptions were thrown") # Will only be executed if we dont have any exception

# print("Execution Continues")

# OR
# fromt timeit module importing timeit function to calculate the execution tim of python code
from timeit import timeit

try:
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):  # ValueError Exception if user enters non-numeric value
    print("You didn't enter a valid age")

else:
    # Will only be executed if we dont have any exception
    print("No exceptions were thrown")

print("Execution Continues")

# Finally Clause - Will always executed irrespective of exception or not

try:
    file = open("Part_5.py")  # Opening a file
    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):  # ValueError Exception if user enters non-numeric value
    print("You didn't enter a valid age")
else:
    # Will only be executed if we dont have any exception
    print("No exceptions were thrown")
finally:
    file.close()

print("Execution Continues")

# The With Statement

try:
    with open("Part_5.py") as file:  # Releasing eternal resources i.e. Part_5.py
        print("File Opened")
        # file.__exit__ Objects having __exit__ or __enter__ methods then such objects support context management protocols, with statement automatically calls exit method and hece there is no need for finally statement i.e closing external resources

    age = int(input("Age:"))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):  # ValueError Exception if user enters non-numeric value
    print("You didn't enter a valid age")

else:
    # Will only be executed if we dont have any exception
    print("No exceptions were thrown")

print("Execution Continues")

# RAISING

# Using 'raise' statement to raise the exception

# In Python we have various kind of in-built exception can be searched on google


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)  # Calling the function and passing value = -1
except ValueError as error:  # Except block of type Valueerror an exceptional object and giving it name - error
    print(error)


# Defining a variable, Code1 , which will calculate execution time of a piece of code within """......"""

code1 = """ 
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


try:
    calculate_xfactor(-1)  # Calling the function and passing value = -1
except ValueError as error:  # Except block of type Valueerror an exceptional object and giving it name - error
    print(error)
"""
print("Code1 executed 10000 times and its execution time is :", timeit(code1, number=10000)
      )  # Calling timeit function with Code1 as first argument and number of times it will be executed

code2 = """ 
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age


xfactor = calculate_xfactor(-1)  # Calling the function and passing value = -1
if xfactor == None:
    pass 
"""
print("Code2 executed 10000 times and its execution time is :", timeit(code2, number=10000)
      )


# -------------------------END-------------------------
