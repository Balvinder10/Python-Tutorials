# COMPARISON OPERATORS GENERALLY BOOLEAN OPERATIONS
# <,>,==,!=,<=,>=
# ord("character") gives the numeric representation of the character

print(ord("b"))
print(ord("B"))

# CONDITIONAL STATEMENTS

# IF STATEMENT

# IF STATEMENT ALWAYS ENDS WITH : OPERATOR AND RESULT IS ALWAYS BOOLEAN
# INDENTATION DEFINES THE CODE TO BE EXECUTED UNDER THE CONDITION AND THE PYTHON AUTOMATICALLY DOES IT
# ENDING OR REMOVING INDENTATION ENDS THE CONDITIONAL STATEMENT

temp = 35
if temp > 30:
    print("It's Warm")
    print("Drink Water")
print("Done\n\n")

# ELIF STATEMENT FOR MULTIPLE CONDITIONS

temp = 15
if temp > 30:
    print("It's Warm")
    print("Drink Water")
elif temp > 20:
    print("It's Nice")
else:
    print("It's Cold")
print("Done\n\n")

# Program to check person is eligible or not
age = 22
if age >= 18:
    message = "Eligible"
else:
    message = "Not Eligible"
print(message)

# USING TERNARY OPERATOR TO REWRITE THE SAME CODE
print("\n\n")

age = 22
message = "Eligible" if age >= 18 else "Not Eligible"
print("Eligible\n\n")

# LOGICAL OPERATORS - AND,OR,NOT
# AND OPERATOR BOTH CONDITIONS MUST BE TRUE OR FALSE
# OR OPERATOR EITHER OF THE CONDITION TRUE GIVES THE RESULT i.e ATLEAST ONE OF THE CONDITION MUST BE TRUE

high_income = False  # variable is boolean
good_credit = True   # variable is boolean

if high_income and good_credit:
    print("Eligible")
else:
    print("Not Eligible\n")

high_income = False  # variable is boolean
good_credit = True   # variable is boolean

if high_income or good_credit:  # No need to write high_income=="True" as the variable itself boolean
    print("Eligible\n\n")
else:
    print("Not Eligible\n\n")

# NOT OPERATOR

high_income = True  # variable is boolean
good_credit = True  # variable is boolean
student = True      # variable is boolean

if not student:  # not true and hence condition will become false
    print("Eligible")  # Executed only if true
else:
    print("Not Eligible\n\n")  # Executed only if false

student = False

if (high_income or good_credit) and not student:
    print("Eligible\n\n")
else:
    print("Not Eligible")

# BOOLEAN OPERATORS ARE SHORT CIRCUIT

# THE EVALUTAION OR EXECUTION STOPS THE MOMENT PYTHONN COME ACROSS FALSE IN THE CONDITIONAL STATEMENT NO MATTER WHAT IS WRITTEN AFTER THAT

# SIMILARLY IN OR STATEMENT THE EXECUTION STOPS THE MOMNET PYTHON COME ACROSS TRUE NO MATTER WHAT IS WRITTEN AFTER THAT IN A CONDITIONAL STATEMENT

# HENCE IN PYTHON LOGICAL OPERATORS ARE SHORT CIRCUIT

# CHAINING COMPARISON OPERATORS

age = 22
# if age>=18 and age<65 can be re-written as
if 18 <= age < 65:
    print("\nEligible Using Chain Comparison\n")


# FOR LOOPS

# Range is fxn starts with 0 no of times and number is any variable(int)
for number in range(3):
    print("First Attemp Using for Loop-", number+1, (number+1) * ".")

print("\n\n")

# Here we are starting with 1 upto 10 but with step or gap of 2
for number in range(1, 10, 2):
    print("Second Attempt Using For Loop-", number, number * ".")


print("\n\n")

# FOR ELSE

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break  # To break out of the loop

print("\n\n")

successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break  # To break out of the loop
else:  # Will be executed only if loop never executes break
    print("Attempted 3 times and failed")

print("\n\n")

# NESTED LOOPS

for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

print("\n\n")

# ITERABLES

# Range fxn returns an object of range type i.e a complex type
print(type(range(5)), "\n\n")

# Range types are iterables
# STRINGS ARE ALSO ITERABLES

for x in "Python":  # IN EACH ITERATION X WILL HOLD ONE CHARACTER
    print(x)

print("\n")
#  ANOTHER COMPLEX TYPE CALLED LIST AND USES [] OPERATOR
# List to store list of numbers,strings etc

for x in [1, 2, 3, 4]:
    print(x)

print("\n")

# WHILE LOOP
# TO ITERATE AS LONG AS CONDITION IS TRUE

number = 100
while number > 0:
    print(number)
    # INTEGER DIVISION (//) ,NO DECIMAL POINT, number // = 2 (Augmented Operator)
    number = number // 2

# CTRL + D force termination of while loop
print("\n")

command = ""  # Empty string
while command != "quit":  # PYHTON IS CASE SENSITIVE
    command = input(">")  # INPUT FXN TAKES INPUT IN THE STRING TYPE ALWAYS
    print("ECHO", command)  # USE TERMINAL TO GET INPUT

# USE CTRL+BACKTICK(`) TO OPEN TERMINAL
#  INORDER TO AVOID ERROR DUE TO CASE SENSITIVITY
print("\n")

command = ""
while command.lower() != "quit":  # .lower() will automatically converts input into lower case
    command = input(">")
    print("ALPHA", command)  # USE TERMINAL TO GET INPUT

# IF YOU ARE WORKING WITH INFINITE LOOPS LIKE while True: , there has to be way out i.e break statement from the loop otherwise at som point program will run out of memory and will crash

# COUNTING EVEN NUMBERS FROM 1 TO 10

print("\n\n")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")

# END OF PART 2
