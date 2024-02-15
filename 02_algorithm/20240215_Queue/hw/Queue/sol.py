import sys
from collections import deque
sys.stdin = open('input.txt')

# 사탕 개수
candy = 20

# 사람이 몇명인지 세기 위한 변수
count = 1

# 사탕 받는 대기줄을 deque로 구현
wait = deque()

# 첫번째 사람.  # human[0] : 사람 번호, human[1] : 받을 사탕의 개수
human = [count, count]

# 줄에 사람을 추가함(현재 1번 1명)
wait.append(human)


# 사탕이 모두 떨어질 때까지 반복
while candy > 0:

    # 사탕받을 사람을 왼쪽에서 pop (queue의 형식)
    사탕받은사람 = wait.popleft()

    # 사탕을 나눠줌
    candy -= 사탕받은사람[1]

    # 사탕을 받을때마다 다음에 받는 사탕의 개수가 늘어나기 때문에 human[1]을 1 더해줌
    사탕받은사람[1] += 1

    # 사탕을 받으면 받은 즉시 다시 뒤로가서 줄을 섬 : append를 통해 wait의 맨 뒤에 값을 추가
    wait.append(사탕받은사람)

    # 사람이 한명 사탕을 받을 때마다 번호가 늘어남
    # 1번이 사탕을 받고 나간다면 2번 사람이 생기는 방식
    count += 1
    human = [count, count]

    # 새로 생긴 사람을 줄에 추가
    wait.append(human)

print(f'{사탕받은사람[0]}번 사람이 사탕{사탕받은사람[1]}개를 받을 때 사탕이 모두 소모')