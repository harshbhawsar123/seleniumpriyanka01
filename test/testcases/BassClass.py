import logging
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("setup")
class BassClass:
    def get_logger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('../../logs/logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)# File handler object
        logger.setLevel(logging.DEBUG)
        return logger

    def takescreenshot(self, driver):
        driver.save_screenshot("..//..//screenshot//result.png")
