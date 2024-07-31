import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():

    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    my_schedule_tab_xpath = "//a[@class='nav-link']"
    my_schedule_text_xpath = "//p[@class='lable-heading_search']"
    calender_block = "//div[@class='rbc-calendar']"
    calender_top_bar = "//div[@class='d-flex justify-content-between align-items-start filter-box-sec']"
    calender_short_view = "//div[@class='col-xl-3 col-sm-12 mt-5cal']"
    back_button = "//div[@class='calendar-bckbtn ms-0']"
    after_text = "//h3[@class='leader_text']"
    day_btn_xpath = "//button[@class='btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 ']"
    day_btn_display = "//div[@class='rbc-time-gutter rbc-time-column']"
    month_btn_xpath = "//button[@class='btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 ']"
    month_btn_display = "//div[@class='rbc-row rbc-month-header']"
    week_btn_xpath = "//button[@class='btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 active']"
    week_btn_display = "//div[@class='rbc-events-container']"
    back_arrow_btn = "//button[@class='button-reset']"
    forward_arrow_btn = "//button[@class='button-reset pe-0 rightprevbtn']"


    def test_my_schedule_tab(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        my_schedule_tab = self.driver.find_element(By.XPATH,self.my_schedule_tab_xpath)
        self.lp.click_my_schedule_tab()
        if my_schedule_tab.is_displayed():
            if self.lp.click_my_schedule_tab():
                message = self.driver.find_element(By.XPATH,self.my_schedule_text_xpath).text
                message == "Schedule"
                self.logger.info("*******test_my_schedule_tab*******")
                self.driver.save_screenshot(".\\screenshots\\test_my_schedule.png")
                assert True
                self.driver.close()
            else:
                self.logger.info("*******test_my_schedule_tab*******")
                self.driver.save_screenshot(".\\screenshots\\test_my_schedule.png")
                self.driver.close()
                assert False

    def test_my_schedule_tab_buttons(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_my_schedule_tab()
        calender_block = self.driver.find_element(By.XPATH,self.calender_block)
        calender_top_bar = self.driver.find_element(By.XPATH,self.calender_top_bar)
        calender_short_view = self.driver.find_element(By.XPATH,self.calender_short_view)
        back_btn = self.driver.find_element(By.XPATH,self.back_button)
        day_btn = self.driver.find_element(By.XPATH,self.day_btn_xpath)
        month_btn = self.driver.find_element(By.XPATH,self.month_btn_xpath)
        week_btn = self.driver.find_element(By.XPATH,self.week_btn_xpath)
        back_arrow_btn = self.driver.find_element(By.XPATH,self.back_arrow_btn)
        forward_arrow_btn = self.driver.find_element(By.XPATH,self.forward_arrow_btn)

        if calender_top_bar == self.calender_top_bar:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif calender_block == self.calender_block:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif calender_short_view == self.calender_short_view:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif back_btn == self.back_button:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif day_btn == self.day_btn_xpath:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif month_btn == self.month_btn_xpath:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif week_btn == self.week_btn_xpath:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif back_arrow_btn == self.back_arrow_btn:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        elif forward_arrow_btn == self.forward_arrow_btn:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False


    def test_my_schedule_back_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_back_button()
        text = self.driver.find_element(By.XPATH,self.after_text).text
        if text == "My Progress Status":
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_programs_my_schedule_tab_buttons.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False

    def test_my_schedule_day_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_day_button()
        display = self.driver.find_element(By.XPATH,self.day_btn_display)
        if display == self.day_btn_display:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_day_btn.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False

    def test_my_schedule_month_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_month_button()
        display = self.driver.find_element(By.XPATH,self.month_btn_display)
        if display == self.month_btn_display:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_month_btn.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False


    def test_my_schedule_week_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_week_button()
        display = self.driver.find_element(By.XPATH,self.week_btn_display)
        if display == self.week_btn_display:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_week_btn.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_tab_buttons*******")
            self.driver.close()
            assert False

    def test_back_arrow_btn_and_forward_arrow_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_tab_buttons*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_back_arrow_button()
        self.lp.click_forward_arrow_button()
        self.driver.close()

