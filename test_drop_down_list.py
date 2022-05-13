import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestDropDownList(unittest.TestCase):

    """TestingDropDownList
    http://the-internet.herokuapp.com/dropdown"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/dropdown"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_drop_down_list(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        drop_down = driver.find_element(By.CSS_SELECTOR, "#dropdown")
        self.assertTrue(drop_down)
        text = driver.find_element(By.CSS_SELECTOR, "#dropdown > option:nth-child(1)")
        self.assertEqual(text.text, "Please select an option")
        drop_down.click()
        time.sleep(2)
        hidden_option = driver.find_element(By.CSS_SELECTOR, "#dropdown > option:nth-child(2)")
        self.assertTrue(hidden_option)
        hidden_option.click()
        time.sleep(2)
        drop_down.click()
        time.sleep(2)

        driver.save_screenshot("option_1_selected.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
