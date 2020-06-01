
from Screenshot import Screenshot_Clipping
from selenium import webdriver
import time

wd = webdriver.Chrome()

url = 'https://cn.bing.com/search?q=Selenium-Screenshot+github&qs=n&form=QBLHCN&sp=-1&pq=selenium-screenshot+git&sc=0-23&sk=&cvid=E4B25D5FBD7F471E8BDDF8ECBD1DED94'
wd.implicitly_wait(10)
wd.get(url)

ob=Screenshot_Clipping.Screenshot()
img_url=ob.full_Screenshot(wd, save_path=r'.', image_name='Myimage.png')
print(img_url)
wd.close()
wd.quit()