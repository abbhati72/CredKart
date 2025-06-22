import pytest

from pageObjects import Login_Page
from pageObjects.Login_Page import Login_page_class
from utilities import readconfig, Logger, teakScreenShotsSer

@pytest.mark.usefixtures("driver_setup")
class Test_CredKat_Login_Class:
    driver = None
    login_url = readconfig.ReadConfig.get_login_url()
    reg_url = readconfig.ReadConfig.reg_login_url()
    username = readconfig.ReadConfig.get_username()
    password = readconfig.ReadConfig.get_password()

    def test_login_001(self):
        Logger.loggerClass.getLooger().info("inside test login 001")

        # driver.get(readconfig.ReadConfig.get_login_url())
        self.lp = self.driver.get(self.login_url)
        self.lp = Login_page_class(self.driver)
        self.lp.enter_email(readconfig.ReadConfig.get_username())
        self.lp.enter_password(readconfig.ReadConfig.get_password())
        self.lp.click_login_btn()

        print(">>>>>>>>>>>>>>>>>>>>> ", self.lp.verify_login())

        if self.lp.verify_login() == "pass":
            Logger.loggerClass.getLooger().info("inside test login 001 PASS")
            teakScreenShotsSer.Take_Screen_Shots.getScreenShots("test_login_001_pass", self.driver)
            assert True
        else:
            Logger.loggerClass.getLooger().info("inside test login 001 FAIL")
            assert False

    def test_title_cjeck_003(self):
        Logger.loggerClass.getLooger().info("test_title_cjeck_003")
        self.lp = self.driver.get(self.login_url)
        print(self.driver.title)
        if self.driver.title == "CredKart":
            Logger.loggerClass.getLooger().info("test_title_cjeck_003_PASS")
            assert True

        else:
            Logger.loggerClass.getLooger().info("test_title_cjeck_003_FAIL")
            assert False

