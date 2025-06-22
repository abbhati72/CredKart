from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login_page_class:
    text_email_xpath = "//input[@id='email']"
    text_password_xpath = "//input[@id='password']"
    login_btn = "//button[@class='btn btn-primary']"
    toggle_xpath = "//a[@class='dropdown-toggle']"
    logout_btn_xpat = "//a[@href='https://automation.credence.in/logout']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def enter_email(self, email):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_email_xpath)))
        self.driver.find_element(By.XPATH, self.text_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_email_xpath).send_keys(email)

    def enter_password(self, password):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.text_password_xpath)))
        self.driver.find_element(By.XPATH, self.text_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_password_xpath).send_keys(password)

    def click_login_btn(self):
        self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.login_btn)))
        self.driver.find_element(By.XPATH, self.login_btn).click()

    def verify_login(self):
        try:
            self.wait.until(expected_conditions.visibility_of_element_located((By.XPATH, self.toggle_xpath)))
            return "pass"
        except:
            return "fail"
