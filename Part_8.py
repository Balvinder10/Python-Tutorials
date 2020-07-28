# PYTHON LIBRARIES

# WORKING WITH FILES, DIRECTORIES AND PATHS

# --------------PATHS---------------

# PATH CLASS -  FOUNDATION TO WORK WITH FILES AND DIRECTORIES


import subprocess  # Module help in running other programs
from string import Template
from email.mime.image import MIMEImage  # Attaching Image to the mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import webbrowser
import string
import random
from datetime import datetime
from datetime import datetime, timedelta
# Module which gives date-time objecy with attributes like year , month and so on
import datetime
import time  # TIme module gives time stamp
import sqlite3
import json
import csv
from zipfile import ZipFile  # Importing ZipFile Class
import shutil
from time import ctime
from pathlib import Path  # Path-Class

# Creating Path Object

Path(r"C:\Python\TestPath")  # r-raw string
path = Path("Ecommerce/__init__.py")
Path() / "Ecommerce" / "__init__.py"  # Another method

Path.home()  # Returns home directory of Current User

path.exists()  # To check whether path exist or not
path.is_file()  # To check whether the path object represents file or not
path.is_dir()  # To check whether the path object represents directory or not

print(path.name)  # Returns the name of file in path
print(path.stem)  # Returns the name of file without extension in path
print(path.suffix)  # Returns the extension of file in path
print(path.parent)  # Returns the parent folder of the file in path

# TO create a new path object based on existing path but only change name and extension of the file
path.with_name("file.txt")
print(path)

print(path.absolute())  # To get absolute value of the path

# To change the extension of the existing file represented by the path - WE HAVE NOT CHANGED THE FILE NAME/EXTENSION , WE ARE ONLY REPRESENTING A PATH OBJECT
path.with_suffix(".txt")
print(path)

# -----------------DIRECTORIES-----------------

path = Path("Ecommerce")  # path object representing a directory

# path.exists()
# path.mkdir() # To create a dir
# path.rmdir() # To remove a dir
# path.rename("Ecommerce2") # TO rename a dir

# Get the list of files/dir in the path object - GIVES A GENERATOR OBJECT, RETURNS A NEW VALUE EVERY TIME WE ITERATE IT
print(path.iterdir())

for p in path.iterdir():
    print(p)

# Can be done above operation using list comprehension

# paths = [p for p in path.iterdir() if p.is_dir()] to filter only dir
paths = [p for p in path.iterdir()]
print(paths)

# path.glob("*.xyz") , method takes a pattern for search and returns a generator

py_files = [p for p in path.glob("*.py")]  # To searh recursively "**/*.xyz"
# py_files = [p for p in path.glob("**/*.py")] # To searh recursively "**/*.xyz"

print(py_files)

# path.rglob("*.xyz") - To search recursively

py_files1 = [p for p in path.rglob("*.py")]
print(py_files1)

# -----------------FILES------------------

path1 = Path("Ecommerce/__init__.py")

# path1.exists()
# path.rename("__init__.txt")
# path.unlink() # To delete

print("\n", path1.stat())  # Returns infomation aboout the file

# from time import ctime - To read human readable time as shown in stat()

print("\n",  ctime(path1.stat().st_ctime))  # Gives creation time of a file

# Returns the content of file as a bytes object representing binary data
print(path1.read_bytes(), "\n")

print(path1.read_text())  # Returns content of the file as a string

# File can also be opened using inbuilt open()

# name of the file, open in read "r" mode. SINCE IT GIVES FILE OBJECT THEN IT MUST BE CLOSED THEREFORE WE USE WITH STATEMENT WHICH AUTOMATICALLY CLOSES THE FILE AT THE END OF EXECUTION
file1 = open("__init__.py", "r")

with open("__init__.py", "r") as file:
    pass

# WHEREAS PRINT(PATH.READ_TEXT()) THERE IS NO PROBLEM OF CLOSING THE FILE AND HENCE IS PREFERRED

