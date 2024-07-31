import configparser

config = configparser.ConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_admin_page_url():
        url = config.get('admin login info','admin_page_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info','password')
        return password

    @staticmethod
    def get_invalid_username():
       invalid_username = config.get('admin login info','invalid_username')
       return invalid_username

    @staticmethod
    def get_invalid_password():
        invalid_password = config.get('admin login info','invalid_password')
        return invalid_password

    @staticmethod
    def get_logger():
        logger = config.get('admin login info','logger')
        return logger

    @staticmethod
    def get_image_Xpath():
        image_Xpath = config.get('admin login info','image_Xpath')
        return image_Xpath

    @staticmethod
    def test_title_verification():
        test_title = config.get('admin login info','test_title_verification')
        return test_title

    @staticmethod
    def page_purpose_heading():
        page_purpose = config.get('admin login info','page_purpose_heading')
        return page_purpose

    @staticmethod
    def username_verification():
        username_verification = config.get('admin login info','username_verification')
        return username_verification





    @staticmethod
    def get_page():
        url = config.get('Rishabh login page info','page_url')
        return url

    @staticmethod
    def get_image_url():
        image_Xpath = config.get('Rishabh login page info','image_Xpath')
        return image_Xpath

    @staticmethod
    def username():
        username = config.get('Rishabh login page info','user_name')
        return username

    @staticmethod
    def password():
        password = config.get('Rishabh login page info','pass_word')
        return password

    @staticmethod
    def invalid_username():
        invalid_username = config.get('Rishabh login page info','invalid_username')
        return invalid_username

    @staticmethod
    def invalid_password():
        invalid_password = config.get('Rishabh login page info','invalid_password')
        return invalid_password

    @staticmethod
    def get_logo():
        logo = config.get('Rishabh login page info','logo_X_path')
        return logo

    @staticmethod
    def get_welcome_messages():
        text = config.get('Rishabh login page info','welcome_text')
        return text












