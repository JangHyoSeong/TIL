import requests
from pprint import pprint


def ebook_list(title):

    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': '',
        'Query' : title,
        'QueryType': 'Title',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'eBook',
        'output': 'js',
        'Version': '20131101',
    }
    
    # print(requests.get(URL, params=params).url)
    response = requests.get(URL, params=params).json()
    result = []
    try:
        for paper_book in response['item'][0]['subInfo']['paperBookList']:
            book = {}
            if response['item'][0]['priceSales'] * 0.9 <= paper_book['priceSales']:
                book['itemId'] = paper_book['itemId']
                book['isbn'] = paper_book['isbn']
                book['priceSales'] = paper_book['priceSales']
                book['link'] = paper_book['link']
                result.append(book)
    except IndexError:
        return None


    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
