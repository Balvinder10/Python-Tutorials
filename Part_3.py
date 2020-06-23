# FUNCTIONS


def greet():  # def for definition and greet is the name of our fxn
    print("Hi there")
    print("Welcom aboard")


greet()  # Calling the fxn


def greeet(first_name, last_name):  # parameters of the fxn i.e input defined
    print(f"Hi {first_name} {last_name}")
    print("Welcom aboard")


greeet("Balinder", "Singh")  # Calling the fxn using arguments


# FUNCTIONS RETURNING A VALUE

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Balvinder Singh")
print("\n", message, "\n")

# Writing message to a file content.txt, w - open it for writing
file = open("content.txt", "w")  # Returns a file object
file.write(message)  # Calling messsage to write in content.txt


def increment(number, by):
    return number + by


print(increment(2, 1))


def multiply(*numbers):  # [] used to create list and () for tuples and teh difference is that tuples cannot be modified i,e no data can be added and are iterables and hence canbe used in loops
    # Prints a Tuple because of * in parameters
    print(f"\n Tuple generated is {numbers}")
    total = 1
    for number in numbers:
        print(number)
        total *= number
    return total


print(f" The Product is {multiply(2, 3, 4, 5)}\n")


# Function returning multiple 'Key-Value' pair


def save_user(**user):  # Double * indicates key-value pair
    # Together the output obtained is called DICTIONARY
    print(f"Gives DICTIONARY output: {user}")


save_user(id=1, name="Warren Peace", age=22)


# SCOPE : rEFERS TO THE REGION OF THE CODE WHERE A VARIABLE IS DEFINED

# VARIABLES DEFINED WITHIN A FUNCTION ARE CALLED LOCAL VARIABLES

# VARIABLES DEFINED WITHIN THE MAIN PROGRAM I.E. OUTSIDE ANY FXN ARE CALLED GLOBAL VARIABLES

# TO CHANGE GLOBAL VARIABLE WITHIN A FUNCTION USE 'global' KEYWORD FOLLOWED BY THE GLOBAL VARIABLE NAME

message = "a"


def greete(name):
    message = "b"


greete("Warren")
print(f"\n Global Variable prevails : {message}\n")


# DEFINING GLOBAL VARIABLE WITHIN THE FUNCTION


def greetee(name):
    global message
    message = "b"


greetee("Warren")
print(f" Global Variable Changed to : {message} Within A Function\n")

# TO TURN MUTIPLE LINES INTO COMMENT YOU CAN ALSO SELECT LINES AND THEN 'CTRL+/' TO TURN THEM INTO COMMENTS

# END PART 3
