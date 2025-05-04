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