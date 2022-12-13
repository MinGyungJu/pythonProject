from selenium import  webdriver

urs = 'qpw3'
pwd = 'rormtlssk1!'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)
# 2. 페이지 접근
driver.get('https://fifaonline4.nexon.com/main/index/')

btn = driver.find_element_by_class_name('gnbLogin')
btn.click()
driver.implicitly_wait(2)

txtNexonID = driver.find_element_by_id('txtNexonID')
txtPWD = driver.find_element_by_id('txtPWD')

txtNexonID.send_keys(urs)
txtPWD.send_keys(pwd)

btn = driver.find_element_by_class_name('button01')
btn.click()
driver.implicitly_wait(2)