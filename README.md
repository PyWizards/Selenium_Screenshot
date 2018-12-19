**Slenium Screenshot :**

The Selenium Screenshot is used to clipped Html Element usinf Selenium Webdriver

**Installations :**

`pip install Selenium-Screenshot`

This Package Supported for Python 3.*

**How to Use :** 

**For Full Page ScreenShot :**
```python
from Screenshot import Screenshot_Clipping
from selenium import webdriver

Scr=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot"
driver.get(url)
img_url=Scr.Full_Scrrenshot(driver,r'E:\Sayar_python\Selenium\test')
print(img_url)

driver.close()

driver.quit()
```

**For Html Element Clipping :**

````python
from Screenshot import Screenshot_Clipping
from selenium import webdriver

Scr=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://github.com/sam4u3/Selenium_Screenshot"
driver.get(url)
element=driver.find_element_by_class_name('pagehead-actions')
img_url=Scr.Get_element(driver,element,r'E:\Sayar_python\Selenium\test')
print(img_url)

driver.close()

driver.quit()
````





**Contact Information :**

[Email: sayarmendis26@gmail.com](mailto::sayarmendis26@gmail.com)

