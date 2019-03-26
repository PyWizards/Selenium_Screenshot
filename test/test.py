# from Screenshot import Screenshot_Clipping
# from selenium import webdriver
# import os


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