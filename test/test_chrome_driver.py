import os
import sys

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(DATA_DIR)))

from selenium import webdriver
from Screenshot import Screenshot_Clipping

chromedriver_path = os.path.abspath(DATA_DIR + '/chromedriver.exe')


def test_full_screenshot():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    # url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
    url = 'http://yandex.ru'
    driver.get(url)
    img_url = ob.full_Screenshot(driver, save_path=r'.',image_name='Myimage.png',is_load_at_runtime=True,load_wait_time=3)
    os.remove(img_url)
    driver.close()

    driver.quit()


def test_element_screenshot():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
    driver.get(url)

    element = driver.find_element_by_class_name('signup-prompt')
    img_url = ob.get_element(driver, element, r'.')
    os.remove(img_url)

    driver.close()

    driver.quit()


def test_hide_element():
    ob = Screenshot_Clipping.Screenshot()
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    url = "https://github.com/sam4u3"
    driver.get(url)
    Hide_elements = ['class=avatar width-full height-full avatar-before-user-status']  # Use full class name
    img_url = ob.full_Screenshot(driver, save_path=r'.', elements=Hide_elements,
                                 image_name='Myimage.png')
    os.remove(img_url)
    driver.close()

    driver.quit()
