import sys
sys.stdin = open('input.txt')

def calcMinTime(rooms):

    time = 0
    
    for room, student in rooms.items():
        time = max(time, len(student))

    return time




T = int(input())

for testcase in range(1, T+1):

    N = int(input())

    move = [list(map(int, input().split())) for _ in range(N)]
    rooms = {room: [] for room in range(1, 401)}

    for i in range(N):
        start, end = move[i]
        rooms[start].append(end)
        rooms[end].append(start)

    time = calcMinTime(rooms)


    print(f'#{testcase} {time}')