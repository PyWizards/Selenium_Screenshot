

**Slenium Screenshot :**

The Selenium Screenshot is used to clipped Html Element using Selenium Webdriver

**Installations :**

`pip install Selenium-Screenshot`

This Package Supported for Python 3.*

**How to Use :** 

**For Full Page ScreenShot :**
```python
from Screenshot import Screenshot_Clipping
from selenium import webdriver



ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url=ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()
```

**For Html Element Clipping :**

````python
from Screenshot import Screenshot_Clipping
from selenium import webdriver


ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
driver.get(url)

element=driver.find_element_by_class_name('signup-prompt')
img_url=ob.get_element(driver, element, r'.')
print(img_url)

driver.close()

driver.quit()

````

**For Html Element Clipping with Hiding Element :**
````python
from Screenshot import Screenshot_Clipping
from selenium import webdriver


ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3"
driver.get(url)
Hide_elements=['class=avatar width-full height-full avatar-before-user-status'] # Use full class name
img_url=ob.full_Screenshot(driver, save_path=r'.', elements=Hide_elements, image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()


````

**Contact Information :**

[Email: sayarmendis26@gmail.com](mailto::sayarmendis26@gmail.com)

