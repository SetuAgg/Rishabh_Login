import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_page import Login_Admin_Page
from utilities.read_properties import Read_Config
from utilities import excel_utils
import time

#class Test_02_Admin_Login_data_driven:
    #admin_page_url = "https://vriddhi-admin-dev.stackroute.io/"
    #image_Xpath = "//img[@class='img img-responsive']"
    #path = ".//test_data//login_admin_data.xlsx"
    #logger = Log_Maker.log_gen()
    #status_list = []

#Use if we use config.ini and read_properties file
class Test_02_Admin_Login:
    admin_page_url = Read_Config.get_admin_page_url()
    image_Xpath = Read_Config.get_image_Xpath()
    path = ".//test_data//login_admin_data.xlsx"
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    invalid_password = Read_Config.get_invalid_password()
    logger = Read_Config.get_logger()


    def test_valid_admin_login_data_driven(self,setup):
        self.logger.info("***test_valid_admin_login_data_driven***")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)

        self.rows = excel_utils.get_row_count(self.path,"Sheet1")
        print( "number of rows",self.rows)

        for r in range(2,self.rows+1):
            self.username = excel_utils.read_data(self.path,"Sheet1",r,1)
            self.password = excel_utils.read_data(self.path,"Sheet1",r,2)
            self.expected_login = excel_utils.read_data(self.path,"Sheet1",r,3)
            self.admin_lp.enter_username(self.username)
            self.admin_lp.enter_password(self.password)
            self.admin_lp.click_login()
            time.sleep(5)

            if self.expected_login == "Yes":
                self.logger.info("test data is passed")
                self.status_list.append("Pass")
            elif self.expected_login == "No":
                self.logger.info("test data is NOT passed")
                self.status_list.append("Fail")

        print("Status List is",self.status_list)
        if "Fail" in self.status_list:
            self.logger.error("Test data failed")
            assert False
        else:
            self.logger.info("Test data passed")
            assert True

        self.admin_lp.click_login()
        self.logger.info("test_valid_admin_login_data_driven")
        self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login_data_driven.png")















