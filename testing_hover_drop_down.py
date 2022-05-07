import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestHoverDropDown(unittest.TestCase):

    """TestingHoverDropDown
    http://the-internet.herokuapp.com/hovers"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/hovers"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_hover_drop_down(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        image = driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(3) > img:nth-child(1)")
        self.assertTrue(image)
        hidden_submenu_of_the_image = driver.find_element(By.CSS_SELECTOR, "div.figure:nth-child(3) > div:nth-child("
                                                                           "2) > a:nth-child(2)")
        self.assertTrue(hidden_submenu_of_the_image)
        action = ActionChains(driver)
        action.move_to_element(image)
        action.click(hidden_submenu_of_the_image)
        action.perform()
        driver.save_screenshot("clicked_hidden_drop_down_menu.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
