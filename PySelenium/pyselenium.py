# AUTOMATING CHROME TO LOGIN INTO GITHUB AND CHECK THE USERNAME

from selenium import webdriver

# Creating an instance of the chrome class - Working browser is chrome

browser = webdriver.Chrome()

browser.get("https://github.com")

# FINDING ELEMENTS BY THEIR TAG, ID OR CLASS

# Finding by text and hence spellin the same way as on the page. Returns a web element
signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()  # Calling click method to click on the sign in on the page

# TO FIL IN THE DETAILS IN THE SPACE PROVIDED USING INSPECT

# In the input tag id uniquely identifies the login_field
username_box = browser.find_element_by_id("login_field")

# send_keys method simulates user typing in a text box
username_box.send_keys("User_Name")

# Similarly filling the password

# In the input tag id uniquely identifies the login_field
password_box = browser.find_element_by_id("password")

password_box.send_keys("Password")

password_box.submit()

browser.page_source  # Returns HTML content of the page

assert "Profile/User_Name" in browser.page_source  # assert statement to verify

# OR

profile_link = browser.find_element_by_class_name("user-profile-link")

link_label = profile_link.get_attribute("innerHTML")
assert "Profile/User_Name" in link_label

signout = browser.find_element_by_class_name("dropdown-signout")
signout.submit()

browser.quit()
