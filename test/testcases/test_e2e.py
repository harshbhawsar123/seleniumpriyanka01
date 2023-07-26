import time
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from main.objects.Logging import LoginPage
from main.objects.booking import booking
from main.utilities.DBCollectionFile import DBCollectionFile
from test.testcases.BassClass import BassClass

@pytest.mark.usefixtures("setup")
class TestBooking(BassClass):

    def test_booking(self, logs=None):
        logger = self.get_logger()
        try:
            logger.debug('Browser Launched')
            db=DBCollectionFile()
            data=db.debconnect()
            service_obj = Service("C:/WebDrivers.exe")
            driver = webdriver.Chrome(service=service_obj)
            driver.get("https://www.makemytrip.com/")
            driver.maximize_window()
            Login=LoginPage(self.driver)
            time.sleep(3)
            #driver.switch_to.active_element
            time.sleep(12)
            frameList = self.driver.find_elements(by=By.TAG_NAME, value="iframe")
            self.driver.switch_to.frame(frameList[3])
            time.sleep(2)
            self.driver.execute_script("document.elementFromPoint(0,0).click()")
            time.sleep(5)
            '''Login.usernameInputOption().send_keys('9713212872')
            time.sleep(5)
            #driver.switch_to.active_element
            Login.continueBtnOption().click()
            time.sleep(3)
            otp=input()
            Login.otpInput().send_keys(otp)
            time.sleep(3)
            Login.loginBtnOption().click()
            time.sleep(3)'''
            driver.execute_script("document.elementFromPoint(0,0).click()")
            bookObj = booking(self.driver)
            bookObj.fromButtonOption().click()
            #driver.find_element(By.XPATH,value="//span[text()='From']").click()
            time.sleep(10)
            bookObj.fromInputOption().send_keys(data[0])
            time.sleep(5)

            bookObj = booking(self.driver)
            time.sleep(3)
            bookObj.fromButtonOption().click()
            time.sleep(3)
            bookObj.fromInputOption().send_keys(data[0])
            time.sleep(3)
            bookObj.fromCityOption().click()
            time.sleep(3)
            bookObj.toButtonOption().click()
            time.sleep(2)
            bookObj.toInputOption().send_keys(data[1])
            time.sleep(2)
            bookObj.toCityOption().click()
            time.sleep(5)
            bookObj.nextBtnOption().click()
            time.sleep(3)
            dates = bookObj.dateChoicesOption()
            print(len(dates))
            for d in dates:
                e = d.find_element(By.TAG_NAME, value="p")
                if e.text == '15':
                    e.click()
                    break
            time.sleep(3)
            bookObj.classTravelOption().click()
            time.sleep(2)
            bookObj.adultTktsOption().click()
            time.sleep(2)
            bookObj.childTktsOption().click()
            time.sleep(2)
            bookObj.applyTktsOption().click()
            time.sleep(2)
            bookObj.searchFlightOption().click()
            time.sleep(5)
            bookObj.adPopupOption().click()
            time.sleep(5)
            self.takescreenshot(self.driver)
        except Exception as EX:
            logs.error("Execption handling",EX)
