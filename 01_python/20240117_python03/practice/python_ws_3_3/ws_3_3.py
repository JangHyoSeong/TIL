def rental_book(name, number):
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다')

number_of_book = 100

def decrease_book(decreaseNum):
    global number_of_book
    number_of_book -= decreaseNum
    print('남은 책의 수 : ', number_of_book)
    return number_of_book


rental_book('홍길동', 3)