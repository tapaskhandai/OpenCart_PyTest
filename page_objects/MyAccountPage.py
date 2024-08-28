from selenium.webdriver.common.by import By


class MyAccountPage:
    success_msg_account_updated = "//div[contains(text(),'Success: Your account')]"
    link_edit_account_info = "//a[normalize-space()='Edit your account information']"
    textbox_firstname_edit_info = "//input[@id='input-firstname']"
    textbox_lastname_edit_info = "//input[@id='input-lastname']"
    textbox_telnum_edit_info = "//input[@id='input-telephone']"
    button_continue_edit_info = "//input[@value='Continue']"
    link_change_password = "//a[normalize-space()='Change your password']"
    textbox_password_change_password = "//input[@id='input-password']"
    textbox_confirm_password_change_password = "//input[@id='input-confirm']"
    error_msg_change_password = "//div[contains(text(),'Password confirmation does not match password!')]"

    def __init__(self, driver):
        self.driver = driver  # self.driver is class variable here

    def click_edit_your_account_info(self):
        self.driver.find_element(By.XPATH, self.link_edit_account_info).click()

    def enter_personal_details(self, firstname, lastname, tel_num):
        self.driver.find_element(By.XPATH, self.textbox_firstname_edit_info).clear()
        self.driver.find_element(By.XPATH, self.textbox_firstname_edit_info).send_keys(firstname)
        self.driver.find_element(By.XPATH, self.textbox_lastname_edit_info).clear()
        self.driver.find_element(By.XPATH, self.textbox_lastname_edit_info).send_keys(lastname)
        self.driver.find_element(By.XPATH, self.textbox_telnum_edit_info).clear()
        self.driver.find_element(By.XPATH, self.textbox_telnum_edit_info).send_keys(tel_num)

    def click_continue_my_account(self):
        self.driver.find_element(By.XPATH, self.button_continue_edit_info).click()

    def capture_success_msg_account_updated(self):
        return self.driver.find_element(By.XPATH, self.success_msg_account_updated).text

    def click_change_your_password(self):
        self.driver.find_element(By.XPATH, self.link_change_password).click()

    def enter_password_and_confirm_password(self, password, confirm_password):
        self.driver.find_element(By.XPATH, self.textbox_password_change_password).send_keys(password)
        self.driver.find_element(By.XPATH, self.textbox_confirm_password_change_password).send_keys(confirm_password)

    def capture_error_msg_change_password(self):
        return self.driver.find_element(By.XPATH, self.error_msg_change_password).is_displayed()
