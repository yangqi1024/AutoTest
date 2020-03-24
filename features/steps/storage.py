import unittest
import os
from appium import webdriver
from time import sleep


class StorageManager(unittest.TestCase):

    def setUp(self):
        dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps[
            'app'] = dir_path + '/apps/android.apk'
        desired_caps['appPackage'] = 'com.itpiggy.adddemo'
        desired_caps['appActivity'] = '.MainActivity'
        desired_caps['noReset'] = True
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def getDriver(self):
        sleep(0.5)
        return self.dr
