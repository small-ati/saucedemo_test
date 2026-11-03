from selenium.webdriver.edge.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class SauPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,20)
        self.username_loc = (By.ID,'user-name')
        self.password_loc = (By.ID,"password")
        self.login_button_loc = (By.ID,"login-button")
    def open(self,url):
        self.driver.get(url)
    #不知道要不要加return

    def login(self,username,password):
        #登录
        username_box = self.wait.until(EC.presence_of_element_located(self.username_loc))
        username_box.clear()
        username_box.send_keys(username)
        password_box = self.wait.until(EC.presence_of_element_located(self.password_loc))
        password_box.clear()
        password_box.send_keys(password)
        login = self.wait.until(EC.presence_of_element_located(self.login_button_loc)).click()

    def add_item(self):
        add_item_button = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')))
        return add_item_button
    def products (self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="header_container"]/div[2]/span')))
    def shopp_car(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="shopping_cart_container"]/a')))
