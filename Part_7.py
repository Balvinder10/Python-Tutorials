# MODULES - SPLITTING A CODE INTO MULTIPLE FILES

# Importing from sales module

from Ecommerce.shopping import shop
from Ecommerce.customer import contact  # HERE CONTACT ACT AS AN OBJECT
from Ecommerce.shopping import shop  # HERE SHOP ACT AS AN OBJECT
from Ecommerce.Sales_M1 import calc_shipping, calc_tax


# OTHER METHOD FOR IMPORTING FROM A PACKAGE

# from Ecommerce import Sales_M1
# Sales_M1.calc_shipping


# OTHER METHOD OF IMPOTYING A MODULE

# import Sales_M1
# Sales_M1.calc_shipping()

# import Ecommerce.sales after creating a package


calc_shipping()  # Calling functions from Sales_M1 Module
calc_tax()


# TURNING A MODULE INTO A PACKAGE

# STEP 1 : CREATE A DIRECTORY WHERE YOU WANT TO SAVE THE MOADULE
# STEP 2 : MOVE THE MODULE IN THE SAME DIRECTORY AND CREATE ANOTHER FILE WITH NAME '__init__.py'


# CREATING A SUB MODULE - SHOP
# from Ecommerce.shopping import shop

# INTRA PACKAGE REFERENCE

# In our shop module we want to import contact module
# THIS CAN BE ACHIEVED THROUGH ABSOLUTE/RELATIVE IMPORT STATEMENT

# THIS HAS TO BE WRITTEN IN SHOP MODULE
# from Ecommerce.customer import contact - ABSOLUTE IMPORT

# from ..customer import contact # RELATIVE IMPORT '..' TAKES ONE LEVEL UP FROM THE CURRENT MODULE (THIS HAS TO BE WRITTEN IN SHOP MODULE) I.E. ECOMMERCE FROM THERE WE CAN GO TO DESIRED PACKAGE


contact.cus_con()


# THE DIR FUNCTION - USE TO FIND THE LIST OF ATTRIBUTES AND METHODS IN AN OBJECT
print(dir(shop))
print(shop.__name__)
print(shop.__package__)
print(shop.__file__)
