import requests
from bs4 import BeautifulSoup

# beautifulSoup는 의미있는 response로 바꿔줌
url = "http://www.naver.com"
response = requests.get(url)

# response.text가 str타입이라는 뜻
# class 'str'
print(type(response.text))

# response.txt를 하나하나 떼서 beautifulsoup통에 넣음
# class 'bs4.BeautifulSoup'
print(type(BeautifulSoup(response.text, 'html.parser')))
