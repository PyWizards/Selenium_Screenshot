import os
import unittest

from PIL import ImageChops, Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Screenshot import Screenshot
from test.util.mock_server import run_server

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
WEBSITE_DIR = os.path.join(DATA_DIR, 'data/website')


class TestScreenshot(unittest.TestCase):
    def setUp(self):
        _, address = run_server(WEBSITE_DIR, 8000)
        self.base_url = address
        options = webdriver.ChromeOptions()
        options.add_argument("window-position=0,0")
        options.add_argument("window-size=1000,1000")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.ob = Screenshot.Screenshot()

    def tearDown(self):
        self.driver.quit()

    def test_full_screenshot(self):
        image_name = 'full_screenshot.png'
        url = self.base_url + '/test.html'
        image_ref_path = os.path.join(DATA_DIR, 'data', image_name)

        self.driver.get(url)
        img_url = self.ob.full_screenshot(self.driver, save_path=r'.', image_name=image_name, is_load_at_runtime=True,
                                          load_wait_time=3)

        image_ref = Image.open(image_ref_path)
        image_result = Image.open(img_url)
        diff = ImageChops.difference(image_ref, image_result)
        equal = not diff.getbbox()
        # if not equal:
        #     diff.show()
        # assert equal

        image_ref.close()
        image_result.close()
        os.remove(img_url)

    def test_element_screenshot(self):
        image_name = 'paypal.png'
        image_ref_path = os.path.join(DATA_DIR, 'data', image_name)
        url = self.base_url + '/test.html'

        self.driver.get(url)
        element = self.driver.find_element(By.XPATH, "//img[@title='Donate via PayPal']")
        img_url = self.ob.get_element(self.driver, element, save_path=r'.', image_name=image_name)

        image_ref = Image.open(image_ref_path)
        image_result = Image.open(img_url)
        diff = ImageChops.difference(image_ref, image_result)
        equal = not diff.getbbox()
        # if not equal:
        #     diff.show()
        # assert equal

        image_ref.close()
        image_result.close()
        os.remove(img_url)

    def test_hide_element(self):
        image_name = 'hide_element.png'
        image_ref_path = os.path.join(DATA_DIR, 'data', image_name)
        url = self.base_url + '/test.html'

        self.driver.get(url)
        hide_elements = ['class=position-relative js-header-wrapper ']
        img_url = self.ob.full_screenshot(self.driver, save_path=r'.', image_name=image_name,
                                          hide_elements=hide_elements)

        image_ref = Image.open(image_ref_path)
        image_result = Image.open(img_url)
        diff = ImageChops.difference(image_ref, image_result)
        equal = not diff.getbbox()
        # if not equal:
        #     diff.show()
        # assert equal

        image_ref.close()
        image_result.close()
        os.remove(img_url)
