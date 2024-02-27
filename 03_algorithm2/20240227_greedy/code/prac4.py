'''
중복순열, 순열 만들기
N개의 주사위를 던져 나올 수 있는 모든 순열 출력
'''

path = []

def dice(x, N, type):
    
    if type == 1:
        if x == N:
            print(path)
            return

        for i in range(1, 7):
            path.append(i)
            dice(x+1, N, type)
            path.pop()

    elif type == 2:
        if x == N:
            print(path)
            return
        
        for i in range(6):
            if visited[i] == True:
                continue
            visited[i] = True
            path.append(i+1)
            dice(x+1, N, type)
            path.pop()
            visited[i] = False

N, type = map(int, input().split())
visited = [False] * 6
dice(0, N, type)

