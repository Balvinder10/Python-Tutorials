# CLASSES - Are blueprints for creating new objects of particular type
# OBJECT - Is an instance of a class

# Example , Class: Human, which will define all the attributes of Humans
# Example , Objects (in the Classs: Human) : John, Mary, Jack

# CREATING CUSTOM CLASSES


from abc import ABC, abstractmethod


class Point:  # Creating Class Point - First Letter of every word must be upper case and should not have underscore
    def draw(self):  # Defining all the functions related to Point class and all functions in our classes should have atleast one parameter and by convention it is "self"
        print("Draw")


point = Point()
print(type(point))

# Function to know whether a paticular object is an istance of a given class
print(isinstance(point, Point))

# CONSTRUCTOR

# Providing initial values for the variables to be passed into a function

# USING SELF WE CAN READ ATTRIBUTE OF THE CURRENT OBJECT OR CAN CALL OTHER METHODS OF THE OBJECT


class Point1:
    def __init__(self, x, y):  # MAGIC METHOD (CONSTRUCTOR) AND IS EXECUTED WHEN WE CREATE A NEW POINT1 OBJECCT. HERE SELF IS A REFERENCE TO CURRENT POINT1 OBJECT WHEREAS X & Y ARE ADDITIONAL PARAMETERS TO INITIALISE A POINT1 OBJECT.
        self.x = x  # Since self is a reference to current object
        self.y = y  # Wit this when we use '.' operator we can use x,y and draw as well

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point1(1, 2)
point.z = 10  # There is no need to define all the attributes within a constructor and can be defined later since objects in python are dynamic
point.draw()

another = Point(3, 4)
another.draw()

# Above mentioned attributeds i.e x, y and z are called instance attributes i.e attributes that belong to Point1 ojects or instances

# Example (Instance attributes) - different eye colours of different people
# Example (Class attributes)    - all people have 2 eyes - Attributes at the class level and same across all instances of a class i.e shared across all instances of a class

# CLASS VS INSTANCE ATTRIBUTES


class Point2:
    default_color = "red"  # Defining a class level attribute

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point2 = Point2(1, 2)
print(point2.default_color)

# If we change class attribute than its change is visible across all objets of that type
Point2.default_color = "yellow"
print(Point2.default_color)


# CLASS VS INSTANCE METHODS

class Point3:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):  # Its first parameter is class i.e. 'cls' and is reference to class
        # Giving initial values to Point3 object and is equivalent to Point3(0, 0)
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


# Zero is a method defined at class level and is also called factory method
# Creating a Class method saves time of intialising parameter again and again
point3 = Point3.zero()
point3.draw()

# MAGIC METHODS - '__' AND ARE CALLED AUTOMATICALLY BY INTERPRETOR

# COMPARING OBJECTS


class Point4:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):  # RETURN STRING REPRESENTATION OF THE OBJECT
        return f"({self.x}, {self.y})"

    def __eq__(self, other):  # MAGICAL METHOD TO CHECK EQUALITY
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):  # MAGICAL METHOD TO CHECK > OR <
        return self.x > other.x and self.y > other.y

    def __add__(self, other):  # MAGICAL METHOD TO ADD TWO OR MORE OBJECTS
        # CREATING NEW POINT OBJECT WHICH WILL RETURN ADDITION
        return Point4(self.x+other.x, self.y + other.y)


point4 = Point4(10, 20)
other = Point4(1, 2)

print(point4 == other)  # OP is False without '__eq__' magical method because by deafault "==" compares the references or addresses of these two objects in memory i.e point and other variable are referencing 2 difffernt objects in memory. HENCE CAN BE SOLVED USING MAGIC METHOD WHICH CAN BE SEARCHED ONLINE
print(point4 > other)


# PERFORMING MATHEMATICAL OPERATIONS BETWEEN 2 OBJECTS USING MAGICAL METHOD

combined = point4 + other
print(combined.x)
print(point4)  # WIll give type and address of the poin4 object in mempry BUT after using '__str__' magical method converts an object into a string


# MAKING CUSTOM CONTAINERS

# EARLIER COMMON DATASTRUCTURE LIKE LISTS, SETS, DICTIONARIES ETC ARE CONTAINER TYPES

class TagCloud:  # Jeeping track of number of tags on a block and this class represents a container
    def __init__(self):
        self.tags = {}  # Initialising tags attribute as a dictionary

    def add(self, tag):  # To check if we have a particular tag in a dictionary
        # get method to get an a item by a key - 'tag' and supply a default value 0, if we dont have that and increment by 1
        # Case sensitivity is taken into account while setting it as well as reading it
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):  # Here tag is a key
        # With this implementation we can easily get the value a tag-key
        return self.tags.get(tag.lower(), 0)

    # setitem magical method is to set the value(i.e. count) for a key(i.e. tag). It take 3 parameters- tag, key, value
    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):  # To get number of items in a TagCloud
        return len(self.tags)

    def __iter__(self):  # To iterate over Tagcloud
        # iter function returns iterable object, which gives one item at a time
        iter(self.tags)


cloud = TagCloud()  # Creating a cloud Object
cloud.add("python")
cloud.add("python")
cloud.add("Python")  # Gives K-V pair , where K - python
print(cloud.tags)
# getitem magic method but we cannot set i.e cloud["python"] = 10
print(cloud["python"])
cloud["python"] = 10  # Possible because of setitem magical method
print(cloud["python"])
print(len(cloud))  # Possible because of len magical method


