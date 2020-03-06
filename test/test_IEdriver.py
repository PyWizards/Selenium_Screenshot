import os
import sys

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.dirname(DATA_DIR)))

from Screenshot.Screenshot_Clipping import Screenshot
from selenium import webdriver

iedriver_path = os.path.abspath(DATA_DIR + '/IEDriverServer.exe')


def test_IE():
    sc = Screenshot()
    object = webdriver.Ie(executable_path=iedriver_path)
    url = 'https://twitter.com'
    object.get(url)
    img_url = sc.full_Screenshot(object, save_path='.')
    os.remove(img_url)
    object.close()
    object.quit()
