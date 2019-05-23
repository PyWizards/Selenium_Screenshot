import os
import time
import uuid

from PIL import Image


class Screenshot:
    """
       #================================================================================================================#
       #                                          Class: Screenshot                                                     #
       #                                    Purpose: Captured full and element screenshot using selenium                #
       #                                    a) Capture full webpage as image                                            #
       #                                    b) Capture element screenshots                                              #
       #================================================================================================================#
    """

    def __init__(self):
        """
        Usage:
            N/A
        Args:
            N/A
        Returns:
            N/A
        Raises:
            N/A
        """
        pass

    def full_Screenshot(self, driver, save_path='', image_name='selenium_full_screenshot.png', elements=None):
        """
        Usage:
            Capture full web page as a image
        Args:
            driver(str) : The path of chromedriver
            save_path(str) : The path where to save full screenshot
            image_name(str) : Name of image to be saved
            elements(list) : List of elements to be hide
        Returns:
            save_path (str) : The full path of saved image
        Raises:
            Element hide (Exception) : When class or id not specified to hide element

        """
        print("Starting chrome full page screenshot Capturing ...")
        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        rectangles = []

        self.hide_elements(driver, elements)

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
            file_name = "part_{0}.png".format(part)
            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])
            stitched_image.paste(screenshot, offset)
            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle
        save_path = save_path + '\\' + image_name
        stitched_image.save(save_path)
        print('Full Screenshot Image Saved at: ', save_path)
        return save_path

    def get_element(self, driver, element, save_location):
        """
         Usage:
             Capture Element screenshot as a image
         Args:
             driver(str) : The path of chromedriver
             element (Iwebelement) : The element on web page to be captured
             save_location (str) : Path where to save image
         Returns:
             img_url(str) : The path of image
         Raises:
             N/A
         """
        image = self.full_Screenshot(driver, save_path=save_location, image_name='clipping_shot.png')
        location = element.location
        size = element.size
        x = location['x']
        y = location['y']
        w = size['width']
        h = size['height']
        width = x + w
        height = y + h

        image_object = Image.open(image)
        image_object = image_object.crop((int(x), int(y), int(width), int(height)))
        uid = str(uuid.uuid4())
        img_url = save_location + r'\\' + uid + '.png'
        image_object.save(img_url)
        return img_url

    def hide_elements(self, driver, elements):
        """
         Usage:
             Hide elements from web page
         Args:
             driver(str) : The path of chromedriver
             elements (list) : The element on web page to be hide
         Returns:
             N/A
         Raises:
             N/A
         """
        if elements is not None:
            try:
                for e in elements:
                    sp_xpath = e.split('=')
                    if 'id=' in e.lower():
                        driver.execute_script(
                            "document.getElementById('{}').setAttribute('style', 'display:none;');".format(
                                sp_xpath[1]))
                    elif 'class=' in e.lower():
                        driver.execute_script(
                            "document.getElementsByClassName('{}')[0].setAttribute('style', 'display:none;');".format(
                                sp_xpath[1]))
                    else:
                        print('For Hiding Element works with ID and Class Selector only')
            except Exception as Error:
                print('Error : ', str(Error))
