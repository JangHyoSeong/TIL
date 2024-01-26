import json


def sorted_cs_books_by_price(books, categories):

    bookList = []
    for data in categories:

        if data.get('name') == '컴퓨터 공학':
            computerScienceData = data
            break

    for book in books:

        book_json = open(f'data/books/{book.get("id")}.json', encoding='utf-8')
        bookTemp = json.load(book_json)
        
        if computerScienceData.get('id') in book.get('categoryId'):
            bookList.append(book)

    sortedBookList = sorted(bookList, key = lambda x: x.get('priceSales',0), reverse=True) 
    sortedTitle = [book.get('title') for book in sortedBookList]

    return sortedTitle




# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books, categories_list))
