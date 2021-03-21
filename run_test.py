import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
                command_executor = f"http://{os.environ['HUB_ENDPOINT']}/wd/hub",
                desired_capabilities = DesiredCapabilities.CHROME
                )

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

    def test_(self):
        self.driver.get("http://www.python.org")
        self.assertIn("Python", self.driver.title)
        elem = self.driver.find_element_by_name("q")
        elem.send_keys("pycon")
        assert "No results found." not in self.driver.page_source
        elem.send_keys(Keys.RETURN)

if __name__ == "__main__":
    unittest.main()
