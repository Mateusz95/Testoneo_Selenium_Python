import unittest
from selenium import webdriver

class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='D:\TestyAutomatyczne\chromedriver.exe')
