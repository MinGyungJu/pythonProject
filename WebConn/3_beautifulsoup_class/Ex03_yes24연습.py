

from bs4 import BeautifulSoup
from urllib import request

# 교보문고 > '파이썬' 검색 > 국내도서
html = request.urlopen("http://www.yes24.com/Product/Search?domain=ALL&query=python")

soup = BeautifulSoup(html,'html.parser')

#[1]
infos = soup.select('#yesSchList .gd_name')
# for info in infos:
#     print(info.text)
#
# print(len(infos), '권이 검색되었습니다')

#[2]
imgUrl = soup.select("#yesSchList div.itemUnit img")
# print(imgUrls)
for i in imgUrl:
    # print(i.attrs["alt"],":",i.attrs["src"])
    imgPath = imgUrl.attrs['data-original']
    bookName = imgUrl.attrs['alt'].strip().replace('/','_')
    print(bookName,imgPath)
    request.urlretrieve(imgPath, 'imgs/'+bookName+'.jpg')