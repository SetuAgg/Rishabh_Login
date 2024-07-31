import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():

    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    notification_bell_xpath = "//img[@id='niit_logo_mob']"
    notification_bell_dropdown = "//a[@class='get_CertifiedContainer dropdownItem_notiFcation dropdown-item']"
    show_all_btn = "//button[@class='btn setup-button rs-btn']"
    show_all_display = "//h3[@class='program-head notification-heading mb-3']"
    show_all_back_button = "//button[@class='btn btn-primary bckbtn module-backbtn']"
    all_bar_xpath = "//select[@class='notification-select form-select']"
    read_option = "//option[@value='read']"
    unread_option = "//option[@value='unread']"
    notification_present = "//div[@class='notification-head-main']"
    main_heading_Xpath = "//h3[@class='leader_text']"



    def test_notifications_bell(self,setup):
        self.driver = setup
        self.logger.info("*******test_notifications_bell*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        notification_bell = self.driver.find_element(By.XPATH, self.notification_bell_xpath)
        self.lp.click_notification_bell()
        if notification_bell.is_displayed():
            message = self.driver.find_element(By.XPATH, self.notification_bell_xpath).text
            if message == "Show all":
                self.logger.info("*******test_notifications_bell*******")
                self.driver.save_screenshot(".\\screenshots\\test_notifications_bell.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_notifications_bell*******")
            self.driver.save_screenshot(".\\screenshots\\test_notifications_bell.png")
            self.driver.close()
            assert False

    def test_notification_bell_dropdown(self, setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_notification_bell()
        text = self.driver.find_element(By.XPATH, self.show_all_btn).button
        if text == self.show_all_btn:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False

    def test_show_all_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_show_all_btn()
        text = self.driver.find_element(By.XPATH, self.show_all_display).text
        if text == "Notifications":
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_notifications.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False

    def test_show_all_back_btn(self, setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_show_All_back_btn()
        text = self.driver.find_element(By.XPATH, self.main_heading_Xpath).text
        if text == "My Progress Status":
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_progress_status.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False

    def test_all_bar(self, setup):
        self.driver = setup
        self.logger.info("*******test_all_bar*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_all_bar()
        self.logger.info("****Clickable****")
        self.driver.save_screenshot(".\\screenshots\\test_all_bar.png")

    def test_all_bar_read_option(self, setup):
        self.driver = setup
        self.logger.info("*******test_all_bar_read_option*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_read_options()
        self.logger.info("****Clickable****")
        self.driver.save_screenshot(".\\screenshots\\test_all_bar_read_option.png")

    def test_all_bar_unread_option(self, setup):
        self.driver = setup
        self.logger.info("*******test_all_bar_unread_option*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_unread_options()
        self.logger.info("****Clickable****")
        self.driver.save_screenshot(".\\screenshots\\test_all_bar_unread_option.png")

    def test_notification_present(self, setup):
        self.driver = setup
        self.logger.info("*******test_notification_present*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        notify = self.driver.find_element(By.XPATH, self.notification_present)
        if notify.is_displayed():
            self.logger.info("*******test_notification_present*******")
            self.driver.save_screenshot(".\\screenshots\\test_notification_present.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_notification_present*******")
            self.driver.save_screenshot(".\\screenshots\\test_notification_present.png")
            self.driver.close()
            assert False