# PROPERTIES

class Product:
    def __init__(self, price):
        # self.__price = price # Setting Price attribute and making price attribute as private member by prefixing it with '__'
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")

        self.__price = value

    # property function will return a property object that allows us to set and get value of an attribute
    # Inbuilt property function takes 4 parameters- for_getting the value of an attribute, for_Setting value of an attribute, for_deleting value of an attribute and for_documenting value of an attribute
    price = property(get_price, set_price)


product = Product(10)
print(product.price)
product.price = -10
print(product.price)


# INHERITANCE - IS A MECHANISM THAT ALLOWS US TO DEFINE THE COMMON BEHAVIOUR OR COMMON FUNCTIONS IN ONE CLASS AND INHERIT THEM IN OTHER CLASSES

# HERE WE HAVE DUPLICATED THE EAT IMPLEMENTATION IN BOTH THE CLASSES - MAMMAL AND FISH

# class Mammal:
#     def eat(self):
#         print("eat")

#     def walk(self):
#         print("walk") # Select , then shift+alt+down arrow to duplicate selected part

# class Fish:
#     def eat(self):
#         print("eat")

#     def swim(self):
#         print("swim") # Select , then shift+alt+down arrow to duplicate selected part


# THIS PROBLEM OF REPETITION CAN BE SOLVED USING INHERITANCE OR COMPOSITION
# HENCE DEFINING A SEPARATE CLASS ANIMAL

class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")

# Animal: Parent/Base Class
# Mammal and Fish: Child/Sub Class


class Mammal(Animal):  # Just define Animal as a parameter in the class which inherits the attributes of Animal Class

    def __init__(self):
        super().__init__()  # super to give access to base class - Animal and can call any method from the base class to sub class
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        # Select , then shift+alt+down arrow to duplicate selected part
        print("walk")


class Fish(Animal):

    def swim(self):
        print("swim")


m = Mammal()  # Creating a Mammal object 'm'
m.eat()  # Inheriting a method
print(m.age)  # Inheriting a attribute

# Tells us if an object is an instancce of a given class i.e is m object an instance of Mammal Class
print(isinstance(m, Mammal))
print(isinstance(m, Animal))  # True becaus Mammal inherits from Animal Class
# To check if a class derives/inherits from another class
print(issubclass(Mammal, Animal))


# METHOD OVERRIDING

print(m.age)  # Will give attrinute error because the constructor in Animal class gets replaced by constructor in Mammal Class

# THIS CAN BE RESOLVED BY USING BUILT IN "SUPER" FUNCTION IN THE MAMMAL CLASS TO GET ACCESS TO BASE/SUPER CLASS

# MULTI-LEVEL INHERITANCE


class Animals:
    def eat(self):
        print("Eat")

    class Bird(Animal):
        def fly(self):
            print("Fly")

    class Chicken(Bird):
        pass  # Pass statement to define an empty class


# HERE CHICKEN CLASS INHERITS ALL THE ATTRIBUTES OF A BIRD CLASS BUT A CHICKEN CAN'T FLY - IS CALLED INHERITANCE ABUSE

# THEREFORE LIMIT INHERITANCE TO 1 TO 2 LEVELS ONLY

class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):  # Multiple Inheritance, Class with 2 Base classes
    pass


manager = Manager()
manager.greet()  # Will EXECUTE EMPLOYEE_GREET METHOD BECAUSE EMPLOYEE IS FIRST AND LOOKUP TERMINATES THE MOMENT IT CAME ACROSS FIRST GREET. IF IT WASN'T PRESENT IN EMPLOYEE CLASS THEN IT WOULD HAVE LOOKED INTO PERSON CLASS


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


# These 2 Base classes are small, abstract and have nothing in common - IS A GOOD EXAMPLE OF MULTIPLE INHERITANCE
class FlyingFish(Flyer, Swimmer):
    pass

# A GOOD EXAMPLE OF INHERITANCE


# Making a custom exception - InvalidOperationError which is not present in Python Lib and is derived from - Base Exception Class in the Python
class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):  # Flag to know if Stream is open or not
        self.opened = False

    def open(self):  # Defining a Open Method
        if self.opened:  # If Stream is already opened
            raise IndentationError("Stream is already opened")
        self.opened = True

    def close(self):  # Defining a close Method
        if not self.opened:  # If stream is already closed
            raise IndentationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from a Network")

# ABSTRACT BASE CLASSES - its purpose is to provide common code to its derivatives


stream = MemoryStream()
stream.open()

# from abc import ABC, abstractmethod, here abstractmethid will be used as a decorator
# TO MAKE STREAM CLASS ABSTRACT WE NEED TO DERIVE IT FROM ABC CLASS


class UIControl(ABC):
    # @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(controls):  # draw fxn that takes UIControl Object
    for control in controls:  # Using for loop to iterate over controls object
        control.draw()  # Calls Drawmethod


ddl = DropDownList()
textbox = TextBox()

# Passing a list of control objects - PolyMorphism - draw method is taken different form and is determined during run time - i.e. draw method in textbox,dropdownlist etc
# Perfectly fine because DropDownList is an instance of UIControl i.e ddl object is an instance of UIControl and wherever we expect a UIControl Object we can pass any of its derivatives like Textbox, DropDownList etc.
draw([ddl, textbox])


# -----------------------------END-----------------------
