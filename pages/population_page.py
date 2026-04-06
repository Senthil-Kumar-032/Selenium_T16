from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PopulationPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)   # Wait up to 20 seconds

    # Correct cookie XPath (your element)
    cookie_button_xpath = "//a[contains(@class,'cc-dismiss') and contains(text(),'Got it')]"

    # Population XPath
    population_xpath = "(//span[contains(@class,'counter-number')])[1]"

    def accept_cookies(self):

        #   Handle cookie popup

        try:
            button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, self.cookie_button_xpath))
            )
            self.driver.execute_script("arguments[0].click();", button)
        except:
            print("Cookie popup not found")

    def get_population(self):
        try:
            element = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class,'counter')]")     # Wait for counter section
                )
            )
            text = element.text

            # extract only numbers
            import re
            match = re.search(r'[\d,]{7,}', text)
            return match.group() if match else "Not Found"      # Return result

        except:
            return "Not Found"                                  # If error