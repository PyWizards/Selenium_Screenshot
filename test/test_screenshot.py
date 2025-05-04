import os
import pytest
from selenium import webdriver
from Screenshot import Screenshot

TEST_URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get(TEST_URL)
    yield driver
    driver.quit()


def test_full_page_screenshot(driver, tmp_path):
    output_file = tmp_path / "full_page.png"
    ss = Screenshot(driver)
    ss.capture_full_page(str(output_file), hide_selectors=[".vector-sticky-header", "#mw-head"])

    assert output_file.exists()
    assert os.path.getsize(output_file) > 10_000  # ensure it's not empty


def test_element_screenshot(driver, tmp_path):
    output_file = tmp_path / "element.png"
    ss = Screenshot(driver)

    infobox = driver.find_element("css selector", ".infobox")
    ss.capture_element(infobox, str(output_file), padding=5)

    assert output_file.exists()
    assert os.path.getsize(output_file) > 5_000  # basic size check