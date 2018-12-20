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

**For Html Element Clipping with Hiding Element :**

````python
from Screenshot import Screenshot_Clipping
from selenium import webdriver
import os

ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565098%2Cn%3A13896603011&bbn=16225007011&ie=UTF8&qid=1545303779&rnid=565098&ajr=3"
driver.get(url)
dir_path = os.path.dirname(os.path.realpath(__file__))
Hide_elements=['id=leftNavContainer']
img_url=ob.Full_Scrrenshot(driver,r'E:\Sayar_python\Selenium\test',Hide_elements)
print(img_url)

driver.close()

driver.quit()
````



**Contact Information :**

[Email: sayarmendis26@gmail.com](mailto::sayarmendis26@gmail.com)

