import pytest
from selenium.webdriver.common.by import By
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page
from utilities.custom_logger import Log_Maker


class Rishabh_Test_02_Login_Admin:
    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    dashboard_tab_class = "//a[@class='nav-link']"
    dashboard_tab_visible_text = "//h3[@class='leader_text']"



    @pytest.mark.usefixtures("setup")
    def test_dashboard_tab(self, setup):
        self.driver = setup
        self.logger.info("*******test_dashboard_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_dashboard_tab()
        dashboard_tab = self.driver.find_element(By.XPATH, self.dashboard_tab_class)
        dash_text = self.driver.find_element(By.XPATH, self.dashboard_tab_visible_text).text
        if dashboard_tab.is_displayed():
            if dash_text == "My Progress Status":
                self.logger.info("*******test_dashboard_tab*******")
                self.driver.save_screenshot(".\\screenshots\\test_dashboard_tab.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_dashboard_tab*******")
            self.driver.save_screenshot(".\\screenshots\\test_dashboard_tab.png")
            self.driver.close()
            assert False
