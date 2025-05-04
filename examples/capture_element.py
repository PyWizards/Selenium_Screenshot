from selenium import webdriver
from Screenshot import Screenshot

driver = webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/Python")

ss = Screenshot(driver)

# Capture a specific box (e.g., infobox)
content_only = driver.find_element("css selector", "#mw-content-text")
ss.capture_element(content_only, "content_only.png")

driver.quit()