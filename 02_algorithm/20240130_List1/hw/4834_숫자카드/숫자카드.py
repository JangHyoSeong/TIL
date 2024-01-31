import sys

sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    num_of_cards = int(input())     # 카드의 장수
    str_cards = str(input())          # 카드 입력
    # 어떤 숫자가 몇번 나오는지 카운트하기 위한 리스트
    card_count = [0] * 10

    # 카드가 0으로 시작하는 경우 처리
    i = 0
    while str_cards[i] == '0':
        card_count[0] += 1
        i += 1

    cards = int(str_cards)

    # 카드의 1의 자리의 숫자가 몇번 나오는지 세서 card_list 를 갱신함
    while cards > 0:
        card_count[cards % 10] += 1
        cards //= 10

    max_card = max(card_count)  # 가장 많이 나온 숫자가 몇 번 나왔는지 저장
    max_card_num = 0    # 가장 많이 나온 숫자가 무엇인지 찾기 위한 변수

    for i in range(len(card_count)):
        # 가장 많이 나온 숫자를 찾기 위함.
        # 가장 많이 나온 숫자가 두개 이상이라면 더 큰 숫자로 갱신됨
        if card_count[i] == max_card:
            max_card_num = i


    print(f'#{testcase} {max_card_num} {max_card}')