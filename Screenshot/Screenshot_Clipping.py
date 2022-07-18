import os
import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


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

    @staticmethod
    # Take temporary screenshot of the web page to get the size of the image
    def __get_screen_size(driver: WebDriver) -> dict:
        driver.get_screenshot_as_file('screenshot.png')
        image = Image.open('screenshot.png')
        width, height = image.size

        return {'width': width, 'height': height}

    def full_Screenshot(self, driver: WebDriver, save_path: str = '', image_name: str = 'selenium_full_screenshot.png',
                        elements: list = None, is_load_at_runtime: bool = False, load_wait_time: int = 5, multi_images: bool = False) -> str:
        """
        Take full screenshot of web page
        Args:
            driver: The Selenium web driver object
            save_path: The path where to store screenshot
            image_name: The name of screenshot image
            elements: List of Xpath of elements to hide from web pages
            is_load_at_runtime: Page Load at runtime
            load_wait_time: The Wait time while loading full screen
            multi_images: The flag is uses to capture multiple images and create single image in vertical format

        Returns:
            str : The path of image
        """
        image_name = os.path.abspath(save_path + '/' + image_name)

        final_page_height = 0
        original_size = driver.get_window_size()

        if is_load_at_runtime:
            while True:
                page_height = driver.execute_script("return document.body.scrollHeight")
                if page_height != final_page_height and final_page_height <= 10000:
                    driver.execute_script("window.scrollTo(0, {})".format(page_height))
                    time.sleep(load_wait_time)
                    final_page_height = page_height
                else:
                    break

        if isinstance(driver, webdriver.Ie):
            self.hide_elements(driver, elements)
            required_width = driver.execute_script('return document.body.parentNode.scrollWidth')
            driver.set_window_size(required_width, final_page_height)
            driver.save_screenshot(image_name)
            driver.set_window_size(original_size['width'], original_size['height'])
            return image_name

        else:
            total_width = driver.execute_script("return document.body.offsetWidth")
            total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
            viewport_width = driver.execute_script("return document.body.clientWidth")
            viewport_height = driver.execute_script("return window.innerHeight")
            driver.execute_script("window.scrollTo(0, 0)")
            time.sleep(2)
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
                    rectangles.append((ii, i, top_width, top_height))
                    ii = ii + viewport_width
                i = i + viewport_height
            stitched_image = None
            previous = None
            part = 0

            # This value indicates if is the first part of the screenshot, or it is the rest of the screenshot
            init_canvas = True
            # Get the screenshot and save the dimensions of the image, this will be useful for create a
            # correct canvas with correct dimensions
            # and not show images with a wrong size or cut
            size_screenshot = self.__get_screen_size(driver)
            # Get temporary sum of height of the total pages
            height_canvas = size_screenshot['height'] * len(rectangles)

            # Compare if the screenshot it's only one part and assign the correct dimensions of the screenshot size
            # Or assign the height of the total screenshot
            if multi_images:
                # Assign the height of the total screenshot at canvas even if not used at the moment
                stitched_image = Image.new('RGB', (size_screenshot['width'], height_canvas))
            else:
                # Assign the dimensions corresponding to the size of the uniq screenshot
                stitched_image = Image.new('RGB', (size_screenshot['width'], size_screenshot['height']))

            # This constant is used top offset the image in the canvas
            jump = round(size_screenshot['height'] / 2)
            # With take multiple screenshots this value is used to adjust the position of the image in the canvas
            # This value know update every time the screenshot is taken
            top_offset = jump

            for rectangle in rectangles:
                if previous is not None:
                    driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                    time.sleep(1)
                    self.hide_elements(driver, elements)

                file_name = "part_{0}.png".format(part)
                driver.get_screenshot_as_file(file_name)
                screenshot = Image.open(file_name)

                if rectangle[1] + viewport_height > total_height:
                    offset = (rectangle[0], rectangle[1] + top_offset)
                else:
                    if init_canvas:
                        offset = (rectangle[0], rectangle[1])
                        init_canvas = False
                    else:
                        offset = (rectangle[0], rectangle[1] + top_offset)
                        top_offset = jump + top_offset

                stitched_image.paste(screenshot, offset)
                del screenshot
                os.remove(file_name)
                part = part + 1
                previous = rectangle
            save_path = os.path.abspath(os.path.join(save_path, image_name))
            stitched_image.save(save_path)
            return save_path

    def get_element(self, driver: WebDriver, element: WebElement, save_location: str, image_name: str = 'cropped_screenshot.png', to_hide: list = None) -> str:
        """
         Usage:
             Capture Element screenshot as a image
         Args:
             driver: Web driver instance
             element : The element on web page to be captured
             save_location  : Path where to save image
         Returns:
             img_url(str) : The path of image
         Raises:
             N/A
         """
        image = self.full_Screenshot(driver, save_path=save_location, image_name='clipping_shot.png', elements=to_hide, multi_images=True)
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
        img_url = os.path.abspath(os.path.join(save_location, f"{image_name}.png"))
        image_object.save(img_url)
        return img_url

    @staticmethod
    def hide_elements(driver: WebDriver, elements: list) -> None:
        """
         Usage:
             Hide elements from web page
         Args:
             driver : The path of chromedriver
             elements : The element on web page to be hide
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
