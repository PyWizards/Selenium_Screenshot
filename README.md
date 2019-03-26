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
url = "https://github.com/sam4u3/Selenium_Screenshot/blob/master/Screenshot/Screenshot_Clipping.py"
driver.get(url)
img_url=ob.Full_Scrrenshot(driver,r'C:\Users\Admin\Downloads','Myimage.png')
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
img_url=ob.Get_element(driver,element,r'C:\Users\Admin\Downloads')
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
url = "https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565098%2Cn%3A13896603011&bbn=16225007011&ie=UTF8&qid=1545303779&rnid=565098&ajr=3"
driver.get(url)
Hide_elements=['id=leftNavContainer']
img_url=ob.Full_Scrrenshot(driver,r'C:\Users\Admin\Downloads',Hide_elements,'Myimage.png')
print(img_url)
# print(url)
driver.close()

driver.quit()


````

**Contact Information :**

[Email: sayarmendis26@gmail.com](mailto::sayarmendis26@gmail.com)

