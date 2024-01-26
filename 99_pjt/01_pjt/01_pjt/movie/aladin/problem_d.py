import json


def best_book(books):
    max = 0

    for book in books:
        
        book_json = open(f'data/books/{book.get("id")}.json', encoding='utf-8')
        bookTemp = json.load(book_json)

        if bookTemp.get('customerReviewRank') > max:
            max = bookTemp.get('customerReviewRank')
            bestBook = book.get('title')
        
    return bestBook





# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books_list = json.load(books_json)

    print(best_book(books_list))
