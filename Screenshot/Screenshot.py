import time
import base64
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

class Screenshot:
    def __init__(self, driver: webdriver.Chrome, scroll_pause: float = 0.3):
        self.driver = driver
        self.scroll_pause = scroll_pause

    def hide_elements(self, elements_or_selectors):
        """Hide elements via CSS selector or WebElement objects."""
        if not elements_or_selectors:
            return

        for item in elements_or_selectors:
            if isinstance(item, str):
                # Hide by CSS selector
                self.driver.execute_script(f"""
                        document.querySelectorAll("{item}").forEach(el => {{
                            el.style.display = "none";
                        }});
                    """)
            elif isinstance(item, WebElement):
                # Hide specific element directly
                self.driver.execute_script("""
                        arguments[0].style.display = "none";
                    """, item)

    def _scroll_to_bottom(self):
        last_height = 0
        while True:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(self.scroll_pause)
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def _get_page_dimensions(self):
        width = self.driver.execute_script("return Math.max(document.body.scrollWidth, document.documentElement.scrollWidth);")
        height = self.driver.execute_script("return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);")
        return width, height

    def capture_full_page(self, output_path="screenshot.png", hide_selectors=None):
        if hide_selectors is None:
            hide_selectors = ["#mw-head", "#mw-panel", ".vector-sticky-header"]
        self.hide_elements(hide_selectors)
        self._scroll_to_bottom()

        width, height = self._get_page_dimensions()

        # Force the viewport size using Chrome DevTools Protocol
        self.driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": width,
            "height": height,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        time.sleep(0.5)

        # Take screenshot using CDP
        screenshot_data = self.driver.execute_cdp_cmd("Page.captureScreenshot", {
            "format": "png",
            "fromSurface": True,
            "captureBeyondViewport": True
        })

        # Decode and save
        image_data = base64.b64decode(screenshot_data['data'])
        image = Image.open(BytesIO(image_data))
        image.save(output_path)

        print(f"[✓] Full-page screenshot saved to: {output_path}")

    def capture_element(self, element: WebElement, output_path="element.png", padding=0):
        """Capture full-width screenshot of a specific element using full-page technique."""
        # Ensure lazy content is loaded
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(self.scroll_pause)

        # Get page size and set viewport to full page (CDP method)
        total_width = self.driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.documentElement.scrollWidth);")
        total_height = self.driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.documentElement.scrollHeight);")

        self.driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": total_width,
            "height": total_height,
            "deviceScaleFactor": 1,
            "mobile": False
        })
        time.sleep(0.5)

        # Take full screenshot using CDP
        screenshot_data = self.driver.execute_cdp_cmd("Page.captureScreenshot", {
            "format": "png",
            "fromSurface": True,
            "captureBeyondViewport": True
        })
        png_data = base64.b64decode(screenshot_data['data'])
        image = Image.open(BytesIO(png_data))

        # Get element position
        location = element.location_once_scrolled_into_view
        size = element.size

        left = int(location['x']) - padding
        top = int(location['y']) - padding
        right = int(location['x'] + size['width']) + padding
        bottom = int(location['y'] + size['height']) + padding

        cropped = image.crop((left, top, right, bottom))
        cropped.save(output_path)
        print(f"[✓] Element screenshot saved to: {output_path}")