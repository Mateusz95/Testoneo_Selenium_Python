import time
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

    def test_login(self):
        driver = self.driver
        url = 'https://autodemo.testoneo.com/en/login?back=my-account'
        driver.get(url)
        login_form_input = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[1]/div[1]/input')
        login_form_input.clear()
        login_text = 'johnyczorny@gmail.com'
        login_form_input.send_keys(login_text)
        password_form_input = driver.find_element_by_xpath('//*[@id="login-form"]/section/div[2]/div[1]/div/input')
        password_form_input.clear()
        password_text = 'johny123'
        password_form_input.send_keys(password_text)
        signin_button = driver.find_element_by_xpath('//*[@id="submit-login"]')
        signin_button.click()
        time.sleep(2)
        after_login_header = driver.find_element_by_xpath('//*[@id="main"]/header/h1')
        after_login_header_text = after_login_header.text
        expected_after_login_header = 'Your account'
        self.assertEqual(expected_after_login_header, after_login_header_text, f'Expected differ header after login')

    def test_tshirt_product(self):
        driver = self.driver
        url = 'https://autodemo.testoneo.com/en/men/1-1-hummingbird-printed-t-shirt.html'
        driver.get(url)
        expected_product_title = 'HUMMINGBIRD PRINTED T-SHIRT'
        product_title = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/h1')
        product_title_text = product_title.text
        self.assertEqual(expected_product_title, product_title_text, f'Expected product title is differ on page {url}')
        expected_price = '23.52'
        product_price = driver.find_element_by_xpath('//*[@id="main"]/div[1]/div[2]/div[1]/div[2]/div/span[1]')
        product_price_content = product_price.get_attribute('content')
        # print(product_price_content) #check what is inside content attribute
        self.assertEqual(expected_price, product_price_content, f'Price is differ than expected on page {url}')

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
