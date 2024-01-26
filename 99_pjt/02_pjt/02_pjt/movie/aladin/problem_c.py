import requests
from pprint import pprint


def bestseller_book():

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

    book_list = response['item']
    book_list.sort(key=lambda x: x['salesPoint'], reverse=True)

    top5 = []
    for i in range(5):
        top5.append(book_list[i]['title'])
    return top5
        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
