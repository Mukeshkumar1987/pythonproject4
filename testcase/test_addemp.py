import pytest
import time

from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By

from pageObjects.AddEmp_page import AddEmployee
from pageObjects.Loginpage import loginpage
from utilites.Logger import LogGenerator
from utilites.Readproperties import Readconfig


class Test_Add_Emp:
  Url = Readconfig.geturl()
  username = Readconfig.getusername()
  password = Readconfig.getpassword()
  log = LogGenerator.loggen()


  def test_addEmp_003(self,setup):
      self.log.info("test_addEmp_003 is started")
      self.driver = setup
      self.log.info("Opening Browser")
      self.driver.get(self.Url)
      self.log.info("Going to Url-->" + self.Url)
      self.lp = loginpage(self.driver)
      self.lp.Enter_UserName(self.username)
      self.log.info("Entering UserName-->" + self.username)
      self.lp.Enter_Password(self.password)
      self.log.info("Entering password-->" + self.password)
      self.lp.Click_Login()
      self.log.info("Click On login")
      self.ae = AddEmployee(self.driver)
      self.ae.Click_PIM()
      self.log.info("Click On PIM")
      self.ae.Click_Add()
      self.log.info("Click On Add")
      self.ae.Enter_First_Name("Credense")
      self.log.info("Entering FirstName")
      self.ae.Enter_Middle_Name("IT")
      self.log.info("Entering MiddleName")
      self.ae.Enter_Last_Name("Pune")
      self.log.info("Entering LastName")
      time.sleep(2)
      self.ae.Click_Save()
      self.log.info("Click on Save")
      if self.ae.Add_Employee_status()==True:
          self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Orange hrm project\\test_addemp_003-pass.png")
          # time.sleep(2)
          self.lp.Click_MenuButton()
          self.log.info("Click on MenuButton")
          self.lp.Click_Logout()
          self.log.info("Click on Logout Button")
          assert True

      else:
          self.driver.save_screenshot("C:\\Users\\mukes\\PycharmProjects\\Orange hrm project\\test_addemp_003-fail.png")
          self.log.info("test_addEmp_003 is Failed")
          assert False
      self.driver.close()
      self.log.info("test_addEmp_003 is Completed")


