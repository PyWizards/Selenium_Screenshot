
**Slenium Screenshot :**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/selenium-screenshot)](https://pepy.tech/project/selenium-screenshot)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)


The Selenium Screenshot is used to clipped Html Element using Selenium Webdriver

**Supported WebDriver :**

- Chromedriver
- IEDriverServer

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
**Limitation :**

- Screenshot can take only 10000 of height of website


**Contact Information :**

[Email: sayarmendis26@gmail.com](mailto::sayarmendis26@gmail.com)

**Donation :**

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares :)

<a href="https://www.instamojo.com/@sayarmendis26/" target="_blank"><img src="https://www.soldermall.com/images/pic-online-payment.jpg" alt="Donate via Instamojo" title="Donate via instamojo" /></a>
