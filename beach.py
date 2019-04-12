#! /usr/bin/env python

import selenium
from selenium import webdriver

student_id = 'YourStudentId'
password = 'YourPassword'

# Open beach board login
browser = webdriver.Chrome("PathToChromeDriver")
browser.get("https://csulb.okta.com/?tab=PAPP_GUEST")

# Wait
browser.implicitly_wait(7)

# Get login elements and sign in
login = browser.find_element_by_css_selector('#okta-signin-username')
login.send_keys(student_id)

# Get password
password_login = browser.find_element_by_css_selector('#okta-signin-password')
password_login.send_keys(password)

# Get/click submit button
button = browser.find_element_by_css_selector('#okta-signin-submit')
button.click()

# Wait then click beachboard button
browser.implicitly_wait(5)
beach_board = browser.find_element_by_css_selector('#main-content > div > div.container.content-wrapper > ul.app-buttons-list.clearfix.ui-sortable > li:nth-child(4) > a')
beach_board.click()

# Maximize window
browser.maximize_window()

