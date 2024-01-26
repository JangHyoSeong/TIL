import requests
from pprint import pprint


def author_other_works(title):

    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': '',
        'Query' : title,
        'QueryType': 'Title',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()

    try:
        author = response['item'][0]['author']
    except IndexError:
        return None
    
    idx = author.find('(지은이)')
    author = author[:idx-1]    

    params = {
    'ttbkey': 'ttbwkdgytmd2001230001',
    'Query' : author,
    'QueryType': 'Author',
    'MaxResults': 20,
    'start': 1,
    'SearchTarget': 'Book',
    'output': 'js',
    'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()

    result = []

    for book in response['item']:
        result.append(book)
    
    # 중복 제거를 위한 set
    unique = set()

    for book in result:
        isbn = book['isbn']
        if isbn not in unique:
            unique.add(book['title'])
            
    result = list(unique)

    return result[:5]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
