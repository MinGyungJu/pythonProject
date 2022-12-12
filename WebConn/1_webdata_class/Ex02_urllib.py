
# 내장모듈이용

from urllib import request

url = 'http://www.google.com'
site = request.urlopen(url)

page = site.read()
print(page)
print('*'*50)

print(site.status)
print('*'*50)

headers = site.getheaders()
print(headers)
print('*'*50)

for x,y in headers:
    print(x,":",y)