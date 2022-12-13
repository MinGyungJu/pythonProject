from selenium import  webdriver
from bs4 import BeautifulSoup

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdriver/chromedriver.exe')
driver.implicitly_wait(3)
# 2. 페이지 접근
driver.get('https://pelicana.co.kr/store/stroe_search.html')
html = driver.page_source
#print(html)

#추출 시작
soup = BeautifulSoup(html,'html.parser')
name = soup.select('.table tr>td:nth-child(1)')
#print(name)
tell = soup.select('.table tr>td:nth-child(3)')
#print(tell)

for name, tell in zip(name, tell):
    print(name.text, tell.text)