path1.write_text("Writing some textual data to file")
path1.write_bytes(" 001 ")


# COPYING A FILE

# PATH OBJECT IS NOT IDEAL FOR COPYING A FILE

source = Path("Ecommerce/__init__.py")
target = Path() / "__init__.py"  # i.e current dir + __init__.py

source.read_text()  # STEP 1: Reading content of the source file

# STEP 2: Writing Into the target (There is no need for step1)
target.write_text(source.read_text())

# ANOTHER BETTER WAY TO COPY


# import shutil is a shell_utilities module , provide high level operations for copying and moving files/directories

shutil.copy(source, target)


# -----------------ZIP FILES--------------

# from zipfile import ZipFile # Importing ZipFile Class

# Creating zip file object - files.zip in the current directory
zip = ZipFile("files.zip", "w")

# Path("Ecommerce").rglob("*.*") # Getting all the files in Ecommerce directory and writing it into files.zip and rglob to recursively find all the filesin the dir - REturns Generator object and can beiterate over

for path in Path("Ecommerce").rglob("*.*"):
    zip.write(path)
zip.close()

# OR

# with ZipFile("files.zip", "w") as zip:
#     for path in Path("Ecommerce").rglob("*.*"):
#         zip.write(path)  - No need to call close method

# OPENING A ZIP IN READ MODE

with ZipFile("files.zip") as zip:
    print(zip.namelist())  # Which returns list of all the files in the zip file
    # Return info object and give information about __Init__.py
    info = zip.getinfo("Ecommerce/__init__.py")
    print(info.file_size)
    print(info.compress_size)
    # Extracting all the files from zip file and storing into Extract/different directory as mentioned within "" , within same directory
    zip.extractall("Extract")


# ---------------CSV FILES---------------

# import csv - Module

# file = open("data.csv", "w") # Opening afile in write mode and returns file onject
# file.close()

with open("data.csv", "w") as file:  # No need to separately close a file
    # First parameter is file_object and returns writer object which helps in writing tabular data
    writer = csv.writer(file)
    # Passing first row as a header
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 15])

# READING A CSV FILE

with open("data.csv") as file:
    reader = csv.reader(file)
    # Calling list function to convert all the data in a csv file into list objetc and the list object is iterable
    print(list(reader))
    # The reader object has index positioned at the begining of the file and when we convert reader object into list that index position goes at the end of file
    # SO WHEN WE ITERATE OVER THE LIST OBJECT, OBTAINED FROM READER OBJECT, WE ARE ALREADY AT THE END OF IFLE AND BELOW CODE WILL NOT SHOW OP AND HENCE TO SOLVE THIS PROBLEM WE HAVE TO COMMENT OUT - "print(list(reader))" i.e DO NOT CONVERT READER INTO LIST IN ORDER TO OBTAIN ROWS OP
    # WHERE EACH ROW IS AN ARRAY OF STRINGS
    for row in reader:
        print(row)  # Prints list of rows


# -------------------JSON FILES----------------

# import json - To import json module

# Array of movies object, and each item in this array is dictionary i.e each item in movies is a collection of K-V pair

movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 2, "title": "Terminator 2 ", "year": 1993},
]

data = json.dumps(movies)  # get a string of movies data formatted as json
print(data)

# Writing data variable into a file

# Passing the data to be written into movies.json
Path("movies.json").write_text(data)

# READING FROM JSON

# data is a string formatted as a json
data = Path("movies.json").read_text(data)  # import Pathlib

movies_read = json.loads(data)  # Parssing the data into array of dictionaries
print(movies_read)
print(movies_read[0])
print(movies_read[0]["title"])


# ----------------SQLITE FILES-----------------------


# import sqlite3
# import json
# from pathlib import Path

# Creating Path object to load movies.json and read all of its which rutrns a string and pass that string to json.loads to parse which will give list of movies
movies = json.loads(Path("movies.json").read_text())
print(movies)  # Gives list of dictionaries

# Method 'connect' and pass the name of database and if the file with that name does not exist in the directory then it will cretae for us. This will return a connection object
connection = sqlite3.connect("db.sqlite3")

