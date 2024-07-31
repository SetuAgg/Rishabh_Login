import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_page import Login_Admin_Page
from utilities.read_properties import Read_Config
import softest

class Test_03_Admin_Login(softest.TestCase):
    admin_page_url = "https://vriddhi-admin-dev.stackroute.io/"
    username = "aggarwalsetu.1@gmail.com"
    logger = Log_Maker.log_gen()
    purpose_heading = "jb-h1 login-pass"
    ID_reset = "resetPss"

    #class Test_03_Admin_Login(softest.TestCase):
        #admin_page_url = Read_Config.get_admin_page_url()

        #username = Read_Config.get_username()
        #logger = Read_Config.get_logger()
        #page_purpose_heading = Read_Config.page_purpose_heading()
        #ID_reset = Read_Config.get_ID_reset()



    @pytest.mark.regression
    def test_title(self,setup):
        self.logger.info("test_title")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        expected_title = "Admin - Vriddhi Admin"
        if act_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\test_title.png")
            self.logger.info("test_title_verification")
            assert True
            self.driver.close()
        else:
            self.logger.info("test_title")
            self.driver.save_screenshot(".\\screenshots\\test_title.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def page_purpose_heading(self,setup):
        self.logger.info("page_purpose_heading")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        text = self.driver.find_element(By.CLASS_NAME, self.purpose_heading).text
        if text == "Forgot Password":
            self.driver.save_screenshot(".\\screenshots\\page_purpose_heading.png")
            self.logger.info("page_purpose_heading")
            self.driver.close()
            assert True
        else:
            self.logger.info("page_purpose_heading")
            self.driver.close()
            self.driver.save_screenshot(".\\screenshots\\page_purpose_heading.png")
            assert False


    @pytest.mark.regression
    def username_verification(self,setup):
        self.logger.info("username_verification")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.get(self.username)
        self.driver.find_element(By.ID, self. ID_reset).click()
        self.driver.save_screenshot(".\\screenshots\\username_verification.png")
        # Assuming you want to check if the username field is filled or correct
        username_element = self.driver.find_element(By.ID, "user_login")
        try:
            assert username_element.get_attribute("value") == self.username, "Username does not match"
            self.logger.info("username_verification passed")
        except AssertionError as e:
            self.logger.error("username_verification failed")
            raise e
        finally:
            self.driver.save_screenshot(".\\screenshots\\username_verification.png")
            self.driver.close()






