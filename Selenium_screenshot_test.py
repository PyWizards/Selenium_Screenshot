from Screenshot.Screenshot_Clipping import Screenshot
from selenium import webdriver



def test_IE():
    sc=Screenshot()
    object=webdriver.Ie(executable_path="IEDriverServer.exe")
    object.set_window_size(1200,768)
    url='https://github.com/sam4u3/Selenium_Screenshot'
    object.get(url)
    img_url=sc.full_Screenshot(object,save_path='.')
    print(img_url)
    object.close()
    object.quit()
