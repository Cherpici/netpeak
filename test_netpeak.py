# -*- coding: utf-8 -*-
import  allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
import unittest

@allure.title('Test for Netpeak')
class Netpeak(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(executable_path='C://Users/Ion/PycharmProjects/selenium/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_steps1(self):
        with allure.step('Open the main page Netpeak'):
            self.driver.get('https://netpeak.ua/')

    def test_steps2(self):
        with allure.step('Go to page "Работа в Netpeak" pressing a button "Карьера"'):
            self.driver.find_element_by_xpath('//li[@class="blog"]').click()

    def test_steps3(self):
        with allure.step('Go to the questionnaire filling page pressing a button "Я хочу работать в Netpeak"'):
            self.driver.find_element_by_xpath('//a[@class="btn green-btn"]').click()

    def test_steps4(self):
        with allure.step('Upload file with invalid format in block and chek error'):
            element = self.driver.find_element_by_xpath('//input[@name="up_file"]')
            element.send_keys("C://Users/Ion/PycharmProjects/selenium/foto.png")

            t = self.driver.find_element_by_xpath('//div[@id="up_file_name"]/label').text
            assert t == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."

    #Fill in the form with random data
    def test_steps5(self):
        with allure.step('Personal data'):
            Firstname = self.driver.find_element_by_xpath('//input[@id="inputName"]').send_keys('Ivan')
            Lastname = self.driver.find_element_by_xpath('//input[@id="inputLastname"]').send_keys('Ivanov')
            Bd = Select(self.driver.find_element_by_xpath('//select[@name="bd"]')).select_by_value('05')
            Bm = Select(self.driver.find_element_by_xpath('//select[@name="bm"]')).select_by_value('03')
            By = Select(self.driver.find_element_by_xpath('//select[@name="by"]')).select_by_value('1990')
            Email =self.driver.find_element_by_xpath('//input[@id="inputEmail"]').send_keys('asgvasdva@gmail.com')
            Number = self.driver.find_element_by_xpath('//input[@id="inputPhone"]').send_keys('0969355640')

    def test_steps6(self):
        with allure.step('Click the send resume button'):
            Button = self.driver.find_element_by_xpath('//button[@id="submit"]').click()

    def test_steps7(self):
        with allure.step('Check that the message on the current page is highlighted in red'):
            Message_color = self.driver.find_element_by_xpath('//p[@class="warning-fields help-block"]').value_of_css_property('color')
            assert Message_color == 'rgba(255, 0, 0, 1)'

    def test_steps8(self):
        with allure.step('Click on the logo to go to the main page and make sure that the desired page has opened'):
            Click_logo = self.driver.find_element_by_xpath('//div[@class="logo-block"]').click()
            assert self.driver.title == 'Раскрутка сайта, продвижение сайтов: Netpeak Украина — интернет-маркетинг для бизнеса'

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()



