# @date 时间 2020/8/2 16:10
# @developer 开发者：Ashley @email luoyuhong1996@163.com
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver


class BasePage:

    def __init__(self,driver:WebDriver = None):
        if driver is None:
            self._driver = driver
            chrome_options = webdriver.ChromeOptions()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(chrome_options=chrome_options,executable_path="D:\\selenium\\chromedriver.exe")
            self._driver.get("https://work.weixin.qq.com/wework_admin/frame")
        else:
            self._driver = driver
        self._driver.implicitly_wait(5)

    def find(self,locator,value=None):
        return self._driver.find_element(*locator) if isinstance(locator,tuple) else self._driver.find_element(locator,value)

    def finds(self,locator,value=None):
        return self._driver.find_elements(*locator) if isinstance(locator,tuple) else self._driver.find_elements(locator,value)

    def send_keys(self,locator,value=None,keywords=None):
        return self.find(locator,value).send_keys(keywords)