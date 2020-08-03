from appium import webdriver


class AddMember :

    def setup(self) :
        command_executor= ""
        desired_capabilities = {}
        self.driver = webdriver.Remote(command_executor=command_executor,desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(8)
