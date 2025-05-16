from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver, base_url, timeout=10):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        self.driver.get(self.base_url)

    def get_title(self):
        return self.driver.title

    def is_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def get_element_attribute(self, locator, attribute):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.get_attribute(attribute)