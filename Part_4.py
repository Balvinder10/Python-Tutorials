# DATA TYPE

# LIST

from pprint import pprint
from sys import getsizeof
from array import array  # Imported to array module later
from collections import deque  # Importing 'deque' module
letters = ["a", "b", "c"]  # List of letters

# List of Lsits

# We have list in which each item is a list itself and hence gives rise to matrix

matrix = [[0, 1], [2, 3]]
print(matrix, "\n")

zeros = [0]*100  # List of 100 zeroes

combined = zeros + letters  # Concatenation of lists

# CREATING LIST OF NO FROM 0 to 19 USING LIST FUNCTION(ITERABLE)
num = list(range(20))
print(num, "\n")

# REMEMBER STRING ARE ALSO ITERABLE I.E YOU CAN LOOP OVER THEM
char = list("Hello World")
print(char, "\n")

print(num, "\n")
print(num[::2], "\n")  # This will return every 2nd number in the list
print(num[::-2], "\n")  # Negative index starts from the end

# LIST UNPACKING

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Definignonly first two  items in a list and everything else will be stored in the list created 'other' using *list_name
first, second, *others, last = numbers

print(first)
print(others)
print(last, "\n")


# LOOPING OVER A LIST

for letter in letters:
    print(letter)

print("\n")
# To get index of a each list item alongwith the list we use 'enumerate' function

# 'enumerate' FXN GENERATES A TUPLE, WHICH IS LIKE ALIST AND ITERABLE BUT CANNOT ADD NEW ITEM

for letter in enumerate(letters):
    print(letter)

# To unpacjk a Tupple in a loop

items = (0, "a")
index, letter = items
print("\n", index, letter, "\n")

for index, letter in enumerate(letters):
    print(index, letter)

 # APPENDING A LIST

letters.append("d")
print(letters, "\n")

# ADDING AN ITEM AT SPECIFIC POSITION
letters.insert(0, "-")
print(letters, "\n")

# REMOVING AN ITEM FROM THE END OF A LIST
letters.pop()
print(letters, "\n")

letters.pop(0)  # Removing an item from specific index number
print(letters, "\n")

# Removing an element directly without knowing its index number
letters.remove("b")
print(letters, "\n")

del letters[0:1]  # 'del' is also used to remove elements and also helps in removing range of elements from a lsit while pop only deletes single element at a time

letters.clear()  # To remove all the elements from a list
print(letters)   # Will print only empty list


# FINDING INDEX OF AN ELEMENT

letters = ["a", "b", "c"]
print(letters.index("b"))  # Using 'index'

# Gives the number of occurence of given item in a list
print("\n", letters.count("d"))

# SORTING A LIST

numbers = [3, 51, 2, 8, 6]
numbers.sort()
print(numbers, "\n")

numbers.sort(reverse=True)  # Descending order
print(numbers, "\n")

# sorted() takes any iterable and sort it
# sorted() will not modify the exiting list it will return new sorted list

print(sorted(numbers))  # print(sorted, reverse = True)
print(numbers)  # Before sorted list remains unchanged

# SORTING LIST OF TUPLES

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]

items.sort()  # Nothing is changed because python does not know how to sort a tupke
print(items)


# def sort_item(item):
#     return item[1] # Sorting by the price


# items.sort(key=sort_item)
# print("\n", items)


# LAMBDA FUNCTIONS/EXPRESSIONS - one line anonymous function

# lambda parameters:expression(return) , hence no need for sort_item function
items.sort(key=lambda item: item[1])
print("\n", items)

# MAP FUNCTION

prices = []

for item in items:
    prices.append(item[1])  # Returns the prices

print("\n", prices)

# map(lambda each_item_in_list : return_statement, list_name iterable)
# Returns a map abject which is another iterable
x = map(lambda item: item[1], items)
print(f"Obtained another iterable : {x}\n")

# Hence using loop to extract the element

for item in x:
    print(item)

# ALTERNATIVELY

# Directly converting map object to list
pricess = list(map(lambda item: item[1], items))
print("\n", pricess)


# FILTERING LIST using 'filter fxn'

