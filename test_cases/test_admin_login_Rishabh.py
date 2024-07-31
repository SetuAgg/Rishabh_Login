import pytest
from selenium.webdriver.common.by import By

from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page


class Rishabh_Test_01_Login_Admin:
    page_url = Read_Config.get_page()
    image_Xpath = Read_Config.get_image_url()
    user_name = Read_Config.username()
    pass_word = Read_Config.password()
    invalid_username = Read_Config.invalid_username()
    invalid_password = Read_Config.invalid_password()
    logger = Log_Maker.log_gen()
    logo_X_path = Read_Config.get_logo()
    welcome_text = Read_Config.get_welcome_messages()


    @pytest.mark.regression
    def test_Rishabh_title_verification(self, setup):
        self.driver = setup
        self.logger.info("*******test_Rishabh_title_verification*******")
        self.driver.get(self.page_url)
        actual_title = self.driver.title
        expected_title = "RishabhSoft"
        if actual_title == expected_title:
            self.driver.save_screenshot(".\\screenshots\\test_Rishabh_title_verification.png")
            self.logger.info("*******test_Rishabh_title_verification*******")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_Rishabh_title_verification********")
            self.driver.save_screenshot(".\\screenshots\\test_Rishabh_title_verification.png")
            self.driver.close()
            assert False


    @pytest.mark.regression
    def test_welcome_test(self, setup):
        self.driver = setup
        self.logger.info("*******test_welcome_test*******")
        self.driver.get(self.page_url)
        self.lp = Rishabh_Login_Page(self.driver)
        text = self.driver.find_element(By.XPATH, self.welcome_text).text
        if text == "LOGIN":
            self.logger.info("*******test_welcome_test********")
            self.driver.save_screenshot(".\\screenshots\\welcome_text.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_welcome_test********")
            self.driver.save_screenshot(".\\screenshots\\welcome_text.png")
            self.driver.close()
            assert False




    @pytest.mark.regression
    def test_Rishabh_valid_admin_login(self, setup):
            self.driver = setup
            self.logger.info("*******test_Rishabh_valid_admin_login*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            self.lp.enter_username(self.user_name)
            self.lp.enter_password(self.pass_word)
            self.lp.click_login_button()
            self.logger.info("*******test_Rishabh_valid_admin_login*******")
            self.driver.save_screenshot(".\\screenshots\\test_Rishabh_valid_admin_login.png")


    @pytest.mark.regression
    def test_Rishabh_invalid_admin_login_username(self, setup):
            self.driver = setup
            self.logger.info("*******test_Rishabh_invalid_admin_login_username*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            self.lp.enter_username(self.invalid_username)
            self.lp.enter_password(self.pass_word)
            self.lp.click_login_button()
            error = self.driver.find_element(By.XPATH,"//div[@style='color: red; --darkreader-inline-color: #ff1a1a;']").text
            if error == "Invalid Email Or Password":
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_invalid_admin_login_username.png")
                self.logger.info("*******test_Rishabh_invalid_admin_login_username*******")
                assert True
                self.driver.close()

            else:
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_invalid_admin_login_username.png")
                self.logger.info("*******test_Rishabh_invalid_admin_login_username*******")
                self.driver.close()
                assert False


    @pytest.mark.regression
    def test_Rishabh_invalid_admin_login_password(self, setup):
            self.driver = setup
            self.logger.info("*******test_Rishabh_invalid_admin_login_password*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            self.lp.enter_username(self.user_name)
            self.lp.enter_password(self.invalid_password)
            self.lp.click_login_button()
            error = self.driver.find_element(By.XPATH,"//div[@style='color: red; --darkreader-inline-color: #ff1a1a;']").text
            if error == "Invalid Email Or Password":
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_invalid_admin_login_password.png")
                self.logger.info("*******test_Rishabh_invalid_admin_login_password*******")
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_invalid_admin_login_password.png")
                self.logger.info("*******test_Rishabh_invalid_admin_login_password*******")
                self.driver.close()
                assert False

    @pytest.mark.regression
    def test_Rishabh_invalid_admin_login_both(self, setup):
            self.driver = setup
            self.logger.info("*******test_Rishabh_invalid_admin_login_both*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            self.lp.enter_username(self.invalid_username)
            self.lp.enter_password(self.invalid_password)
            self.lp.click_login_button()
            error = self.driver.find_element(By.XPATH,"//div[@style='color: red; --darkreader-inline-color: #ff1a1a;']").text
            if error == "Invalid Email Or Password":
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_invalid_admin_login_both.png")
                self.logger.info("*******test_Rishabh_invalid_admin_login_both*******")
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_invalid_admin_login_both.png")
                self.logger.info("*******test_Rishabh_invalid_admin_login_both*******")
                self.driver.close()
                assert False


    @pytest.mark.regression
    def test_Rishabh_admin_login_logo_verification(self, setup):
            self.driver = setup
            self.logger.info("*******test_Rishabh_admin_login_logo_verification*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            logo_element = self.driver.find_element(By.XPATH,self.logo_X_path)
            if logo_element.is_displayed():
                self.logger.info("*******test_Rishabh_admin_login_logo_verification_passed*******")
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_admin_login_logo_verification.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_Rishabh_admin_login_logo_verification_failed******")
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_admin_login_logo_verification.png")
                self.driver.close()
                assert False




    @pytest.mark.regression
    def test_Rishabh_admin_login_image_verification(self, setup):
            self.driver = setup
            self.logger.info("*******test_Rishabh_admin_login_image_verification*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            image_element = self.driver.find_element(By.XPATH,self.image_Xpath)
            if image_element.is_displayed():
                self.logger.info("*******test_Rishabh_admin_login_image_verification_passed*******")
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_admin_login_image_verification.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_Rishabh_admin_login_image_verification_failed*******")
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_admin_login_image_verification.png")
                self.driver.close()
                assert False



    @pytest.mark.regression
    def test_valid_Rishabh_login_both(self, setup):
            self.driver = setup
            self.logger.info("*******test_valid_Rishabh_login_both*******")
            self.driver.get(self.page_url)
            self.lp = Rishabh_Login_Page(self.driver)
            self.lp.enter_username(self.user_name)
            self.lp.enter_password(self.pass_word)
            self.lp.click_login_button()
            dash_identity = self.driver.find_element(By.XPATH,"//h3[@class='leader_text']")
            if dash_identity == "My Progress Status":
                self.logger.info("*******test_valid_Rishabh_login_both*******")
                self.driver.save_screenshot(".\\screenshots\\test_Rishabh_login_both.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_valid_Rishabh_login_both*******")
                self.driver.close()
                assert False



















































