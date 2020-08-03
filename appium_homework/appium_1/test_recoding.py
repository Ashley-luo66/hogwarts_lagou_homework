from appium import webdriver


class TestRecoing :

    def setup(self) :
        command_executor = "http://127.0.0.1:4723/wd/hub"
        desired_capabilities = {"platformName" : "android",
                                "deviceName" : "464f47524e4f3098",
                                # "deviceName" : "SS2LHMC780904373",
                                "appPackage" : "com.tencent.wework",
                                "appActivity" : ".launch.WwMainActivity",
                                "automationName" : "UiAutomator2",
                                "autoGrantPermissions" : "true",
                                "noReset" : "true"
                                }
        self.driver = webdriver.Remote(command_executor=command_executor, desired_capabilities=desired_capabilities)
        self.driver.implicitly_wait(8)

    def test_case(self) :
        el1 = self.driver.find_element_by_id("com.tencent.wework:id/hib")
        el1.click()
        el2 = self.driver.find_element_by_id("com.tencent.wework:id/g5b")
        el2.send_keys("test11")
        el2.click()
        el3 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.RelativeLayout[1]/android.widget.RelativeLayout")
        el3.click()
        el4 = self.driver.find_element_by_id("com.tencent.wework:id/ea7")
        el4.send_keys("测试code")
        el5 = self.driver.find_element_by_id("com.tencent.wework:id/ea3")
        el5.click()

    def teardown(self) :
        self.driver.quit()
