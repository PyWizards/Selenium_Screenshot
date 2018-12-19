from Screenshot import Screenshot_Clipping
from selenium import webdriver
import os

ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot"
driver.get(url)
dir_path = os.path.dirname(os.path.realpath(__file__))
element=driver.find_element_by_class_name('pagehead-actions')
img_url=ob.Get_element(driver,element,r'E:\Sayar_python\Selenium\test')
# img_url=ob.Full_Scrrenshot(driver,r'E:\Sayar_python\Selenium\test')
print(img_url)

driver.close()

driver.quit()