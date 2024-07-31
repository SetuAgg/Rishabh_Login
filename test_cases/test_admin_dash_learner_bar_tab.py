import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():

    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    learner_bar_xpath = "//select[@class='form-select']"
    learner_bar_option1 = "//option[@value='1']"
    learner_bar_option2 = "//option[@value='2']"
    learner_bar_option3 = "//option[@value='4']"
    main_heading_Xpath = "//h3[@class='leader_text']"
    instructor_display = "//div[@class='d-flex align-items-center justify-content-center row mt-2']"
    instructor_option_bar = "//select[@class='notification-select form-select']"
    instructor_option_bar_option1 = "//option[@value='Today']"
    instructor_option_bar_option2 = "//option[@value='Past']"
    instructor_option_bar_option3 = "//option[@value='Future']"
    instructor_option_bar_option3_text = "//div[@class='accordion-button collapsed']"


    def test_learner_bar_tab(self, setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        learner_tab = self.driver.find_element(By.XPATH,self.learner_bar_xpath)
        self.lp.click_learner_bar()
        if learner_tab.is_displayed():
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False


    def test_learner_bar_options1(self, setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_learner_bar()
        self.lp.click_learner_bar_option1()
        text = self.driver.find_element(By.XPATH,self.main_heading_Xpath).text
        if text == "My Progress Status":
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False

    def test_learner_bar_options2(self, setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_learner_bar()
        self.lp.click_learner_bar_option2()
        text = self.driver.find_element(By.XPATH,self.main_heading_Xpath).text
        if text == "My Progress Status":
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False

    def test_learner_bar_options3(self, setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_learner_bar()
        self.lp.click_learner_bar_option3()
        text = self.driver.find_element(By.XPATH,self.instructor_display)
        if text == self.learner_bar_option3:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False

    def test_instructor_options(self,setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_instructor_option_bar()
        self.lp.click_today()
        text = self.driver.find_element(By.XPATH,self.instructor_display)
        if text == self.instructor_display:
            if text.is_displayed():
                self.logger.info("*******learner_bar_tab*******")
                self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False

    def test_instructor_options2(self, setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_instructor_option_bar()
        self.lp.click_future()
        text = self.driver.find_element(By.XPATH,self.instructor_display)
        if text == self.instructor_display:
            if text.is_displayed():
                self.logger.info("*******learner_bar_tab*******")
                self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False

    def test_instructor_option3(self,setup):
        self.driver = setup
        self.logger.info("*******learner_bar_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_instructor_option_bar()
        self.lp.click_past()
        message = self.driver.find_element(By.XPATH,self.instructor_option_bar_option3_text)
        if message == self.instructor_option_bar_option3_text:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******learner_bar_tab*******")
            self.driver.save_screenshot(".\\screenshots\\learner_bar_tab.png")
            self.driver.close()
            assert False




















