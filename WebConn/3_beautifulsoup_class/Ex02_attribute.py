from bs4 import BeautifulSoup

html = """
    <html>
        <body>
            <ul>
                <li><a href='http://www.naver.com'>네이브</a></li>
                <li><a href='http://www.daum.net'>다아음</a></li>
            </ul>
        </body>
    </html>
"""

''' 리스트(li)목록의 내용과 해당 경로를 추출하기
    속성추출 : attrs['속성명']

    [출력결과]
    네이브 : http://www.naver.com
    다아음 : http://www.daum.net
'''
soup = BeautifulSoup(html,'html.parser')

liTags=soup.find_all('a')

print(liTags[0].text)
print(liTags[1].text)
print(liTags[0].attrs['href'])
print(liTags[1].attrs['href'])
print(liTags[0].text,":",liTags[0].attrs['href'])
print(liTags[1].text,":",liTags[1].attrs['href'])

print('---'*50)

for a in liTags:
    print(a.text, ":",a.attrs['href'])

