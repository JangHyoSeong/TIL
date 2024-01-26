import json
from pprint import pprint


def book_info(book, categories):

    categoryInput = []

    for data in categories:
        if data.get('id') in book.get('categoryId'):
            categoryInput.append(data.get('name'))

    new_data = {

        'id' : book.get('id'),
        'title' : book.get('title'),
        'author' : book.get('author'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover' : book.get('cover'),
        'categoryId' : book.get('categoryId'),
        'categoryName' : categoryInput
    }

    return new_data
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다. 
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
