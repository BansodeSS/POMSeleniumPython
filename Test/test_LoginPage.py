import pytest
from Test.test_base import BaseTest
from Pages.LoginPage import  LoginPage
from Config.Config import TestData

class Test_Login(BaseTest):

    def test_signup_link_visible(self):
        self.login_page = LoginPage(self.driver)
        flag = self.login_page.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.login_page = LoginPage(self.driver)
        title = self.login_page.get_title(TestData.TITLE)
        assert title== TestData.TITLE

    def test_login(self):
        self.login_page = LoginPage(self.driver)
        self.login_page.do_login(TestData.USER_NAME,TestData.PASSWORD)

