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

