import queue
import sys

sys.stdin = open('input.txt')

T = 10
for testcase in range(1, T+1):
    tc = int(input())
    numbers = list(map(int, input().split()))

    q = queue.Queue()

    for num in numbers:
        q.put(num)

    i = 1
    while True:
        temp_num = q.get() - i
        if temp_num <= 0:
            temp_num = 0
            q.put(temp_num)
            break
        else:
            q.put(temp_num)

        i += 1
        if i == 6:
            i = 1
    result = ' '.join(str(q.queue[i]) for i in range(q.qsize()))
    print(f'#{testcase} {result}')         
