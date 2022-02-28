from bs4 import BeautifulSoup
import requests

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#daum.html이라는 파일 생성, 열기
file = open("daum.html", "w")
#response.text를 daum.html에 쓰기
file.write(response.text)
#daum.html 닫기
file.close()

print(soup.title)
print(soup.title.string)
print(soup.span)
print(soup.findAll('span'))
