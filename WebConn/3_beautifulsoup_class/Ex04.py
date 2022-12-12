from urllib import request
from bs4 import BeautifulSoup
from urllib import  parse
from urllib.parse import quote_plus

html = request.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")

soup = BeautifulSoup(html,'html.parser')

# green = soup.select(".green")
# for a in green:
#     print(a.text)

#--------------------------------------------------
html2 = request.urlopen("http://www.pythonscraping.com/pages/page3.html")
soup2 = BeautifulSoup(html2,'html.parser')

gift = soup2.select("#giftList .gift")
# for a in gift:
#     print(a.select_one("td:nth-child(1)").text.strip(),":",a.select_one("td:nth-child(3)").text.strip())
#     # --------------------------------------------------
html3 = request.urlopen("https://wikidocs.net/")
soup3 = BeautifulSoup(html3,"html.parser")
baseUrl = "https://wikidocs.net/"

book = soup3.select(".media")
for a in book:
    print(a.select_one('.book-subject').text,":",a.select_one('.menu_link').text)
    imgPath = a.select_one('.book-image').attrs['src']

    imgpath1 = parse.urljoin(baseUrl,imgPath)
    #print(imgpath1)
    bookName = a.select_one('.book-subject').text
    imgpath2 = quote_plus(imgpath1,safe="://")
    request.urlretrieve(imgpath2,'imgs/'+bookName+'.jpg')