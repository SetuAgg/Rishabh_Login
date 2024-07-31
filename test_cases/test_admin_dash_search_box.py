import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():
    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    search_box_id = "search"
    search_icon_Xpath = "//img[@src='./static/media/voice-search.5bc3256c9dbba7e3cb88a57208319427.svg']"
    search_icon_text = "//h3[@class='lable-heading_search']"
    search_icon_mic_Xpath = "//img[@src='./static/media/mic-search.a442ef7205029ba80a3c50ef00da8a03.svg']"

    def test_dash_search_box(self, setup):
        self.driver = setup
        self.logger.info("*******test_dash_search_box*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        search_box = self.driver.find_element(By.XPATH, self.search_box_id)
        if search_box.is_displayed():
            self.logger.info("*******test_dash_search_box*******")
            self.driver.save_screenshot(".\\screenshots\\test_dash_search_box.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_dash_search_box*******")
            self.driver.save_screenshot(".\\screenshots\\test_dash_search_box.png")
            self.driver.close()
            assert False

    def test_search_icon_mic(self, setup):
        self.driver = setup
        self.logger.info("*******test_search_icon_mic*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        text = self.driver.find_element(By.XPATH, self.search_icon_text).text
        if text == self.search_icon_text:
            self.lp.click_search_icon_mic()
            self.logger.info("*******test_search_icon_mic*******")
            self.driver.save_screenshot(".\\screenshots\\test_search_icon_mic.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_search_icon_mic*******")
            self.driver.close()
            assert False


    def test_search_icon(self,setup):
        self.driver = setup
        self.logger.info("*******test_search_icon*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_search_icon()
        text = self.driver.find_element(By.XPATH,self.search_icon_text).text
        if text == "Search Result for":
            self.logger.info("*******test_search_icon*******")
            self.driver.save_screenshot(".\\screenshots\\test_search_icon.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_search_icon*******")
            self.driver.save_screenshot(".\\screenshots\\test_search_icon.png")
            self.driver.close()
            assert False

