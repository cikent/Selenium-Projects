require "selenium-webdriver"
require "rspec"

# Global variables for test execution
timestamp = Time.now.to_i
username = "user#{timestamp}"
email = "user#{timestamp}@test.com"
password = "password"
expected_banner_text = "Welcome to the alpha blog user#{timestamp}"

# Define function for sending username
def enter_username(username)
	username_field = @driver.find_element(id: 'user_username')
	username_field.send_keys(username)
end

# Define function for sending email
def enter_email(email)
	email_field = @driver.find_element(id: 'user_email')
	email_field.send_keys(email)
end

# Define function for sending password
def enter_password(password)
	password_field = @driver.find_element(id: 'user_password')
	password_field.send_keys(password)
end

# Define a function for selecting Submit/Enter on the page
def submit_form()
	sign_up_button = @driver.find_element(id: 'submit')
	sign_up_button.click
end

# Define a function to get the banner text confirmation
def get_banner_text()
	banner = @driver.find_element(id: 'flash_success')
	banner_text = banner.text
end

# TEST: Sign up for blog
describe "Blog application" do
  describe "signup to the blog application" do
    it "confirm that a user can successfully signup" do
    	@driver = Selenium::WebDriver.for :firefox
		# Go to signup form
        @driver.navigate.to "https://selenium-blog.herokuapp.com/signup"
		# Fill out and submit form
		enter_username(username)
		enter_email(email)
		enter_password(password)
		submit_form()

		# Confirm user is signed up successfully
		banner_text = get_banner_text()
		expect(banner_text).to eq(expected_banner_text) 

		@driver.quit
	end
  end
end
