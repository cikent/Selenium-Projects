require "selenium-webdriver"

# TEST: Sign up for blog
driver = Selenium::WebDriver.for :firefox
driver.navigate.to "https://selenium-blog.herokuapp.com/signup"

username_field = driver.find_element(id: "user_username")
username_field.send_keys("user")

email_field = driver.find_element(id: "user_email")
email_field.send_keys("email@test.com")

password_field = driver.find_element(id: "user_password")
password_field.send_keys("password")

submit_button = driver.find_element(id: "submit")
submit_button.click

driver.quit