# filter(fxn, iterable) , gives filter object which is iterable like map() and hence can be loop over
y = filter(lambda item: item[1] >= 10, items)  # Returning list with prices>=10
print("\n", list(y))


# LIST COMPREHENSION
# [expression for item in items_i.e._an_iterable] , iterating over an iterable and applying the expression to each item

pricese = [item[1] for item in items]  # Does the same operation as in line 160
print(f"\nMap Using List Comprehension : {pricese}\n")

# Iterate over each item and then will return each item however after filtering them
# It has same operations as in line 167

filtered = [item for item in items if item[1] >= 10]
print(f"Filtered Using List Comprehension : {filtered}\n")


# ZIP FUNCTION= Combinig lists into single list of tuples

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Desired Output : [(1,10), (2,20), (3,30)]

print(list(zip(list1, list2)))
print(list(zip("abc", list1, list2)))  # Passing a string alongwiths lists


# STACK [LIFO BEHAVIOUR]

# LIFO - Last In First Out (Stack Datastructure)

# Using list as a stack [Below is an example of browser switching between pages 1, 2, 3]

browsing_session = []  # Empty list
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print("\n", browsing_session)
last = browsing_session.pop()
print(last)
print(browsing_session)
print("Redirect", browsing_session[-1])

print(browsing_session)

# FALSY VALUES : 0,"",[]

if not browsing_session:  # i.e if not []
    print("Disable")


# QUEUES [FIFO BEHAVIOUR]

# FIFO - First In First Out

# [1, 2, 3, 4] <- Here 1 is inserted first and must be taken out first and the rest must be  shifted to left
# Such shifting can be done through a module(bucket withbunch of reusable code) - 'deque'


queue = deque([])  # Passing empty list into a deque object

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

print("\n", queue, "\n")

# Using 'not' operator to check whether the queue is empty or not

if not queue:
    print("Empty Queue")


# TUPPLES - A read only List, we can use it to contain sequence of objects, but cannot modify, add and remove existing object within a Tupple i.e they are immutable

# Using Paranthesis to define an empty Tupple instead of [], for a list.
point = (1, 2)

# Other methodes of defining a Tupple : point = 1,2 or point = 1,
point1 = 1, 2
point2 = 1,
print("\n", type(point1), type(point2), "\n")

# We can concatenate a Tupple

point += 3, 4

popro = point1*3

print(point, popro, "\n")

# Converting a list to a tupple using a 'tupple' function

# tuple(iterable) , remember a string is also an itereable
pp = tuple([1, 2, 3])
pp1 = tuple(("Hello World"))

print(f"The tuple generated :\n {pp} \n {pp1} \n")

# Similar to a lsit we can use index to access individual item/object
print(point[0:2])


# Unpacking a tuple
x, y, z = pp  # Defining three variables
print(pp[y], "\n")

# SWAPPING VARIABLES

x = 10
y = 11  # Without using a third varable

x, y = y, x  # Here we have defined a tuple and unpacking it to lest side

# ARRAYS - Dealing With Large Sequence Of Numbers, They are fast and takes less memory
# To use array we need to first import it from array module as done in line 5


# array(typecode, list of integers/strings/etc) , you can search google for python 3 typrcode
numbers = array("i", [1, 2, 3])  # Here "i" is a typecode for integers

numbers.append(4)  # To append at the end of the list
numbers.insert(5, 7)  # To add number 7 at specific index 5
print(numbers, "\n")

# SET - A an unordered collection with no duplicates and is represented by {}
# Helpful in removinfg the duplicates from a list, after converting it to set

numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
print("\n", uniques, "\n")

first = set(numbers)
second = {1, 5}  # Creating a set
# second.add(5)
# second.remove(1)
# print(len(second), "\n")

# Set is also useful in carrying out various mathematical operations

# Will give union of first and second set
print(f" The Union of 2 sets: {first | second}\n")
print(f" The Intersection of 2 sets: {first & second}\n")
# Will return a set containing values of first set not present in second set
print(f" The Difference of 2 sets: {first - second}\n")
# Will return the items that are either in first or second set but not in both
print(f" The Sematic Differnce of 2 sets: {first ^ second}\n")

