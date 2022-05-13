import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestShiftingContent(unittest.TestCase):

    """TestingShiftingContent
    http://the-internet.herokuapp.com/shifting_content"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/shifting_content"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_choosing_example_1(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        menu_element = driver.find_element(By.CSS_SELECTOR, ".example > a:nth-child(3)")
        self.assertTrue(menu_element)
        menu_element.click()
        powered_by = driver.find_element(By.CSS_SELECTOR, ".large-4 > div:nth-child(2) > a:nth-child(1)")
        self.assertTrue(powered_by)
        print("Found powered by")
        time.sleep(2)

        driver.save_screenshot("menu_element_chosen.png")
        time.sleep(5)

    def test_choosing_example_2(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        an_image = driver.find_element(By.CSS_SELECTOR, ".example > a:nth-child(6)")
        self.assertTrue(an_image)
        an_image.click()
        powered_by = driver.find_element(By.CSS_SELECTOR, ".large-4 > div:nth-child(2) > a:nth-child(1)")
        self.assertTrue(powered_by)
        print("Found powered by")
        time.sleep(2)

        driver.save_screenshot("an_image_chosen.png")
        time.sleep(5)

    def test_choosing_example_3(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        list1 = driver.find_element(By.CSS_SELECTOR, ".example > a:nth-child(9)")
        self.assertTrue(list1)
        list1.click()
        powered_by = driver.find_element(By.CSS_SELECTOR, ".large-4 > div:nth-child(2) > a:nth-child(1)")
        self.assertTrue(powered_by)
        print("Found powered by")
        time.sleep(2)

        driver.save_screenshot("list_chosen.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
