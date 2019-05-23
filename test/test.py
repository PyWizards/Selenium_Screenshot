# For Full Page ScreenShot :

from selenium import webdriver

from Screenshot import Screenshot_Clipping

ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url = ob.full_Screenshot(driver, save_path=r'D:\Sayar Mendis\Python_Projects\Selenium\test',
                             image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()

# For Html Element Clipping :

from Screenshot import Screenshot_Clipping
from selenium import webdriver

ob = Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
driver.get(url)

element = driver.find_element_by_class_name('signup-prompt')
img_url = ob.get_element(driver, element, r'D:\Sayar Mendis\Python_Projects\Selenium\test')
print(img_url)

driver.close()

driver.quit()

# For Html Element Clipping with Hiding Element :

from Screenshot import Screenshot_Clipping
from selenium import webdriver


ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3"
driver.get(url)
Hide_elements = ['class=avatar width-full height-full avatar-before-user-status']  # Use full class name
img_url = ob.full_Screenshot(driver, save_path=r'D:\Sayar Mendis\Python_Projects\Selenium\test', elements=Hide_elements,
                             image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()