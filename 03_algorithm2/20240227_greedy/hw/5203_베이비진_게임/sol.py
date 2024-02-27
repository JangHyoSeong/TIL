import sys
sys.stdin = open('input.txt')

def babygin(player):
    # 베이비진 검사하는 함수
    # 리스트를 복사해옴
    arr = player[:]

    # run, triplet 개수를 세는 변수
    count = 0

    # 카운트 배열을 순회
    idx = 0
    while idx < 10:

        # 한 숫자가 3개이상이라면
        # count += 1
        if arr[idx] >= 3:
            count += 1
            arr[idx] -= 3
            continue

        # 범위를 벗어나지 않는 선에서 3숫자가 연속으로 있다면
        # connt += 1
        if idx <= 7:
            if arr[idx] >= 1 and arr[idx+1] >= 1 and arr[idx+2] >= 1:
                count += 1
                for i in range(3):
                    arr[idx+i] -= 1
                continue
        idx += 1

    return count


T = int(input())

for testcase in range(1, T+1):
    cards = list(map(int, input().split()))

    # 카운트 배열 선언
    result = 0
    player_1 = [0] * 10
    player_2 = [0] * 10

    for i in range(0, 12, 2):

        # 배열에 값 입력
        player_1[cards[i]] += 1
        player_2[cards[i+1]] += 1

        # 베이비진 결과
        result_1 = babygin(player_1)
        if result_1:
            result = 1
            break
        
        result_2 = babygin(player_2)

        if result_1 > result_2:
            result = 1
            break
        elif result_1 < result_2:
            result = 2
            break

    
    print(f'#{testcase} {result}')