# Similar to file object connection object must also be closed when done with it

with sqlite3.connect("db.sqlite3") as conn:
    # Assumoing we have table called Movies, where ? are placeholders for the values we are going to supply.3? -> 3 Columns i.e id, title and year
    # This command is instruction we sent to database for creating, deleting and updating data
    command = "INSERT INTO Movies VALUES(?, ?, ?)"

    # Iterating over movies list
    for movie in movies:
        conn.execute(command, tuple(movie.values()))  # execute method toexecute command and first argument is command and second argument is actual value. Each movie object is K-V pair i.e dictionary in a loop. Second argument - Actual vaues and getting value of each movie(a K-v pair from movies dictionary) object in a loop and put those values into a tuple using inbuilt tuple

    conn.commit()  # Onlyt need to write data in db. Commit method to write changes into a database - on running code upto this point will show operational error : no such Table :Movies - Because we are dealinng with empty database which does not have Movies table. So we have to create a Movies database using DB Browser to create a Movies Table by loading db.sqlite3 and creating a Table Movies

# READING FROM SQLITE DATABASE

with sqlite3.connect("db.sqlite3") as conn:
    # These command statements are similar to SQL commands
    command = "SELECT * FROM MOVIES"
    cursor = conn.execute(command)  # Will return a iterable object
    for row in cursor:  # gets one row at atime
        print(row)  # GIves tuple of the values for row in databse

    # WIll retuurn all the rows in database in one go and will reutn a list of tuples
    movies_list = cursor.fetchall()
    print(movies_list)  # Must comment out for command i.e line 253,254 because after execution the cursor will be at the end of db and hence fetchall will not show in any result


# ----------------TIMESTAMPS---------------


# import time # TIme module gives time stamp

# import datetime # Module which gives date-time objecy with attributes like year , month and so on

print(time.time())  # time method return current time as a floating point number as seconds from the begining of point i.e. operating system ex : In UNIX it is Jan 1 ,1970


def send_emails():  # A function to Simulate sending emails to 10000 recepients
    for i in range(10000):
        pass


start = time.time()  # TO store current time
send_emails()
end = time.time()  # Tostore ending time of the execution of simulation

duration = end - start  # Gives amount of time in seconds for the duration of executoin
print(duration)


# WORKING WITH DATe TIME OBJECTS

# import datetime

dt = datetime.datetime(2020, 7, 26)  # YYYY-MM-DD


# from datetime import datetime


dt1 = datetime(2020, 7, 26)

dt2 = datetime.now()  # now method to find datetime class that returns cureent date-time

# %Y - 4 digit year, %m - 2 digit month, %d - 2 digit date

# For parsing or converting a datetime string into readable format for python, especially useful when you are either taking date as an input from auser or importing from a file - WHICH PART IS YEAR, MONTH, DATE
dt3 = datetime.strptime("2018/01/01", "%Y/%m/%d")

# CONVERTING TIME STAMP INTO DATE TIME OBJECT

# Will return current date-time object for the timestamp
dt4 = datetime.fromtimestamp(time.time())

print(f"{dt4.year}/{dt4.month}")

# Is opposite of strptime - we convert a datetime object into a string
dt4.strftime("%Y/%m")

print(dt2 > dt1)


# from datetime import datetime, timedelta - timedelta module represents duration

duration = dt2 - dt1  # Returns timedelta object
print(duration)
print("Days", duration.days)
print("Seconds", duration.seconds)

# Methods ends with() i.e xyz.method() whereas attributes don't i.e xyz.attribute

print("Total duration represented as Seconds", duration.total_seconds())

dt5 = dt1 + timedelta(days=1, seconds=1000)
print(dt5)


# ----------GENERATING RANDOM VALUES------------

# import  random

# import string - has interesting attributes

