import selenium.webdriver.common.by

from selenium.webdriver.common.by import By

#import selenium.By



class LoginPage:
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    usernameInput = (By.XPATH, "//*[@data-cy='userName']")
    continueBtn = (By.XPATH, "//*[@data-cy='continueBtn']")
    otpInput = (By.ID, "otp")
    loginBtn = (By.XPATH, "//*[@data-cy='login']")

    def usernameInputOption(self):
        return self.driver.find_element(*LoginPage.usernameInput)

    def continueBtnOption(self):
        return self.driver.find_element(*LoginPage.continueBtn)

    def otpInputOption(self):
        return self.driver.find_element(*LoginPage.otpInput)

    def loginBtnOption(self):
        return self.driver.find_element(*LoginPage.loginBtn)