import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():

    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    welcome_text = "//h3[@class='mb-3']"
    logout_text = "//div[@class='mb-2 login-msg']"
    main_heading_Xpath = "//h3[@class='leader_text']"
    program_text_xpath = "//h3[@class='program-head']"
    profile_dropdown_xpath = "//img[@style='width: 55px; height: 55px; border-radius: 50%;']"
    profile_dropdown_my_profile = "//div[@class='customHover']"
    my_profile_display = "//section[@class='profile-banner container']"
    profile_section_display = "//section[@class='container']"
    profile_dropdown_my_progress = "//div[@class='customHover my_progress_cursor']"
    profile_dropdown_certificates = "//div[@class='customHover']"
    certificate_text_display = "//div[@class='col-md-12 d-flex justify-content-between my--certificate--heading']"
    certificate_image_display = "//div[@id='MyCertificates']"
    profile_dropdown_learning_points = "//div[@class='customHover']"
    learning_points_text_display = "//div[@class='col-md-12 points-head-history']"
    profile_dropdown_my_programs = "//a[@class='customHover dropdown-item']"
    profile_dropdown_change_password = "//a[@class='customHover dropdown-item']"
    change_password_text_display = "//h3[@class='mb-3']"
    profile_dropdown_log_out = "//a[@class='customHover dropdown-item']"


    def __init__(self):
        self.lp = None
        self.driver = None

    def test_profile_bar_tab(self, setup):
        self.driver = setup
        self.logger.info("*******test_profile_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        profile_dropdown = self.driver.find_element(By.XPATH,self.profile_dropdown_xpath)
        self.lp.click_profile_dropdown()
        if profile_dropdown.is_displayed():
            self.logger.info("*******test_profile_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\test_profile_bar_tab.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_profile_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\test_profile_bar_tab.png")
            self.driver.close()
            assert False

    def test_my_profile_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_my_profile_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_my_profile()
        text = self.driver.find_element(By.XPATH,self.my_profile_display).text
        section = self.driver.find_element(By.XPATH,self.profile_section_display)
        if text.is_displayed():
            if text == "Profile":
                self.logger.info("*******test_my_profile_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_profile_btn.png")
                assert True
                self.driver.close()
            elif section.is_displayed():
                self.logger.info("*******test_my_profile_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_profile_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_my_profile_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_profile_btn.png")
            self.driver.close()
            assert False

    def test_my_progress_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_my_progress_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_my_progress()
        text = self.driver.find_element(By.XPATH,self.main_heading_Xpath).text
        if text.is_displayed():
            if text == "My Progress Status":
                self.logger.info("*******test_my_progress_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_progress_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_my_progress_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_progress_btn.png")
            self.driver.close()
            assert False

    def test_certificate_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_certificate_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_certificates()
        text = self.driver.find_element(By.XPATH,self.certificate_text_display).text
        image_display = self.driver.find_element(By.XPATH,self.certificate_image_display)
        if text.is_displayed():
            if text == "My Certificates":
                self.logger.info("*******test_certificate_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_certificate_btn.png")
                assert True
                self.driver.close()
            elif image_display.is_displayed():
                self.logger.info("*******test_certificate_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_certificate_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_certificate_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_certificate_btn.png")
            self.driver.close()
            assert False

    def test_learning_points_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_learning_points_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_learning_pointers()
        text = self.driver.find_element(By.XPATH,self.learning_points_text_display).text
        if text.is_displayed():
            if text == "1040 Learning Points":
                self.logger.info("*******test_learning_points_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_points_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_learning_points_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_points_btn.png")
            self.driver.close()
            assert False

    def test_my_programs_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_my_programs_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_my_programs_btn()
        text = self.driver.find_element(By.XPATH,self.program_text_xpath).text
        if text.is_displayed():
            if text == "Programs":
                self.logger.info("*******test_my_programs_btn******")
                self.driver.save_screenshot(".\\screenshots\\test_programs_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_my_programs_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_btn.png")
            self.driver.close()
            assert False

    def test_change_password_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_change_password_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_change_password()
        text = self.driver.find_element(By.XPATH,self.change_password_text_display).text
        if text.is_displayed():
            if text == "Change your Password":
                self.logger.info("*******test_change_password_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_password_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_change_password_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_password_btn.png")
            self.driver.close()
            assert False

    def test_logout_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_logout_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_profile_dropdown()
        self.lp.click_logout()
        text = self.driver.find_element(By.XPATH,self.welcome_text).text
        message = self.driver.find_element(By.XPATH,self.logout_text).text
        if text == "LOGIN":
            if message == "You have been logged out successfully.":
                self.logger.info("*******test_logout_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_welcome_text.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_logout_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_welcome_text.png")
            self.driver.close()
            assert False





























