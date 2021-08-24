from Pages.BasePages import BasePages
from Config.Config import TestData
from selenium.webdriver.common.by import By

class LoginPage(BasePages):
    '''
    We have to create base page which will be super class of all pages
    '''

    EMAIL = (By.ID,"username")
    PASSWORD = (By.ID,"password")
    LOGIN_BTN = (By.ID,"loginBtn")
    SINGUP_LINK = (By.LINK_TEXT,"Sign up")
    '''
    constructor of page class
    '''
    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.delete_all_cookies()
    '''
    Page Actions
    '''
    ''' this is used to get page title'''
    def get_login_page_title(self,title):
        return self.get_title(title)

    ''' This is used to get sign up link'''
    def is_signup_link_exist(self):
        return self.is_visible(self.SINGUP_LINK)

    ''' This is used to login to app'''
    def do_login(self,username,password):
        self.do_send_key(self.EMAIL,username)
        self.do_send_key(self.PASSWORD,password)
        self.do_click(self.LOGIN_BTN)