import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestScrolling(unittest.TestCase):

    """TestingScrolling
    http://the-internet.herokuapp.com/disappearing_elements"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/disappearing_elements"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_scrolling(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        home_menu = driver.find_element(By.CSS_SELECTOR, ".example > ul:nth-child(4) > li:nth-child(1) > a:nth-child(1)")
        self.assertTrue(home_menu)
        home_menu.click()
        time.sleep(5)
        menu_to_select = driver.find_element(By.CSS_SELECTOR, "#content > ul:nth-child(4) > li:nth-child(26) > a:nth-child(1)")
        self.assertTrue(menu_to_select)
        actions = ActionChains(driver)
        actions.move_to_element(menu_to_select).perform()
        time.sleep(2)
        menu_to_select.click()
        time.sleep(2)

        driver.save_screenshot("menu_selected.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
