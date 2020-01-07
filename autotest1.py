import unittest

from selenium import webdriver


class MainTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path='D:\TestyAutomatyczne\chromedriver.exe')

    def test_header_login_page(self):
        driver = self.driver
        url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        driver.get(url)
        header_check = driver.find_element_by_xpath('//*[@id="main"]/header/h1')
        header_text = header_check.text
        expected_header = 'Log in to your account'
        self.assertEqual(expected_header, header_text, f'Expected different header on page {url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
