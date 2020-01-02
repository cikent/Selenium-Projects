class UsersPage

    # css selectors
    SUCCESS_BANNER = {id: 'flash_success'}

    attr_reader :driver

    # class methods/functions
    def initialize(driver)
        @driver = driver
    end

    def get_banner_text()
        banner = @driver.find_element(id: 'flash_success')
        banner.text
    end

end