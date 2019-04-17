from selenium import webdriver
import unittest

openbrowser = webdriver.Chrome()
openbrowser.maximize_window()

class MyFunc(unittest.Testcase):
    def setUp(self):
        self.openbrowser = webdriver.Chrome()
        self.openbrowser.maximize_window()




