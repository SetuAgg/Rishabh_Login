import pytest
from selenium.webdriver.common.by import By
from utilities.custom_logger import Log_Maker
from base_pages.Login_admin_Rishabh import Rishabh_Login_Page

class Rishabh_Test_02_Login_Admin():

    page_URL = "https://rishabhsoftacademy-preprod.niit.com/home"
    logger = Log_Maker.log_gen()
    logo_Xpath = "//img[@class='kotak-icon']"

    main_heading_Xpath = "//h3[@class='leader_text']"
    image_xpath = "//div[@class='top-banner']"

    centre_text_class = "leader_text"
    chart_section_xpath = "//div[@class='chart-sec']"
    chart_view_more_btn_xpath = "//button[@class='btn view-more-btn desk-view']"
    view_more_btn_program_text_xpath = "//h3[@class='program-head']"

    leader_board_left_box_xpath = "//div[@class='leaderboardSection-block']"
    leader_board_left_heading_xpath = "//h3[@class='leader_text  progress_text leader-bord-heading-desk']"
    leader_board_chart_xpath = "//div[@class='leaderBoardChart']"
    leader_board_right_box_xpath = "//div[@class='learning_point_section']"

    my_schedule_heading_xpath = "//h3[@class='mt-0']"
    calender_items_block = "//div[@class='accordion-item ']"
    calender_date_icon = "//div[@class='d-flex cal_iconLR']"
    calender_view = "//div[@id='collapseOne']"
    calender_view_more_btn = "//button[@class='calendar_view_more_btn ']"
    calender_view_more_btn_text = "//p[@class='lable-heading_search']"

    view_more_button = "//button[@class='btn view-more-btn']"
    announcements_text_xpath = "//h3[@class='program-head notification-heading mb-3']"
    announcements_card_xpath = "//span[@class='announcement-card']"
    announcements_slider_xpath = "//div[@class='announcement-slider-main']"

    star_of_the_month_xpath = "//div[@class='item']"
    star_of_the_month_heading = "//div[@class='col-md-12']"
    star_of_the_month_text = "//div[@class='star-main empty-start']"

    learners_experience_xpath = "//div[@id='myLearnerExperience']"
    learners_experience_heading = "//p[@class='lable-heading_search learner_txt']"
    learners_experience_slider = "// li[ @class ='slick-active']"


    feedback_btn = "//div[@class='feedback--button contentDesktopView']"
    feedback_btn_text = "//div[@id='example-custom-modal-styling-title']"



    footer_bar = "//footer[@class='home-footer_new']"
    footer_logo = "//div[@class='logoDiv d-flex']"
    footer_text = "//div[@class='footer_cont']"

    privacy_policy_and_terms_of_use_xpath = "//a[@target='_blank']"
    logo_text_xpath = "//img[@alt='niit logo']"



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




    def test_title_rishabh_dash(self,setup):
        self.driver = setup
        self.logger.info("*******test_title_rishabh_dash*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        actual_title = self.driver.title
        expected_title = "RishabhSoft"
        if actual_title == expected_title:
            self.logger.info("*******test_title_rishabh_dash*******")
            self.driver.save_screenshot(".\\screenshots\\test_title_rishabh_dash.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_title_rishabh_dash*******")
            self.driver.save_screenshot(".\\screenshots\\test_title_rishabh_dash.png")
            self.driver.close()
            assert False

    def test_dash_page_logo(self, setup):
        self.driver = setup
        self.logger.info("*******test_dash_page_logo*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        logo_element = self.driver.find_element(By.XPATH,self.logo_Xpath)
        if logo_element.is_displayed():
            self.logger.info("*******test_dash_page_logo*******")
            self.driver.save_screenshot(".\\screenshots\\test_dash_logo.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_dash_page_logo*******")
            self.driver.save_screenshot(".\\screenshots\\test_dash_logo.png")
            self.driver.close()
            assert False



    def test_main_heading(self, setup):
        self.driver = setup
        self.logger.info("*******test_main_heading*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        heading = self.driver.find_element(By.CLASS_NAME,self.main_heading_Xpath).text
        if heading == "IOT":
            self.logger.info("*******test_main_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_main_heading.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_main_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_main_heading.png")
            self.driver.close()
            assert False



    def test_page_image(self,setup):
        self.driver = setup
        self.logger.info("*******test_page_image*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        image = self.driver.find_element(By.XPATH,self.image_xpath)
        if image.is_displayed():
            self.logger.info("*******test_page_image*******")
            self.driver.save_screenshot(".\\screenshots\\test_page_image.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_page_image*******")
            self.driver.save_screenshot(".\\screenshots\\test_page_image.png")
            self.driver.close()
            assert False


    def test_center_text(self,setup):
        self.driver = setup
        self.logger.info("*******center_text*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        centre_text = self.driver.find_element(By.CLASS_NAME,self.centre_text_class)
        if centre_text.is_displayed():
            if centre_text == "My Progress Status":
                self.logger.info("*******test_center_text*******")
                self.driver.save_screenshot(".\\screenshots\\test_center_text.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_center_text*******")
            self.driver.save_screenshot(".\\screenshots\\test_center_text.png")
            self.driver.close()
            assert False


    def test_chart_section(self,setup):
        self.driver = setup
        self.logger.info("*******test_chart_section*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        chart_section = self.driver.find_element(By.XPATH,self.chart_section_xpath)
        if chart_section.is_displayed():
            self.logger.info("*******test_chart_section*******")
            self.driver.save_screenshot(".\\screenshots\\test_chart_section.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_chart_section*******")
            self.driver.save_screenshot(".\\screenshots\\test_chart_section.png")
            self.driver.close()
            assert False


    def test_chart_view_more_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_chart_view_more_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        view_btn = self.driver.find_element(By.XPATH,self.chart_view_more_btn_xpath)
        self.lp.click_chart_view_more_btn()
        text = self.driver.find_element(By.XPATH,self.view_more_btn_program_text_xpath)
        if view_btn.is_displayed():
            if text == "Program":
                self.logger.info("*******test_chart_view_more_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_chart_view_more_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_chart_view_more_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_chart_view_more_btn.png")
            self.driver.close()
            assert False


    def test_leader_board_left_box_xpath(self,setup):
        self.driver = setup
        self.logger.info("*******test_leader_board_left_box_xpath*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        left_box = self.driver.find_element(By.XPATH,self.leader_board_left_box_xpath)
        if left_box.is_displayed():
            self.logger.info("*******test_leader_board_left_box_xpath*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_left_box.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_leader_board_left_box_xpath*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_left_box.png")
            self.driver.close()
            assert False


    def test_leader_board_heading(self,setup):
        self.driver = setup
        self.logger.info("*******test_leader_board_heading*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        heading = self.driver.find_element(By.XPATH,self.leader_board_left_heading_xpath).text
        if heading == "Leaderboard":
            self.logger.info("*******test_leader_board_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_heading.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_leader_board_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_heading.png")
            self.driver.close()
            assert False


    def test_leader_board_chart(self,setup):
        self.driver = setup
        self.logger.info("*******test_leader_board_chart*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        chart = self.driver.find_element(By.XPATH,self.leader_board_chart_xpath)
        if chart.is_displayed():
            self.logger.info("*******test_leader_board_chart*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_chart.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_leader_board_chart*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_chart.png")
            self.driver.close()
            assert False


    def test_leader_board_right_box(self,setup):
        self.driver = setup
        self.logger.info("*******test_leader_board_right_box*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        leader_board_right_box = self.driver.find_element(By.XPATH,self.leader_board_right_box_xpath)
        if leader_board_right_box.is_displayed():
            self.logger.info("*******test_leader_board_right_box*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_right_box.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_leader_board_right_box*******")
            self.driver.save_screenshot(".\\screenshots\\test_leader_board_right_box.png")
            self.driver.close()
            assert False


    def test_my_schedule_heading(self,setup):
        self.driver = setup
        self.logger.info("*******test_my_schedule_heading*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        my_schedule_heading = self.driver.find_element(By.XPATH,self.my_schedule_heading_xpath)
        if my_schedule_heading == "My Schedule":
            self.logger.info("*******test_my_schedule_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_heading.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_my_schedule_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_my_schedule_header.png")
            self.driver.close()
            assert False



    def test_calender_items_block(self,setup):
        self.driver = setup
        self.logger.info("*******test_calender_items_block*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        calender_item_block = self.driver.find_element(By.XPATH,self.calender_items_block)
        if calender_item_block.is_displayed():
            self.logger.info("*******test_calender_items_block*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_items_block.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_calender_items_block*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_items_block.png")
            self.driver.close()
            assert False


    def test_calender_date_icon(self,setup):
        self.driver = setup
        self.logger.info("*******test_calender_date_icon*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        data_icon = self.driver.find_element(By.XPATH,self.calender_date_icon)
        if data_icon.is_displayed():
            self.logger.info("*******test_calender_date_icon*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_date_icon.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_calender_date_icon*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_date_icon.png")
            self.driver.close()
            assert False

    def test_calender_view(self,setup):
        self.driver = setup
        self.logger.info("*******test_calender_view*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        calender_view = self.driver.find_element(By.XPATH,self.calender_view)
        if calender_view.is_displayed():
            self.logger.info("*******test_calender_view*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_view.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_calender_view*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_view.png")
            self.driver.close()
            assert False


    def test_calender_view_more_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_calender_view_more_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_calender_view_more_btn()
        calender_view_more_btn = self.driver.find_element(By.XPATH,self.calender_view_more_btn)
        text = self.driver.find_element(By.XPATH,self.calender_view_more_btn_text).text
        if calender_view_more_btn.is_displayed():
            if text == "Schedule":
                self.logger.info("*******test_calender_view_more_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_calender_view_more_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_calender_view_more_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_calender_view_more_btn.png")
            self.driver.close()
            assert False

    def test_view_more_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_view_more_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_view_more_button()
        text = self.driver.find_element(By.XPATH,self.announcements_text_xpath).text
        if text == "Announcements":
            self.logger.info("*******test_view_more_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_view_more_btn.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_view_more_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_view_more_btn.png")
            self.driver.close()
            assert False



    def test_announcements_card(self,setup):
        self.driver = setup
        self.logger.info("*******test_announcements_card*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        announcement_cards = self.driver.find_element(By.XPATH,self.announcements_card_xpath)
        if announcement_cards.is_displayed():
            self.logger.info("*******test_announcements_card*******")
            self.driver.save_screenshot(".\\screenshots\\test_announcements_card.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_announcements_card*******")
            self.driver.close()
            assert False


    def test_announcements_slider(self,setup):
        self.driver = setup
        self.logger.info("*******test_announcements_slider*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        slider = self.driver.find_element(By.XPATH,self.announcements_slider_xpath)
        if slider.is_displayed():
            self.logger.info("*******test_announcements_slider*******")
            self.driver.save_screenshot(".\\screenshots\\test_announcements_slider.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_announcements_slider*******")
            self.driver.close()
            assert False


    def test_star_of_the_month(self,setup):
        self.driver = setup
        self.logger.info("*******test_star_of_the_month*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        star_of_the_month = self.driver.find_element(By.XPATH,self.star_of_the_month_xpath)
        if star_of_the_month.is_displayed():
            self.logger.info("*******test_star_of_the_month*******")
            self.driver.save_screenshot(".\\screenshots\\test_star_of_the_month.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_star_of_the_month*******")
            self.driver.save_screenshot(".\\screenshots\\test_star_of_the_month.png")
            self.driver.close()
            assert False


    def test_star_of_the_month_heading(self,setup):
        self.driver = setup
        self.logger.info("*******test_star_of_the_month_heading*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        head = self.driver.find_element(By.XPATH,self.star_of_the_month_heading)
        if head.is_displayed():
            if head == "Star Of The Month":
                self.logger.info("*******test_star_of_the_month_heading*******")
                self.driver.save_screenshot(".\\screenshots\\test_star_of_the_month_heading.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_star_of_the_month_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_star_of_the_month_heading.png")
            self.driver.close()
            assert False


    def test_star_of_the_month_text(self,setup):
        self.driver = setup
        self.logger.info("*******test_star_of_the_month_text*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        text = self.driver.find_element(By.XPATH,self.star_of_the_month_text)
        if text.is_displayed():
            self.logger.info("*******test_star_of_the_month_text*******")
            self.driver.save_screenshot(".\\screenshots\\test_star_of_the_month_text.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_star_of_the_month_text*******")
            self.driver.save_screenshot(".\\screenshots\\test_star_of_the_month_text.png")
            self.driver.close()
            assert False


    def test_learners_experience(self,setup):
        self.driver = setup
        self.logger.info("*******test_learners_experience*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        learner_experience = self.driver.find_element(By.XPATH,self.learners_experience_xpath)
        if learner_experience.is_displayed():
            self.logger.info("*******test_learners_experience*******")
            self.driver.save_screenshot(".\\screenshots\\test_learners_experience.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_learners_experience*******")
            self.driver.save_screenshot(".\\screenshots\\test_learners_experience.png")
            self.driver.close()
            assert False


    def test_learners_experience_heading(self,setup):
        self.driver = setup
        self.logger.info("*******test_learners_experience_heading*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        heading = self.driver.find_element(By.XPATH,self.learners_experience_heading)
        if heading == "Learner Experience":
            if heading.is_displayed():
                self.logger.info("*******test_learners_experience_heading*******")
                self.driver.save_screenshot(".\\screenshots\\test_learners_experience_heading.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_learners_experience_heading*******")
            self.driver.save_screenshot(".\\screenshots\\test_learners_experience_heading.png")
            self.driver.close()
            assert False


    def test_learners_experience_slider(self,setup):
        self.driver = setup
        self.logger.info("*******test_learners_experience_slider*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        slider = self.driver.find_element(By.XPATH,self.learners_experience_slider)
        if slider.is_displayed():
            self.logger.info("*******test_learners_experience_slider*******")
            self.driver.save_screenshot(".\\screenshots\\test_learners_experience_slider.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_learners_experience_slider*******")
            self.driver.save_screenshot(".\\screenshots\\test_learners_experience_slider.png")
            self.driver.close()
            assert False



    def test_footer_bar(self,setup):
        self.driver = setup
        self.logger.info("*******test_footer_bar*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        footer_bar = self.driver.find_element(By.XPATH,self.footer_bar)
        if footer_bar.is_displayed():
            self.logger.info("*******test_footer_bar*******")
            self.driver.save_screenshot(".\\screenshots\\test_footer_bar.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_footer_bar*******")
            self.driver.save_screenshot(".\\screenshots\\test_footer_bar.png")
            self.driver.close()
            assert False


    def test_footer_logo(self,setup):
        self.driver = setup
        self.logger.info("*******test_footer_logo*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        logo = self.driver.find_element(By.XPATH,self.footer_logo)
        if logo.is_displayed():
            self.logger.info("*******test_footer_logo*******")
            self.driver.save_screenshot(".\\screenshots\\test_footer_logo.png")
            assert True
            self.driver.close()
        else:
            self.logger.info("*******test_footer_logo*******")
            self.driver.save_screenshot(".\\screenshots\\test_footer_logo.png")
            self.driver.close()
            assert False


    def test_footer_text(self,setup):
        self.driver = setup
        self.logger.info("*******test_footer_text*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        text = self.driver.find_element(By.XPATH,self.footer_text).text
        if text.is_displayed():
            if text == "Copyright © 2024 NIIT Inc. All rights reserved." and text == "Privacy Policy|Terms of Use":

                self.logger.info("*******test_footer_text*******")
                self.driver.save_screenshot(".\\screenshots\\test_footer_text.png")
                assert True
                self.driver.close()
        else:

            self.logger.info("*******test_footer_text*******")
            self.driver.save_screenshot(".\\screenshots\\test_footer_text.png")
            self.driver.close()
            assert False


    def test_feedback_btn(self,setup):
        self.driver = setup
        self.logger.info("*******test_feedback_btn*******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_feedback_btn()
        message = self.driver.find_element(By.XPATH,self.feedback_btn_text).text
        if message == "Submit your feedback":
            if message.is_displayed():
                self.logger.info("*******test_feedback_btn*******")
                self.driver.save_screenshot(".\\screenshots\\test_feedback_btn.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_feedback_btn*******")
            self.driver.save_screenshot(".\\screenshots\\test_feedback_btn.png")
            self.driver.close()
            assert False


    def test_privacy_policy_and_terms_of_use(self,setup):
        self.driver = setup
        self.logger.info("*******test_privacy_policy_and_terms_of_use******")
        self.driver.get(Rishabh_Test_02_Login_Admin)
        self.driver.get(self.page_URL)
        self.lp = Rishabh_Login_Page(self.driver)
        self.lp.click_privacy_policy()
        self.lp.click_terms_of_use()
        text_logo = self.driver.find_element(By.XPATH,self.logo_text_xpath)
        if text_logo.is_displayed():
            if text_logo == "NIIT":
                self.logger.info("*******test_privacy_policy_and_terms_of_use******")
                self.driver.save_screenshot(".\\screenshots\\test_privacy_policy_and_terms_of_use.png")
                assert True
                self.driver.close()
        else:
            self.logger.info("*******test_privacy_policy_and_terms_of_use*******")
            self.driver.save_screenshot(".\\screenshots\\test_privacy_policy_and_terms_of_use.png")
            self.driver.close()
            assert False

















































































































































































































