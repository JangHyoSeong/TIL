list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽',
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기',
]

# 모든 책을 보유 중인지 확인
all_books_owned = all(book in list_of_book for book in rental_book)

# 보유하지 않은 책 목록 출력
not_owned_books = [book for book in rental_book if book not in list_of_book]

# 결과 출력
if not all_books_owned:
    print("보유하지 않은 책이 있습니다:", ', '.join(not_owned_books))
else:
    print("모두 보유하고 있습니다.")