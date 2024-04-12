import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/tag/love/'
# 1. 다운로드 - url을 이용해서 HTML이 담긴 자료를 받아와야 함
response = requests.get(url)
html_text = response.text
# print(html_text)

# html_text 는 문자열 타입
# 문자열 파싱은 코드로 짜기 매우 복잡하다 -> BeautifulSoup 라이브러리를 사용
soup = BeautifulSoup(html_text, 'html.parser')
# print(soup)
# print(type(soup))

# find : 첫 번째 해당 요소를 찾음 (a tag)
test = soup.find('a')
# print(test) 

# title 태그를 찾음
title = soup.find('title')
# print(title)

# find_all : 해당 태그를 가진 모든 요소를 검색
# 리스트로 반환
a_tags = soup.find_all('a')
# print(a_tags)

# select_one : CSS 선택자를 사용하여 요소를 검색. 모든 일치하는 요소를 리스트로 반환
# class를 통한 검색을 하는 것이 옳다
word = soup.select_one('.text')
print(f'첫 번째 글 = {word}')

# select
words = soup.select('.text')  
for w in words:
    print(f'글 : {w.text}')