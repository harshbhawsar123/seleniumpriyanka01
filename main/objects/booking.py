from selenium.webdriver.common.by import By


class BookingPage:
    driver=''
    def __init__(self,driver):
        self.driver=driver

    fromButton = (By.XPATH,"//span[text()='From']")
    fromInput=(By.XPATH,"//input[@placeholder='From']")
    classTravel = (By.XPATH, "//span[@class='lbl_input appendBottom5']")
    adultTkts = (By.XPATH, "//div[@class='travellers gbTravellers']//li[text()='2']")
    childTkts = (By.XPATH, "//div[@class='makeFlex column childCounter']//li[text()='1']")
    applyTkts = (By.XPATH, "//button[text()='APPLY']")
    searchFlight = (By.XPATH, "//a[text()='Search']")
    adPopup = (By.XPATH, "//button[text()='OKAY, GOT IT!']")
    toButton = (By.ID, "toCity")
    toInput = (By.XPATH, "//input[@placeholder='To']")
    toCity = (By.XPATH, "//div[@class='calc60']//p[contains(text(),'Chandigarh')]")
    nextBtn=(By.CLASS_NAME,"DayPicker-NavButton--next")
    datesChoices=(By.XPATH,"//div[@class='dateInnerCell']")
    fromCity = (By.XPATH, "//div[@class='calc60']//p[contains(text(),'Pune')]")

    def fromCityOption(self):
        return self.driver.find_element(*BookingPage.fromCity)

    def dateChoicesOption(self):
        return self.driver.find_elements(*BookingPage.datesChoices)

    def nextBtnOption(self):
        return self.driver.find_element(*BookingPage.nextBtn)

    def fromButtonOption(self):
        return self.driver.find_element(*BookingPage.fromButton)
    def fromInputOption(self):
        return self.driver.find_element(*BookingPage.fromInput)

    def classTravelOption(self):
        return self.driver.find_element(*BookingPage.classTravel)

    def adultTktsOption(self):
        return self.driver.find_element(*BookingPage.adultTkts)

    def childTktsOption(self):
        return self.driver.find_element(*BookingPage.childTkts)

    def applyTktsOption(self):
        return self.driver.find_element(*BookingPage.applyTkts)

    def searchFlightOption(self):
        return self.driver.find_element(*BookingPage.searchFlight)

    def adPopupOption(self):
        return self.driver.find_element(*BookingPage.adPopup)

    def toButtonOption(self):
        return self.driver.find_element(*BookingPage.toButton)

    def toInputOption(self):
        return self.driver.find_element(*BookingPage.toInput)

    def toCityOption(self):
        return self.driver.find_element(*BookingPage.toCity)


def booking():
    return None