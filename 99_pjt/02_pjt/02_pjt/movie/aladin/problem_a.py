import requests
import json

def author_works():

    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': '',
        'Query' : '파울로 코엘료',
        'QueryType': 'Author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()
    book_list = []
    
    for book in response['item']:
        book_list.append(book['title'])

    return book_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(author_works())
