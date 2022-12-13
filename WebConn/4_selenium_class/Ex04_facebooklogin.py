from selenium import  webdriver

urs = '01027114855'
pwd = 'rormtlssk1!'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)
# 2. 페이지 접근
driver.get('https://www.facebook.com/')

email = driver.find_element_by_id('email')
passwd = driver.find_element_by_id('pass')

email.send_keys(urs)
passwd.send_keys(pwd)

btn = driver.find_element_by_name('login')
btn.click()
driver.implicitly_wait(2)