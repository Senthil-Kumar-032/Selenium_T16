import pytest
from selenium import webdriver

@pytest.fixture
def setup():
    driver = webdriver.Chrome()        # Launch Chrome browser
    driver.maximize_window()           # Maximize window
    # Open target URL
    driver.get("https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live")
    yield driver                      # Provide driver to test
    driver.quit()                     # Close browser after test