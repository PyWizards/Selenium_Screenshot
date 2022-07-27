[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Selenium Screenshot :**

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/personalized-badge/selenium-screenshot?period=total&units=none&left_color=yellowgreen&right_color=blue&left_text=Downloads)](https://pepy.tech/project/selenium-screenshot)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PyPI version](https://badge.fury.io/py/Selenium-Screenshot.svg)](https://badge.fury.io/py/Selenium-Screenshot)
![Python package](https://github.com/sam4u3/Selenium_Screenshot/workflows/Python%20package/badge.svg)


The Selenium Screenshot is used to clipped Html Element using Selenium Webdriver

**Installation :**

`pip install Selenium-Screenshot`

This Package Support Python 3.6+ only

**How to Use :**

**For Full Page ScreenShot :**

```python
from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/tree/master/test"
driver.get(url)
img_url = ob.full_Screenshot(driver, save_path=r'.', image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()
```

**For Html Element Clipping :**

````python
from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
driver.get(url)

element = driver.find_element_by_class_name('signup-prompt')
img_url = ob.get_element(driver, element, r'.')
print(img_url)

driver.close()

driver.quit()

````

**For Html Element Clipping with Hiding Element :**

````python
from Screenshot import Screenshot
from selenium import webdriver

ob = Screenshot.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3"
driver.get(url)
Hide_elements = ['class=avatar width-full height-full avatar-before-user-status']  # Use full class name
img_url = ob.full_Screenshot(driver, save_path=r'.', elements=Hide_elements, image_name='Myimage.png')
print(img_url)
driver.close()

driver.quit()


````
**Limitation:**

- Screenshot can take only 10000 of height of website


**Contact Information :**

[Email:py.wizard.org@gmail.com](mailto::py.wizard.org@gmail.com)

**Donation :**

If you have found my softwares to be of any use to you, do consider helping me pay my internet bills. This would encourage me to create many such softwares.

<a href="https://www.paypal.me/sam4u3" target="_blank"><img src="https://raw.githubusercontent.com/aha999/DonateButtons/master/Paypal.png" alt="Donate via PayPal" title="Donate via PayPal" /></a>
