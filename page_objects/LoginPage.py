from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    link_MyAccount_Login = "//span[normalize-space()='My Account']"
    link_Login_Login = "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']"
    textbox_email_Login = "//input[@id='input-email']"
    textbox_password_Login = "//input[@id='input-password']"
    button_login_Login = "//input[@value='Login']"
    button_logout_homepage = "//a[normalize-space()='Logout']"
    button_continue_homepage = "//a[@class='btn btn-primary']"

    def __init__(self, driver):
        self.driver = driver  # self.driver is class variable here

    def click_my_account(self):
        self.driver.find_element(By.XPATH, self.link_MyAccount_Login).click()

    def click_login_header(self):
        self.driver.find_element(By.XPATH, self.link_MyAccount_Login).click()
        self.driver.find_element(By.XPATH, self.link_Login_Login).click()

    def enter_login_credentials(self, username, password):
        self.driver.find_element(By.XPATH, self.textbox_email_Login).send_keys(username)
        self.driver.find_element(By.XPATH, self.textbox_password_Login).send_keys(password)

    def click_submit_login(self):
        self.driver.find_element(By.XPATH, self.button_login_Login).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_logout_homepage).click()

    def click_continue_homepage(self):
        self.driver.find_element(By.XPATH, self.button_continue_homepage).click()
