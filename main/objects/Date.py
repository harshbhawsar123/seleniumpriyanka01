from distutils.command.install import value

from selenium.webdriver.common.by import By

#import selenium.By



class Date:
    driver = ''

    def __init__(self, driver):
        self.driver = driver

    date1=((By.CLASS_NAME, "calc60")[0])
    date2=(By.CLASS_NAME, "calc60")[0]
