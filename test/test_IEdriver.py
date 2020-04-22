import os
import sys
import time

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(DATA_DIR)))

from Screenshot.Screenshot_Clipping import Screenshot
from selenium import webdriver

iedriver_path = os.path.abspath(DATA_DIR + '/IEDriverServer.exe')


def test_IE():
    sc = Screenshot()
    driver = webdriver.Ie(executable_path=iedriver_path)
    url = 'http://yandex.ru'
    driver.get(url)
    time.sleep(10)
    sc.full_Screenshot(driver, save_path='.', image_name='testimage.png',load_wait_time=5,is_load_at_runtime=True)
    driver.close()
    driver.quit()
