import os
import sys

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(DATA_DIR)))

from selenium import webdriver
from Screenshot import Screenshot_Clipping
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_full_screenshot():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install())
    url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
    driver.get(url)
    img_url = ob.full_Screenshot(driver, save_path=r'.',image_name='Myimage.png',is_load_at_runtime=True,load_wait_time=3)
    os.remove(img_url)
    driver.close()
    driver.quit()


def test_element_screenshot():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install())
    url = "https://github.com/PyWizards/Selenium_Screenshot"
    driver.get(url)
    element = driver.find_element_by_class_name('pagehead-actions')
    img_url = ob.get_element(driver, element, r'.')
    os.remove(img_url)
    driver.close()
    driver.quit()


def test_hide_element():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install())
    url = "https://github.com/sam4u3"
    driver.get(url)
    hide_elements = ['class=avatar width-full height-full avatar-before-user-status']  # Use full class name
    img_url = ob.full_Screenshot(driver, save_path=r'.', elements=hide_elements,
                                 image_name='Myimage.png')
    os.remove(img_url)
    driver.close()

    driver.quit()
