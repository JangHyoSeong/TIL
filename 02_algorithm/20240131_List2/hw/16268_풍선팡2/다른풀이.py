import sys

sys.stdin = open('input.txt')

# 테스트 케이스 수 입력받기
T = int(input())
 
# 각각의 테스트 케이스 별로 입력값 받기
for t in range(1, T + 1):
    N, M = map(int, input().split())
    balloons = [list(map(int, input().split())) for _ in range(N)]
 
    # 상하좌우로 순회할 때 활용할 dx값 리스트 설정
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
 
    # 꽃가루 합계 정보를 담을 리스트 설정
    flower_list = []
     
    # 모든 좌표를 순회하며 좌표 본인의 꽃가루 값에
    for i in range(N):
        for j in range(M):
            flowers = balloons[i][j]
             
            # 상하좌우 좌표의 꽃가루 값 더하기
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                 
                # 단, 주어진 범위를 벗어나지 않은 좌표에 대해서만 더한다.
                if ni in range(N) and nj in range(M):
                    flowers += balloons[ni][nj]
             
            # 해당 좌표와 상하좌우의 좌표의 꽃가루를 전부 합하면
            # 위에서 미리 설정해놓은 리스트에 꽃가루 합계 정보 담기
            flower_list.append(flowers)
 
    # 결과 출력
    print(f'#{t} {max(flower_list)}')
