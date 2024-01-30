import sys

sys.stdin = open('input.txt')

T = 10

for testcase in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 상자를 옮기는 횟수만큼 반복
    for i in range(dump):
        # 최대값을 1 줄이고 최소값을 1 증가
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

    print(f'#{testcase} {max(boxes)-min(boxes)}')