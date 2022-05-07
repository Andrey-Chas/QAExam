import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestDragAndDrop(unittest.TestCase):

    """TestingDragAndDrop"""

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.base_url = "https://qavbox.github.io/demo/dragndrop/"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)

    def test_drag_and_drop(self):
        driver = self.driver
        self.assertIn(self.base_url, driver.current_url)
        driver.implicitly_wait(30)
        driver.set_page_load_timeout(50)
        self.assertIn(driver.title, "DragnDrop")
        action = ActionChains(driver)
        source = driver.find_element(By.ID, "draggable")
        self.assertTrue(source)
        target = driver.find_element(By.ID, "droppable")
        self.assertTrue(target)
        action.drag_and_drop(source, target).perform()
        time.sleep(5)
        self.assertTrue(target.text, "Dropped!")
        time.sleep(2)
        driver.save_screenshot("drag_and_drop_success.png")

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
