import json


def new_books(books):

    book2023 = []

    for book in books:
        
        book_json = open(f'data/books/{book.get("id")}.json', encoding='utf-8')
        bookTemp = json.load(book_json)

        if bookTemp.get('pubDate')[:4] == "2023":
            book2023.append(book.get('title'))

        
    return book2023


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(new_books(books_list))
