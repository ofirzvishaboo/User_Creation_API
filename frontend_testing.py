import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Use the Selenium Grid URL instead of a local driver path


class FrontEndTests:
    def __init__(self, user_id=1):
        driver_path = os.environ.get('DRIVER_PATH')
        options = Options()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        
        # Make sure the URL is exactly correct without hidden characters
        grid_url = 'http://localhost:4444/wd/hub'
        
        self.driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )
        # self.driver = webdriver.Chrome(service=Service(driver_path))
        self.driver.implicitly_wait(10)
        self.driver.get(f'http://127.0.0.1:5001/users/get_user_data/{user_id}')

    def check_name(self):
        user_name_element = self.driver.find_element(By.ID, "user")
        if user_name_element.is_displayed():
            print(f"Name: {user_name_element.text}")
        else:
            print("User name element is not found.")


if __name__ == "__main__":
    frontend_tests = FrontEndTests(user_id=1)
    frontend_tests.check_name()
