# pipenv install beautifulsoup4 - Powerfull package for extracting info from html and xml file
# pipenv install requests

import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")

# response.text # response.text returns the html content of the page

# Second argument is the type of parser you are dealing with , in our case it is html.parser
soup = BeautifulSoup(response.text, "html.parser")

# soup object mirrors the structure of the html document

# After inspect - using soup element finding all elements containing question-summary - Will return a list and each item in the list is instance of the tag class
questions = soup.select(".question-summary")
print(type(questions[0]))

# Will give the dictionary of tag containing attributes in that particular tag
print("\n", questions[0].attrs)
print("\n", questions[0]["id"])  # To acess attributes
# TO acess the attribute in a safer way and returns default value 0 if the attribute do not exist in the tag
print("\n", questions[0].get("id", 0))


print("\n", questions[0].select(".question-hyperlink"))  # CSS selector
# Returns on object rather than list
# print(questions[0].select_one(".question-hyperlink"))

# In order to acess only one and get Text only
print("\n", questions[0].select_one(".question-hyperlink").getText())


# ITERATING OVER ALL THE QUESTIONS AND GETTING TITLE OF EACH

for question in questions:
    print("\n", question.select_one(".question-hyperlink").getText())
    print(question.select_one(".vote-count-post").getText())


# ABOVE CODE IS FOR ONLY SPECIFIC PAGE
