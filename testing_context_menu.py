import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestContextMenu(unittest.TestCase):

    """TestingContextMenuAlert
    http://the-internet.herokuapp.com/context_menu"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "http://the-internet.herokuapp.com/context_menu"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_context_menu_alert(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        self.assertIn(driver.title, "The Internet")
        box_to_click = driver.find_element(By.ID, "hot-spot")
        self.assertTrue(box_to_click)
        action = ActionChains(driver)
        action.context_click(box_to_click).perform()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()
        driver.save_screenshot("alert_accepted.png")
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
