# POPULAR PYTHON PACKAGES

# -----------APIs-------------

# End points(where you are sending request to) that are publicly accessible on the internet

# ------YELP API-------

# pip install pipenv
# pipenv install requests - Requests package to send http request
# Ctrl + Shft + P -> Python Select Interpreter -> Select Python: pipenv

import config
import requests
# import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "Enter API key"

headers = {  # For API authorization
    "Authorization": "Bearer " + api_key
}

params = {  # Sending the parameters
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)  # http request

# print(response.text) - Lets you know the response error

print(response.json())  # Convert the result into dictionary
businesses = response.json()["key"]

for business in businesses:
    print(business["name_key"])

# [item for item in list] - List Comprehension

names = [business["name_key"]
         for business in businesses if business["rating_key"] > 4.5]
print(names)  # GIves highest rated business names in NYC


# ----------HIDING API---------------

# Creating a config.py
# Moving api_key to config.py (cut-paste)

# import config -Importing config module which have attribute api_key

headers = {  # For API authorization
    "Authorization": "Bearer " + config.api_key
}

# To exclude config.py from git
# create .gitignore file and push file into .gitignore

# ---------SENDING TEXT MESSAGES--------------

# Using Twilio

# In Pytext dir
# pipenv install twilio
# from twilio.rest import Client

# --------------WEB SCRAPING------------------

# Not all the websites have APIs.
# So in situation like this is to parse the html behind web page, get rid of all the html tags and extraxt actual data

# Such programs are also called "WEB CRAWLER" or "WEB SPIDER"

# mkdir PyCrawler
# cd PyCrawler
# code . # To open current dir in vscode


# -------------SELENIUM - WEB AUTOMATION-------------------

# mkdir PySelenium
# pipenv install selenium
# Searchfor selenium in pypi.org -> Under Drivers -> Select your browser you want to automate
# Download the driver (according to your chrome version) and paste it in C:\Windows


# ---------------------PDF------------------------------

# mkdir PyPDF

# ---------------------NumPy-------------------------------

# mkdir NumPy


# ------------------------END----------------------