import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    N, M= map(int,input().split())

    flies = [list(map(int, input().split())) for _ in range(N)]

    # 최대값
    max_kill = 0

    # 2차원 배열을 모두 순회
    for i in range(N):
        for j in range(N):
            # i,j 값에서 범위내 모든 합
            temp_kill = 0
            
            # 다이아몬드 모양을 범위로 잡기위해 다음과 같이 범위설정
            # M=3 이라면 -1, 0, 1이 됨
            # M=7 이라면 -3, -2, -1, 0, 1, 2, 3이 됨
            for x in range(-(M//2), M//2+1):

                # 다이아몬드 모양을 생각한다면
                # 다이아몬드의 맨 윗줄의 개수는 1 그다음은 3, ... M까지 증가하고 다시 1까지 줄어듬
                # M = 7인 경우라면 1, 3, 5, 7, 5, 3, 1의 형식
                # 따라서 범위를 설정하기 위해 gap이라는 변수를 다음과 같이 설정
                gap = M - 2 * abs(x)

                # 이렇게 한다면 x, y를 통해 다이아몬드 모양의 범위 설정 가능
                for y in range(-(gap//2), gap//2+1):

                    # 만약 인덱스 범위 내라면
                    if i+x >= 0 and i+x < N and j+y >= 0 and j+y < N:
                        # 합계에 더함
                        temp_kill += flies[i+x][j+y]
                        
            # 최대값 비교
            if max_kill < temp_kill:
                max_kill = temp_kill


    print(f'#{testcase} {max_kill}')