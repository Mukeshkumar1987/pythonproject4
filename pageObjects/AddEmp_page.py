from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException as Ec
import time

class AddEmployee:
    Click_PIM_XPATH = (By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='PIM']")
    CLick_Add_Button_XPATH = (By.XPATH,"//i[@class='oxd-icon bi-plus oxd-button-icon']")
    Text_First_Name_XPATH = (By.XPATH,"//input[@placeholder='First Name']")
    Text_MIddle_Name_XPATH = (By.XPATH,"//input[@placeholder='Middle Name']")
    Text_Last_Name_XPATH = (By.XPATH,"//input[@placeholder='Last Name']")
    Click_Save_button_XPATH = (By.XPATH,"//button[@type='submit']")
    Personal_detail_XPATH = (By.XPATH,"//h6[normalize-space()='Personal Details']")
    Click_Add_Emp_XPATH = (By.XPATH,"//a[normalize-space()='Add Employee']")
    def __init__(self,driver):
        self.driver = driver
    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_XPATH).click()
    def Click_Add(self):
        self.driver.find_element(*AddEmployee.CLick_Add_Button_XPATH).click()
    def Enter_First_Name(self,firstName):
        self.driver.find_element(*AddEmployee.Text_First_Name_XPATH).send_keys(firstName)
    def Enter_Middle_Name(self,middlename):
        self.driver.find_element(*AddEmployee.Text_MIddle_Name_XPATH).send_keys(middlename)
    def Enter_Last_Name(self,lastname):
        self.driver.find_element(*AddEmployee.Text_Last_Name_XPATH).send_keys(lastname)
    def Click_Save(self):
        self.driver.find_element(*AddEmployee.Click_Save_button_XPATH).click()

    def Click_AddEmployee(self):
        self.driver.find_element(*AddEmployee.Click_Add_Emp_XPATH).click()

    def Add_Employee_status(self):
        self.driver.implicitly_wait(10)

        try:
            self.driver.find_element(*AddEmployee.Personal_detail_XPATH)
            return True
        except Ec:
            return False


#
#
#
#
#
#
