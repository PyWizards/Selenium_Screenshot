from Screenshot import Screenshot_Clipping
from selenium import webdriver
import os

ob=Screenshot_Clipping.Screenshot()
driver = webdriver.Chrome()
url = "https://www.amazon.com/s/ref=sr_nr_n_0?fst=as%3Aoff&rh=n%3A16225007011%2Cn%3A13896617011%2Cn%3A565098%2Cn%3A13896603011&bbn=16225007011&ie=UTF8&qid=1545303779&rnid=565098&ajr=3"
driver.get(url)
dir_path = os.path.dirname(os.path.realpath(__file__))
# element=driver.find_element_by_class_name('pagehead-actions')
# img_url=ob.Get_element(driver,element,r'E:\Sayar_python\Selenium\test')
img_url=ob.Full_Scrrenshot(driver,r'E:\Sayar_python\Selenium\test',['id=leftNavContainer'])
print(img_url)

driver.close()

driver.quit()