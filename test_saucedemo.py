import os,pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from saucedemo_obj import SauPage
url = "https://www.saucedemo.com/"
@pytest.fixture
def driver():
    driver_path = os.path.join(os.path.dirname(__file__),'msedgedriver.exe')
    service = Service(driver_path)
    driver = webdriver.Edge(service=service)
    driver.set_page_load_timeout(20)
    yield driver
    driver.quit()
def test_login_add_item(driver):
    element = SauPage(driver)
    element.open(url)
    element.login("standard_user","secret_sauce")
    products = element.products().text
    assert products == "Products",f"登录失败，未找到正确标题：{procucts}"
    shopp_car = element.shopp_car().text
    print(shopp_car)
    element.add_item().click()
    after_items = element.shopp_car().text
    print(after_items)
    assert after_items == "1",f"{after_items}"
    
