import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestHorizontalSlider(unittest.TestCase):

    """HorizontalSlider"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/horizontal_slider"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_horizontal_slider_arrow_right(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        slider = driver.find_element(By.CSS_SELECTOR, ".sliderContainer > input:nth-child(1)")
        self.assertTrue(slider)
        for _ in range(10):
            slider.send_keys(Keys.ARROW_RIGHT)
        driver.save_screenshot("horizontal_slider_arrow_right.png")
        range1 = driver.find_element(By.ID, "range")
        self.assertNotEqual(range1.text, "0")

        time.sleep(5)

    def test_horizontal_slider_arrow_up(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        slider = driver.find_element(By.CSS_SELECTOR, ".sliderContainer > input:nth-child(1)")
        self.assertTrue(slider)
        for _ in range(10):
            slider.send_keys(Keys.ARROW_UP)
        driver.save_screenshot("horizontal_slider_arrow_up.png")
        range1 = driver.find_element(By.ID, "range")
        self.assertNotEqual(range1.text, "0")

        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        # defaultTest="test_horizontal_slider_arrow_up"
    )
