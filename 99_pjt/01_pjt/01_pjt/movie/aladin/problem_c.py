import json
from pprint import pprint


def books_info(books, categories):

    booksList = []

    for book in books:
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
        booksList.append(new_data)

    return booksList


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
