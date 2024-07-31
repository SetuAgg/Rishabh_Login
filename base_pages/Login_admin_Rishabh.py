from selenium.webdriver.common.by import By



class Rishabh_Login_Page:
    textbox_username_name = "email"
    textbox_password_id = "passInput"
    btn_login_xpath = "//button[@type='submit']"
    image_Xpath = "//img[@class='img-fluid']"
    logo_X_path = "//img[@alt='images']"
    dashboard_tab_class = "//a[@class='nav-link']"

    programs_tab_xpath = "//a[@class='nav-link eureka_header_li active_status_color']"
    my_schedule_tab_xpath = "//a[@class='nav-link']"
    notification_bell_xpath = "//img[@id='niit_logo_mob']"

    learner_bar_xpath = "//select[@class='form-select']"
    learner_bar_option1 = "//option[@value='1']"
    learner_bar_option2 = "//option[@value='2']"
    learner_bar_option3 = "//option[@value='4']"
    instructor_option_bar = "//select[@class='notification-select form-select']"
    instructor_option_bar_option1 = "//option[@value='Today']"
    instructor_option_bar_option2 = "//option[@value='Past']"
    instructor_option_bar_option3 = "//option[@value='Future']"

    profile_dropdown_xpath = "//img[@style='width: 55px; height: 55px; border-radius: 50%;']"
    profile_dropdown_my_profile = "//div[@class='customHover']"
    my_profile_display = "//section[@class='profile-banner container']"
    profile_dropdown_my_progress = "//div[@class='customHover my_progress_cursor']"
    profile_dropdown_certificates = "//div[@class='customHover']"
    profile_dropdown_learning_points = "//div[@class='customHover']"
    profile_dropdown_my_programs = "//a[@class='customHover dropdown-item']"
    profile_dropdown_change_password = "//a[@class='customHover dropdown-item']"
    profile_dropdown_log_out = "//a[@class='customHover dropdown-item']"



    view_more_btn_xpath = "//button[@class='btn view-more-btn desk-view']"
    calender_view_more_btn = "//button[@class='calendar_view_more_btn ']"
    view_more_button = "//button[@class='btn view-more-btn']"
    feedback_btn = "//div[@class='feedback--button contentDesktopView']"
    privacy_policy_xpath = "//a[@target='_blank']"
    terms_of_use = "//a[@target='_blank']"
    search_icon_Xpath = "//img[@src='./static/media/voice-search.5bc3256c9dbba7e3cb88a57208319427.svg']"
    search_icon_mic_Xpath = "//img[@src='./static/media/mic-search.a442ef7205029ba80a3c50ef00da8a03.svg']"
    programs_not_started_button = "//button[@class=' active nav-link']"
    programs_started_button = "//button[@id='profile-tab']"
    programs_completed_button = "//button[@id='messages-tab']"

    back_button = "//div[@class='calendar-bckbtn ms-0']"
    day_btn_xpath = "//button[@class='btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 ']"
    month_btn_xpath = "//button[@class='btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 ']"
    week_btn_xpath = "//button[@class='btn btn-primary btn-block setup-button upgrate_colpeteBtn mr-2 active']"
    back_arrow_btn = "//button[@class='button-reset']"
    forward_arrow_btn = "//button[@class='button-reset pe-0 rightprevbtn']"

    show_all_btn = "//button[@class='btn setup-button rs-btn']"
    show_all_back_button = "//button[@class='btn btn-primary bckbtn module-backbtn']"
    all_bar_xpath = "//select[@class='notification-select form-select']"
    read_option = "//option[@value='read']"
    unread_option = "//option[@value='unread']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, self.textbox_username_name).clear()
        self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()


    def click_dashboard_tab(self):
        self.driver.find_element(By.XPATH, self.dashboard_tab_class).click()


    def click_program_tab(self):
        self.driver.find_element(By.XPATH, self.programs_tab_xpath).click()

    def click_my_schedule_tab(self):
        self.driver.find_element(By.XPATH, self.my_schedule_tab_xpath).click()


    def click_notification_bell(self):
        self.driver.find_element(By.XPATH, self.notification_bell_xpath).click()


    def click_learner_bar(self):
        self.driver.find_element(By.XPATH, self.learner_bar_xpath).click()

    def click_learner_bar_option1(self):
        self.driver.find_element(By.XPATH,self.learner_bar_option1).click()

    def click_learner_bar_option2(self):
        self.driver.find_element(By.XPATH,self.learner_bar_option2).click()

    def click_learner_bar_option3(self):
        self.driver.find_element(By.XPATH,self.learner_bar_option3).click()

    def click_instructor_option_bar(self):
        self.driver.find_element(By.XPATH,self.instructor_option_bar).click()



    def click_today(self):
        self.driver.find_element(By.XPATH, self.instructor_option_bar_option1).click()
    def click_future(self):
        self.driver.find_element(By.XPATH, self.instructor_option_bar_option2).click()
    def click_past(self):
        self.driver.find_element(By.XPATH, self.instructor_option_bar_option3).click()




    def click_profile_dropdown(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_xpath).click()
    def click_my_profile(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_my_profile).click()
    def click_my_progress(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_my_progress).click()

    def click_certificates(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_certificates).click()

    def click_learning_pointers(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_learning_points).click()

    def click_my_programs_btn(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_my_programs).click()

    def click_change_password(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_change_password).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.profile_dropdown_log_out).click()


    def click_chart_view_more_btn(self):
        self.driver.find_element(By.XPATH, self.view_more_btn_xpath).click()


    def click_calender_view_more_btn(self):
        self.driver.find_element(By.XPATH, self.calender_view_more_btn).click()

    def click_view_more_button(self):
        self.driver.find_element(By.XPATH, self.view_more_button).click()

    def click_feedback_btn(self):
        self.driver.find_element(By.XPATH,self.feedback_btn).click()


    def click_privacy_policy(self):
        self.driver.find_element(By.XPATH,self.privacy_policy_xpath).click()


    def click_terms_of_use(self):
        self.driver.find_element(By.XPATH, self.terms_of_use).click()


    def click_search_icon(self):
        self.driver.find_element(By.XPATH, self.search_icon_Xpath).click()


    def click_search_icon_mic(self):
        self.driver.find_element(By.XPATH, self.search_icon_mic_Xpath).click()


    def click_programs_not_started_button(self):
        self.driver.find_element(By.XPATH, self.programs_not_started_button).click()


    def click_programs_started_button(self):
        self.driver.find_element(By.XPATH, self.programs_started_button).click()


    def click_programs_completed_button(self):
        self.driver.find_element(By.XPATH, self.programs_completed_button).click()


    def click_back_button(self):
        self.driver.find_element(By.XPATH,self.back_button).click()

    def click_day_button(self):
        self.driver.find_element(By.XPATH,self.day_btn_xpath).click()

    def click_month_button(self):
        self.driver.find_element(By.XPATH,self.month_btn_xpath).click()

    def click_week_button(self):
        self.driver.find_element(By.XPATH,self.week_btn_xpath).click()

    def click_back_arrow_button(self):
        self.driver.find_element(By.XPATH,self.back_arrow_btn).click()

    def click_forward_arrow_button(self):
        self.driver.find_element(By.XPATH,self.forward_arrow_btn).click()

    def click_show_all_btn(self):
        self.driver.find_element(By.XPATH,self.show_all_btn).click()

    def click_show_All_back_btn(self):
        self.driver.find_element(By.XPATH,self.show_all_back_button).click()

    def click_all_bar(self):
        self.driver.find_element(By.XPATH,self.all_bar_xpath).click()

    def click_read_options(self):
        self.driver.find_element(By.XPATH,self.read_option).click()

    def click_unread_options(self):
        self.driver.find_element(By.XPATH,self.unread_option).click()














































