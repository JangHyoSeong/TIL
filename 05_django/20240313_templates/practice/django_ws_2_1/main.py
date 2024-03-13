import requests
import json
from pprint import pprint

API_URL = 'http://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = ''
params = {
    'ttbkey': API_KEY,
    'QueryType': 'ItemNewSpecial',
    'MaxResults': 50,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
}

response = requests.get(API_URL, params=params).json()
book_list = []

for book in response['item']:
    book_dict = {
        '국제 표준 도서 번호' : book['isbn'],
        '저자' : book['author'],
        '제목' : book['title'],
        '출간일' : book['pubDate'],
    }
    book_list.append(book_dict)


pprint(book_list)