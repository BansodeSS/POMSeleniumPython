from selenium import webdriver
from Config.Config import TestData
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['chrome','firefox'],scope='class')
def init_driver(request):
    if request.param =='chrome':
        web_driver = webdriver.Chrome(ChromeDriverManager().install())

    if request.param =='firefox':
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()