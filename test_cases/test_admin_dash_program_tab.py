import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():
    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    programs_tab_xpath = "//a[@class='nav-link eureka_header_li active_status_color']"
    program_text_xpath = "//h3[@class='program-head']"
    programs_not_started_button = "//button[@class=' active nav-link']"
    not_started_button_display = "//img[@alt='Not Found']"
    programs_started_button = "//button[@id='profile-tab']"
    started_button_display = "//img[@alt='Not Found']"

    programs_completed_button = "//button[@id='messages-tab']"
    completed_button_display = "//div[@class='accordion_border']"
    completed_button_block_heading = "//div[@class='accordion-header']"
    completed_button_block_button = "//div[@class='accordion-button']"
    completed_button_block_category = "//div[@class='program_category']"
    completed_button_block_report_view = "//div[@aria-hidden='true']"


    def test_dashboard_program_tab(self,setup):
        self.driver = setup
        self.logger.info("*******test_dashboard_program_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        program_tab = self.driver.find_element(By.XPATH,self.programs_tab_xpath)
        self.lp.click_program_tab()
        if program_tab.is_displayed():
            if self.lp.click_program_tab():
                message = self.driver.find_element(By.XPATH, self.program_text_xpath).text
                if message == self.program_text_xpath:
                    self.logger.info("*******test_dashboard_program_tab*******")
                    self.driver.save_screenshot(".\\screenshots\\test_dashboard.png")
                    assert True
                    self.driver.close()
        else:
            self.logger.info("*******test_dashboard_program_tab*******")
            self.driver.save_screenshot(".\\screenshots\\test_dashboard.png")
            self.driver.close()
            assert False

    def test_program_tab_buttons(self, setup):
        self.driver = setup
        self.logger.info("*******test_program_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_program_tab()
        message = self.driver.find_element(By.XPATH, self.program_text_xpath).text
        if message == self.program_text_xpath:
            self.lp.click_programs_not_started_button()
            image = self.driver.find_element(By.XPATH, self.not_started_button_display)
            if image.is_displayed():
                self.logger.info("*******test_program_tab_buttons*******")
                self.driver.save_screenshot(".\\screenshots\\test_program_tab_buttons.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_program_tab_buttons*******")
                self.driver.close()
                assert False
            self.lp.click_programs_started_button()
            image = self.driver.find_element(By.XPATH, self.not_started_button_display)
            if image.is_displayed():
                self.logger.info("*******test_program_tab_buttons*******")
                self.driver.save_screenshot(".\\screenshots\\test_program_tab_buttons.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_program_tab_buttons*******")
                self.driver.close()
                assert False
            self.lp.click_programs_completed_button()
            display = self.driver.find_element(By.XPATH, self.completed_button_display)
            if display.is_displayed():
                self.logger.info("*******test_program_tab_buttons*******")
                self.driver.save_screenshot(".\\screenshots\\test_program_tab_buttons.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_program_tab_buttons*******")
                self.driver.close()
                assert False

    def test_programs_completed_buttons(self, setup):
        self.driver = setup
        self.logger.info("*******test_programs_completed_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_programs_completed_button()
        self.driver.find_element(By.XPATH, self.completed_button_block_heading)
        heading = self.driver.find_element(By.XPATH, self.completed_button_block_heading).text
        btn = self.driver.find_element(By.XPATH, self.completed_button_block_button)
        category = self.driver.find_element(By.XPATH, self.completed_button_block_category)
        repo = self.driver.find_element(By.XPATH, self.completed_button_block_report_view)

        if heading == self.completed_button_block_heading:
            self.logger.info("*******test_programs_completed_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_completed_buttons.png")
            assert True
            self.driver.close()
        elif btn == self.completed_button_block_button:
            self.logger.info("*******test_programs_completed_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_completed_buttons.png")
            assert True
            self.driver.close()
        elif category == self.completed_button_block_category:
            self.logger.info("*******test_programs_completed_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_completed_buttons.png")
            assert True
            self.driver.close()
        elif repo == self.completed_button_block_report_view:
            self.logger.info("*******test_programs_completed_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_completed_buttons.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_programs_completed_buttons*******")
            self.driver.close()
            assert False





