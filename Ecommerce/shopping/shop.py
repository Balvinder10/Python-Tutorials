# SHOP.PY IS A SUB MODULE UNDER SHOPPING DIR WHICH IN TURN IS UNDER ECOMMEERCE DIR

from Ecommerce.customer import contact
print("Shop Module Initialesd")


def calc_bags():
    pass


def calc_items():
    pass


# THIS HAS TO BE WRITTEN IN SHOP MODULE
# from Ecommerce.customer import contact

contact.cus_con()

# RELATIVE IMPORT FOR INTRA PACKAGE

# from ..customer import contact
