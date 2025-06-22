from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_page_class


class Registration_page_class(Login_page_class):
    text_name_xpath = "//input[@id='name']"
    text_c_password_xpath = "//input[@id='password-confirm']"
    reg_btn_xpath = "//button[@type='submit']"

    def enter_name(self, name):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_name_xpath)))
       # self.driver.find_element(By.XPATH, self.text_name_xpath).send_Keys(name)

       # self.driver.find_element(By.XPATH, self.text_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_name_xpath).send_keys(name)

    def conf_password(self, password):
        self.driver.find_element(By.XPATH, self.text_c_password_xpath).send_keys(password)

    def reg_button_click(self):
        self.driver.find_element(By.XPATH, self.reg_btn_xpath).click()
