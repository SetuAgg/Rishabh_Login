import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_page import Login_Admin_Page
import softest

class Test_01_Admin_Login(softest.TestCase):
    admin_page_url = "https://vriddhi-admin-dev.stackroute.io/"
    image_Xpath = "//img[@class='img img-responsive']"
    username = "aggarwalsetu.1@gmail.com"
    password = "12345678"
    invalid_username = "random@gmail.com"
    invalid_password = "87466"
    logger = Log_Maker.log_gen()
    class_forgot = "FP_BTN jb-link pt-2"

# Use if we use config.ini and read_properties file
#class Test_01_Admin_Login(softest.TestCase):

    #admin_page_url = Read_Config.get_admin_page_url()
    #image_Xpath = Read_Config.get_image_Xpath()

    #username = Read_Config.get_username()
    #password = Read_Config.get_password()
    #invalid_username = Read_Config.get_invalid_username()
    #invalid_password = Read_Config.get_invalid_password()
    #logger = Read_Config.get_logger()
    #class_forgot = Read_Config.get_class_forgot()




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
        return self.driver.find_element(By.XPATH, self.image_Xpath)
    def test_image_displayed(self,setup):
        global image_element
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        try:
            image_element = self.driver.find_element(By.XPATH, self.image_Xpath)
            assert image_element.is_displayed()
            self.logger.info("Image element is displayed")
            self.driver.save_screenshot(".\\screenshots\\test_image_element.png")
            return image_element.is_image_displayed() and image_element.get_attribute('src')

        except:
            self.logger.error("Image element is not displayed")
            self.driver.save_screenshot(".\\screenshots\\test_image_element.png")
            self.driver.quit()

        if image_element.test_image_displayed():
            self.logger.info("test image displayed")
            print("Image is displayed and its src attribute is:", image_element.get_image_element().get_attribute('src'))
            return self.driver.save_screenshot(".\\screenshots\\test_image_displayed.png")
        else:
            self.driver.save_screenshot(".\\screenshots\\_image_displayed.png")
            print("Image is not displayed or not found.")



    @pytest.mark.regression
    def test_valid_admin_login(self,setup):
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.admin_lp = Login_Admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self. password)
        self.admin_lp.click_login()
        actual_title = self.driver.title
        expected_title = "Admin - Vriddhi Admin"
        if actual_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.logger.info("test_title_verification")
            assert True
            self.driver.close()
        else:
            self.logger.info("test_title_verification")
            self.driver.save_screenshot(".\\screenshots\\test_title_verification.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_invalid_admin_login(self, setup):
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


    def email_verification(self, setup):
        self.logger.info("email_verification")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        self.driver.find_element(By.CLASS_NAME, self.class_forgot).click()
        text = self.driver.find_element(By.CLASS_NAME, self.class_forgot).text

        if text == "E-mail is not registered":
            self.driver.find_element(By.CLASS_NAME, self.class_forgot).click()
            self.logger.info("forgot_password_verification")
            self.driver.save_screenshot(".\\screenshots\\email_verification.png")
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\screenshots\\email_verification.png")
            self.driver.close()
            assert False


