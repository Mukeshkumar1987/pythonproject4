import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec


class loginpage:
    Text_UserName_XPATH = (By.XPATH,"//input[@placeholder='Username']")
    Text_Password_XPATH = (By.XPATH,"//input[@placeholder='Password']")
    Click_Login_Button_XPATH = (By.XPATH,"//button[normalize-space()='Login']")
    Click_Menu_Button_XPATH = (By.XPATH,"//span[@class='oxd-userdropdown-tab']")
    Click_Logout_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")
    def __init__(self,driver):
        self.driver = driver
    def Enter_UserName(self,username):
        self.driver.find_element(*loginpage.Text_UserName_XPATH).send_keys(username)
    def Enter_Password(self,password):
        self.driver.find_element(*loginpage.Text_Password_XPATH).send_keys(password)
    def Click_Login(self):
        self.driver.find_element(*loginpage.Click_Login_Button_XPATH).click()
    def Click_MenuButton(self):
        self.driver.find_element(*loginpage.Click_Menu_Button_XPATH).click()
    def  Click_Logout(self):
        self.driver.find_element(*loginpage.Click_Logout_XPATH).click()
    def Login_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*loginpage.Click_Menu_Button_XPATH)
            return True
        except Ec:
            return False

#
# from selenium.webdriver.common.by import By
#
#
# class  loginpage:
#     Text_Username_XPATH = (By.XPATH,"//input[@placeholder='Username']")
#     Text_Password_XPATh = (By.XPATH,"//input[@placeholder='Password']")
#     Text_login_BUttom_XPATH = (By.XPATH,"//button[@type='submit']")
#     Click_Menu_Button_XAPTH = (By.XPATH,"//p[@class='oxd-userdropdown-name']")
#     CLick_logout_Button_XPATH = (By.XPATH,"//a[normalize-space()='Logout']")
#     def __init__(self,driver):
#         self.driver = driver
#     def Enter_userName(self,username):
#         self.driver.find_element(*loginpage.Text_Username_XPATH).send_keys(username)
#     def Enter_username(self,password):
#         self.driver.find_element(*loginpage.Text_Password_XPATh).send.keys(password)
#     def click_Login(self):
#         self.driver.find_element(*loginpage.Text_login_BUttom_XPATH)








