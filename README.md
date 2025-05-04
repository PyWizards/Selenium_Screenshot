[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

**Selenium Screenshot:**

[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/personalized-badge/selenium-screenshot?period=total&units=none&left_color=yellowgreen&right_color=blue&left_text=Downloads)](https://pepy.tech/project/selenium-screenshot)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PyPI version](https://badge.fury.io/py/Selenium-Screenshot.svg)](https://badge.fury.io/py/Selenium-Screenshot)
![Python package](https://github.com/sam4u3/Selenium_Screenshot/workflows/Python%20package/badge.svg)


The Selenium Screenshot is used to clip Html pages and elements using Selenium.

**Installation:**

`pip install Selenium-Screenshot`

This package supports Python 3.6+ only.

**How to Use:**

**For Full Page Screenshot:**

```python
from selenium import webdriver
from Screenshot import Screenshot

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Python")

ss = Screenshot(driver)

# Example: hide sticky header + specific table
table_to_hide = driver.find_element("css selector", "#p-search")

ss.capture_full_page(
    output_path="python_wiki.png",
    hide_selectors=[".vector-sticky-header", "#mw-head", table_to_hide]  # mix of CSS + WebElement
)

driver.quit()
```

**For Html Element Clipping:**

````python
from selenium import webdriver
from Screenshot import Screenshot

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Python")

ss = Screenshot(driver)

# Capture a specific box (e.g., infobox)
content_only = driver.find_element("css selector", "#mw-content-text")
ss.capture_element(content_only, "content_only.png")

driver.quit()

````

**Contact Information:**

[Email:py.wizard.org@gmail.com](mailto::py.wizard.org@gmail.com)

**Donation:**

If you have found my software to be of any use to you, do consider helping me pay my internet bills. This would encourage me to maintain and create more projects.

<a href="https://www.paypal.me/sam4u3" target="_blank"><img src="https://raw.githubusercontent.com/aha999/DonateButtons/master/Paypal.png" alt="Donate via PayPal" title="Donate via PayPal" /></a>
