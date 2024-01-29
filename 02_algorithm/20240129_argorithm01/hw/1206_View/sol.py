T = 10

for testcase in range(1, T+1):
    width = int(input())
    buildings = list(map(int, input().split()))

    view_point = 0

    for height in range(2, width -2):
        max_height = max(buildings[height - 2], buildings[height - 1], buildings[height + 1], buildings[height + 2])
        if buildings[height] >= max_height:
             view_point += buildings[height] - max_height
    
    print(f'#{testcase} {view_point}')
            