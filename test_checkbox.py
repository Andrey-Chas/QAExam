import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestCheckBox(unittest.TestCase):

    """TestingCheckBox
    http://the-internet.herokuapp.com/checkboxes"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/checkboxes"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_check_box_1_remove_check_box_2(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        checkbox_1 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[1]")
        self.assertTrue(checkbox_1)
        checkbox_2 = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input[2]")
        self.assertTrue(checkbox_2)
        checkbox_1.click()
        time.sleep(2)
        checkbox_2.click()
        time.sleep(2)

        driver.save_screenshot("checked_box_1_removed_check_box_2.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

