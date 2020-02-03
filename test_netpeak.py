import  allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select


@allure.title('')
def test_netpeak():
    driver = WebDriver(executable_path='C://Users/Ion/PycharmProjects/selenium/chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(10)

    with allure.step('Open the main page Netpeak'):
        driver.get('https://netpeak.ua/')
    with allure.step('Go to page "Работа в Netpeak" pressing a button "Карьера"'):
        driver.find_element_by_xpath('//li[@class="blog"]').click()
    with allure.step('Go to the questionnaire filling page pressing a button "Я хочу работать в Netpeak"'):
        driver.find_element_by_xpath('//a[@class="btn green-btn"]').click()

    with allure.step('Upload file with invalid format in block and chek error'):
        element = driver.find_element_by_xpath('//input[@name="up_file"]')
        element.send_keys("C://Users/Ion/PycharmProjects/selenium/foto.png")


    #t = driver.find_element_by_xpath('//div[@id="up_file_name"]/label').text
    #assert t == "Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf)."

    #Fill in the form with random data

    with allure.step('Region and role'):
        City = Select(driver.find_element_by_xpath('//select[@id="cityChoice"]')).select_by_value('1')
        Vacansy = Select(driver.find_element_by_xpath('//select[@id="vacChoice"]')).select_by_value('automation-qa-netpeak-group-netpeak-group')
        Country = Select(driver.find_element_by_xpath('//select[@id="myCountry"]')).select_by_value('UA')
        MyCity = Select(driver.find_element_by_xpath('//select[@id="myCity"]')).select_by_value('2')
        MoveAgreement = driver.find_element_by_xpath('//input[@name="move-agreement"]').click()

    with allure.step('Personal data'):
        Firstname = driver.find_element_by_xpath('//input[@id="inputName"]').send_keys('Ivan')
        Lastname = driver.find_element_by_xpath('//input[@id="inputLastname"]').send_keys('Ivanov')
        Bd = Select(driver.find_element_by_xpath('//select[@name="bd"]')).select_by_value('05')
        Bm = Select(driver.find_element_by_xpath('//select[@name="bm"]')).select_by_value('03')
        By = Select(driver.find_element_by_xpath('//select[@name="by"]')).select_by_value('1990')
        Email =driver.find_element_by_xpath('//input[@id="inputEmail"]').send_keys('asgvasdva@gmail.com')
        Number = driver.find_element_by_xpath('//input[@id="inputPhone"]').send_keys('0969355640')

    with allure.step('Salary expectations'):
        Salary = driver.find_element_by_xpath('//input[@id="inputSalary"]').send_keys('9999')

    with allure.step('SKnowledge of foreign languages'):
        Languages = Select(driver.find_element_by_xpath('//div[@class="lang-box"]/div/div[1]/select')).select_by_value('5')
        Nivel = Select(driver.find_element_by_xpath('//div[@class="lang-box"]/div/div[2]/select')).select_by_value('1')

    with allure.step('Questionnaire questions'):
        Question1 = driver.find_element_by_xpath('//div[@id="form"]/div[1]/input').send_keys('https://www.facebook.com/arfha')
        Question2 = driver.find_element_by_xpath('//div[@id="form"]/div[2]/input').send_keys('https://www.telegram.com/arga')
        Question3 = driver.find_element_by_xpath('//div[@id="form"]/div[3]/textarea').send_keys('skyktrsartj')
        Question4 = driver.find_element_by_xpath('//div[@id="form"]/div[4]/textarea').send_keys('jstrjhstrtjs')
        Question5 = driver.find_element_by_xpath('//div[@id="form"]/div[5]/textarea').send_keys('srjrsksrtkmk')

    Rules = driver.find_element_by_xpath('//input[@name="agree_rules"]').click()

    with allure.step('Click the send resume button'):
        Button = driver.find_element_by_xpath('//button[@id="submit"]').click()

    with allure.step('Check that the message on the current page is highlighted in red'):
        Message_color = driver.find_element_by_xpath('//p[@class="warning-fields help-block"]').value_of_css_property('color')
        assert Message_color == 'rgba(255, 0, 0, 1)'

    with allure.step('Click on the logo to go to the main page and make sure that the desired page has opened'):
        Click_logo = driver.find_element_by_xpath('//div[@class="logo-block"]').click()
        assert driver.title == 'Раскрутка сайта, продвижение сайтов: Netpeak Украина — интернет-маркетинг для бизнеса'



