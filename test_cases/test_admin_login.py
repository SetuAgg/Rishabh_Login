import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_page import Login_Admin_Page
from utilities.read_properties import Read_Config

class Test_01_Admin_Login:
    admin_page_url = "https://vriddhi-admin-dev.stackroute.io/"
    image_Xpath = "//img[@class='img img-responsive']"
    username = "aggarwalsetu.1@gmail.com"
    password = "12345678"
    invalid_username = "random@gmail.com"
    invalid_password = "87466"
    logger = Log_Maker.log_gen()

# Use if we use config.ini and read_properties file
#class Test_01_Admin_Login:
    #admin_page_url = Read_Config.get_admin_page_url()
    #image_Xpath = Read_Config.get_image_Xpath()
    #username = Read_Config.get_username()
    #password = Read_Config.get_password()
    #invalid_username = Read_Config.get_invalid_username()
    #invalid_password = Read_Config.get_invalid_password()
    #logger = Read_Config.get_logger()



    def test_title_verification(self,setup):
        self.logger.info(" Test_01_Admin_Login")
        self.logger.info("test_title_verification")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        expected_title = "Admin - Vriddhi Admin"
        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("test_title_verification")
            assert True
            self.driver.close()
        else:
            self.logger.info("test_title_verification")
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False


    def image_element(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        return self.find_element(By.XPATH, self.image_Xpath)
    def is_image_displayed(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        try:
            image_element = self.is_image_displayed()
            return image_element.is_image_displayed() and image_element.get_attribute('src')
            return self.driver.save_screenshot(".\\screenshots\\is_image_displayed.png")
        except:
            return False
        if admin_page_url.is_image_displayed():
            self.logger.info("is image displayed")
            print("Image is displayed and its src attribute is:", admin_page_url.get_image_element().get_attribute('src'))
            return self.driver.save_screenshot(".\\screenshots\\is_image_displayed.png")
        else:
            self.driver.save_screenshot(".\\screenshots\\is_image_displayed.png")
            print("Image is not displayed or not found.")



    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self. password)
        self.admin_lp.click_login()
        self.logger.info("test_valid_admin_login")
        self.driver.save_screenshot(".\\screenshots\\test_valid_admin_login.png")


    def test_invalid_admin_login(self,setup):
        self.logger.info("test_invalid_admin_login")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        error_message = self.driver.find_element(By.XPATH,"").text
        if error_message == "Sorry, you are not broker admin.":
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.logger.info("test_invalid_admin_login")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\test_invalid_admin_login.png")
            self.driver.close()
            assert False










