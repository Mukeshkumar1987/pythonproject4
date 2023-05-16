
import time
import pytest

from selenium import webdriver

from selenium.common import NoSuchElementException as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.Loginpage import loginpage
from utilites.Logger import LogGenerator
from utilites.Readproperties import Readconfig


# #
class Test_Login:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "C:\\Users\\mukes\\PycharmProjects\\Orange hrm project\\Logs\\Orangehrm_Automation.log"

    @pytest.mark.sanity


    def test_Page_Title_001(self,setup):
        self.driver = setup
        self.log.info("test_Page_Title_001 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is-->" + self.driver.title)
        else:
            assert False
            self.log.info("test_Page_Title_001 is Failed")
        self.driver.close()
        self.log.info("test_Page_Title_001 is completed")

    @pytest.mark.sanity

    def test_login_002(self,setup):
        self.driver = setup
        self.log.info("test_login_002 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)

        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.Click_Login()
        if self.lp.Login_Status()==True:
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Orange hrm\\ScreenShots\\test_login_002-pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu button")
            self.lp.Click_Logout()
            self.log.info("Click on logout button")
            self.log.info("test_login_002 is Passed")
            assert True
        else:
            self.log.info("test_login_002 is Failed")
            self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Orange hrm\\ScreenShots\\test_login_002-fail.png")


            assert False
        self.driver.close()
        self.log.info("test_login_002 is Completed")























