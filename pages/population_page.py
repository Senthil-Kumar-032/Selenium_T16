from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)   # Wait up to 20 seconds

    cookie_button_xpath = "//a[contains(@class,'cc-dismiss') and contains(text(),'Got it')]"  # Cookie button
    population_xpath = "(//span[contains(@class,'counter-number')])[1]"  # Population value

    def accept_cookies(self):
        #   Handle cookie popup
        try:
            button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.cookie_button_xpath))  # Wait for button
            )
            self.driver.execute_script("arguments[0].click();", button)  # Click using JS
        except:
            print("Cookie popup not found")  # If not present

    def get_population(self):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class,'counter')]")  # Wait for counter section
                )
            )
            text = element.text  # Get full text

            import re
            match = re.search(r'[\d,]{7,}', text)  # Extract number
            return match.group() if match else "Not Found"  # Return result

        except:
            return "Not Found"  # If error