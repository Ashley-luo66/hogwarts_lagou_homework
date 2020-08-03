from appium import webdriver


class AddMember:

    def setup(self):
        self.driver = webdriver.Remote()