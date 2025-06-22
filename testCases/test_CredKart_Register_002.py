import pytest
from faker import Faker

from pageObjects.RegisterPage import Registration_page_class
from utilities import readconfig, Logger
from utilities.teakScreenShotsSer import Take_Screen_Shots


@pytest.mark.usefixtures("driver_setup")
class Test_Register_002:
    driver = None
    register_url = readconfig.ReadConfig.reg_login_url()

    def test_registration_002(self):
        Logger.loggerClass.getLooger().info("test_registration_002")
        self.rg = Registration_page_class(self.driver)
        self.driver.get(self.register_url)
        print(Faker().name()+" >>>>>>>>>>>>>>>>>>>>>>>>>> ")
        self.rg.enter_name(Faker().name())
        self.rg.enter_email(Faker().email())
        self.rg.enter_password("demo@12345")
        self.rg.conf_password("demo@12345")
        self.rg.reg_button_click()

        if self.rg.verify_login() == "pass":
            Take_Screen_Shots.getScreenShots("Test_Register_002_pass",self.driver)
            assert True

        else:
            Take_Screen_Shots.getScreenShots("Test_Register_002_fail",self.driver)
            assert False
