import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):

    # 배열의 크기, 파리채의 크기를 입력받음
    arr_size, fly_size = map(int, input().split())

    # 파리의 2차원 리스트를 입력받음
    fly = [list(map(int, input().split())) for _ in range(arr_size)]
    
    max_kill = 0

    # 2중 for문을 통해 2차원 리스트를 순회함
    for i in range(arr_size - fly_size + 1):
        for j in range(arr_size- fly_size + 1):
            temp_kill = 0

            # 2중 for문 내에, 파리채의 크기만큼 또 다시 순회함
            for k in range(i, i + fly_size):
                for l in range(j, j + fly_size):
                    temp_kill += fly[k][l]
                    
            # 파리채의 크기 안에 있는 파리들의 합이, 기존에 구했던 최대값보다 크면 갱신
            if temp_kill > max_kill:
                max_kill = temp_kill
    print(f'#{testcase} {max_kill}')