# ELEMENTS IN A SET CANNOT BE ACCESSED THROGH INDEX NO I.E. 'print(first[0])' will show error


# DICTIONARIES - Key-Value Pair
# dict() can also be used to define a dictionary object

point = {"x": 1, "y": 2}
point1 = dict(x=1, y=2)
print(point1["x"], "\n")  # Accessing a dict object using its key

point1["x"] = 10  # Modifying
point1["z"] = 20  # Adding new K-V Pair

print(point1, "\n")


# Checking whether K-V Pair exists or not

if "y" in point1:
    print(point1["y"], "\n")

print(point1.get("a"))  # Checks whether key exists or not and returns "None"
print(point1.get("b", 0))  # Here will return 0 whereas "None" is by deault

del point1["x"]  # deletes the K-V pair
print(point1, "\n")

# LOOP OVER DICT

for key in point1:
    print(key, point1[key])

# Another way of looping over dict()

for x in point1.items():  # WIll give K-V Tuple
    print(x)

print("\n")
# The Unpacking can be done through

for key, value in point1.items():  # WIll unpack K-V Tuple
    print(key, value)

# DICTIONARY COMPREHENSION

values = []  # An example of list comprehension
for x in range(5):
    values.append(x*2)

# The abe same can be done through list comprehension
# [expression for item in iterable]
values = [x*2 for x in range(5)]

# Replacing [] with {} will give set
values = {x*2 for x in range(5)}

# FOR DICTIONARY COMPREHENSION

# values = { x : x*2 for x in range(5)} # {key:value_expression for item in iterable}

# The above comprehension is same as :
values = {}
for x in range(5):
    values[x] = x*2


# GENERATOR EXPRESSION (Memory Efficient)

# Generator objects are iterable and generate new value. Unlike list they dont store value in the memory but generates new value in each iteration

# Using paranthesis gives generator object
values1 = (x*2 for x in range(1000))  # Generator obj
values2 = [x*2 for x in range(1000)]  # List obj
print(f" Type of values1 is: {values1}\n")
# for x in values1:
#     print(x)

# GETTING SIZE OF AN OBJECT using : from sys import getsizeof

print("Generator obj values1 size in bytes for storing 1000 numbers:",
      getsizeof(values1))
print("List obj values2 size in bytes for storing 1000 numbers:", getsizeof(values2))

# Generator obj doesnot store all of the items in memory and hence won't be able to get the total no of items working with

# We can only access all of the Generator obj values only when we iterate over them

# Hence print(len(value1)) will show error


# UNPACKING OPERATOR (*)- Dealing with different data structures AND ALSO USED TO UNPACK ANY ITERABLE

numbers4 = [1, 2, 3]
print(numbers4, "\n")  # Willprint the list
print("Unpacked List using * operator :", *numbers4)     # Will unpack the list

values4 = list(range(5))
print("\n", values4)

values3 = [*range(5), *"Hello"]
print(values3)

# Combining multiple lists using *

third = [1, 2]
fourth = [3]
# Unpacking third and fourth list into another list
values5 = [*third, *fourth]
print("\n", values5, "\n")

# TO UNPACK A DICTIONARY OBJECT USE ** OPERATOR

f = {"x": 1}
s = {"x": 10, "y": 2}
# Creating an emoty list and then unpacking other lists into it
combined = {**f, **s, "z": 3}
# IF YOU HAVE MULTIPLE VALUES WITH THE SAME KEY THEN THE LAST VALUE WILL BE USED
print(combined, "\n")


# EXCERCISE
# COUNTING THE NO OF CHARACTERS IN A STRING

sentence = "This is a common interview question"

char_frequency = {}  # Creating an empty dictionary

for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print("Characters frequency : ", char_frequency, "\n")

# Using pprint to print readable : from pprint import pprint

pprint(char_frequency, width=1)

print("\n")
# .items method returns all the key-value pairs as tuples
# TO sort tuple excepts k-v pair and returns k-v[1] value
char_freq_sorted = sorted(char_frequency.items(),
                          key=lambda kv: kv[1], reverse=True)

print("\n The most frequent character :", char_freq_sorted[0])


# END
