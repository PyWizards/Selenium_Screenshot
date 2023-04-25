import os
import sys
import time


DATA_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(DATA_DIR)))

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from Screenshot.Screenshot import Screenshot
from selenium.webdriver.edge.service import Service
from selenium import webdriver

iedriver_path = os.path.abspath(DATA_DIR + '/IEDriverServer.exe')


def test_IE():
    sc = Screenshot()
    # driver = webdriver.Edge(EdgeChromiumDriverManager(log_level=0).install())
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager(log_level=0).install()))
    url = 'https://github.com/PyWizards/Selenium_Screenshot'
    driver.get(url)
    time.sleep(10)
    image_path = sc.full_screenshot(driver, save_path='.', image_name='testimage.png', load_wait_time=5,
                                    is_load_at_runtime=True)
    os.remove(image_path)
    driver.close()

    driver.quit()