print(random.random())  # Random module- generates random floating point
print(random.randint(1, 10))  # Generates random int between 1 and 10
# From a give array(choice) draws random number
print(random.choice([1, 2, 3, 4]))
# Selects multiple values from array, For k(key) value 'n' generates n pair of random no
print(random.choices([1, 2, 3, 4], k=2))
# Generates 4 random items from astring
print(random.choices("abcdefghi", k=4))
# joins 4 random characters as a string. Helps in generating random password
print("".join(random.choices("abcdefghi", k=4)))
# sepeerates each character by ',' or joins them using ','
print(",".join(random.choices("abcdefghi", k=4)))

# USING STRING MODULE

# Returns string of all the lower and upper case alphabets
print(string.ascii_letters)
print(string.digits)  # Returns digits

# Generates Random combination - Password Generation
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# SHUFFLING OF NUMBERS

numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)


# ----------OPENING THE BROWSER----------

# Useful in automation of script

# import webbrowser

print("Deployment Completed")

# OPENING URL OF THE TARGETTED WEBSITE
webbrowser.open("https://www.google.com")

# ------------SENDING EMAILS-----------------

# Particularly useful when you have database of the customers and send them emails based on their interest

# from email.mime.multipart import MIMEMultipart - Email package with mime(Multipurpose Internet Mail Extension) as subpackage - a standard which defines the format of the emails. MIMEMultipart - Class - cansend the email both as HTML ans palin text content
message = MIMEMultipart()

# Various headers supported by MIME - from, to, subject but we don't have header for the body of email

message["from"] = "Balvinder Singh"
message["to"] = "balvinders9@gmail.com"
message["subject"] = "This is a test"

# Creating body header for the email

# from email.mime.text import MIMEText - For the payload in the attach method
# from email.mime.image import MIMEImage # Attaching Image to the mail
# Plain text content
message.attach(MIMEText("This is the Body of the Email", "plain"))
# Need to pass image object in binary - must import pathlib to use PAth class. Assuming there is test.png in the current working directory
message.attach(MIMEImage(Path("test.png").read_bytes))
# Sending the mail using SMTP Server

# import smtplib - SMTP Server

# smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)  # Returns SMTP object
# smtp.close()

# OR
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()  # Hello method to initialise SMTP Server - SMTP Protocol
    smtp.starttls()  # starttls - puts SMTP connection into 'tls'(transport layer security) mode - For encryption
    # Senders lagin id and password
    smtp.login("acestriker0010@gmail.com", "9403775311")
    smtp.send_message(message)  # Passing the message object
    print("Sent...")


# ---------HTML TEMPLATE(MAIL)----------------

# from string import Template - Using the Template class to replace $name, parameter in template.html with a string

template = Template(Path("template.html").read_text())
template.substitute()  # Willreplace the parameeter dynamically

message = MIMEMultipart()

message["from"] = "Balvinder Singh"
message["to"] = "balvinders9@gmail.com"
message["subject"] = "This is a test"

# PAssing a dictionarie s of all the values to be dynamically substitute in the template.html
body = template.substitute({"name": "john"})


message.attach(MIMEText(body, "html"))  # HTML text content
message.attach(MIMEImage(Path("test.png").read_bytes))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("acestriker0010@gmail.com", "9403775311")
    smtp.send_message(message)
    print("Sent...")


# ------RUNNING EXTERNAL PROGRAMS FROM PYTHON SCRIPT-------


completed = subprocess.run(["ls", "-l"])  # Running command ls with argument -l
completed.args  # Array includes the command executed
completed.returncode  # 0 implies success
completed.stderr  # None - No Error
completed.stdout  # None - Output is not capture(Saved)

# OP Will not be printed in the terminal
completed = subprocess.run(["ls", "-l"], capture_output=True)
print("stdout", completed.stdout)  # OP will be available in stdout attribute


# CALLING OTHER PYTHON SCRIPT

# Both the script - PArt_8.py and other.py will be in different space and processes and will not be sharing variables
completed1 = subprocess.run(
    ["python", "other.py"], capture_output=True, text=True)
print(completed1.returncode)


# ----------------------END----------------------------------
