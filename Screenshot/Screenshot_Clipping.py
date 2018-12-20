import uuid
import os
import time
from PIL import Image


class Screenshot:
    def __init__(self):
        pass


    def Full_Scrrenshot(self,driver,filename,elements=None):

        print("Starting chrome full page screenshot workaround ...")

        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                # print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                time.sleep(3)
                try:
                    for e in elements:
                        sp_xpath=e.split('=')
                        if 'id' in e.lower():
                            driver.execute_script("document.getElementById('{}').setAttribute('style', 'display:none;');".format(sp_xpath[1]))
                        elif 'class' in e.lower():
                            driver.execute_script("document.getElementByClassName('{}').setAttribute('style', 'display:none;');".format(sp_xpath[1]))
                        else:
                            print('For Hiding Element works with ID and Class Selector only')
                except Exception as E:
                    pass
            file_name = "part_{0}.png".format(part)
            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            # print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        filename=filename+'\\'+'selenium_shot.png'
        stitched_image.save(filename)
        # print("Finishing chrome full page screenshot workaround...")
        print('Full Screenshot Image Saved at: ',filename)
        return filename

    def Get_element(self,driver,element,Save_loc):
        image=self.Full_Scrrenshot(driver,Save_loc)
        location = element.location
        size = element.size
        x = location['x']
        y = location['y']
        w = size['width']
        h = size['height']
        width = x + w
        height = y + h

        im = Image.open(image)
        im = im.crop((int(x), int(y), int(width), int(height)))
        uId = str(uuid.uuid4())
        Img_URl = Save_loc+r'\\' + uId + '.png'
        im.save(Img_URl)
        return Img_URl