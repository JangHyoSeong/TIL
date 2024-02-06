import sys
sys.stdin = open('input.txt')

# def f():
#     T = int(input())

#     str_map = [list(map(str, input())) for _ in range(100)]
#     for k in range(100, 0, -1):
#         for l in range(k//2):
#             for i in range(100):
#                 for j in range(100-k):
#                     if str_map[i][j+l] != str_map[i][j+k-l-1]:
#                         break
#                 else:
#                     return k
            
#             for i in range(100-k):
#                 for j in range(100):
#                     if str_map[i+l][j] != str_map[i+k-l-1][j]:
#                         break
#                 else:
#                     return k
                
def f():
    T = int(input())

    length_max = 0
    str_map = [list(map(str, input())) for _ in range(100)]
    for k in range(100, 0, -1):
        for i in range(100):
            for j in range(101-k):
                for l in range(k//2):
                    if str_map[i][j+l] != str_map[i][j+k-l-1]:
                        break
                else:
                    if length_max < k:
                        length_max = k

    for k in range(100, 0, -1): 
        for i in range(101-k):
            for j in range(100):
                for l in range(k//2):
                    if str_map[i+l][j] != str_map[i+k-l-1][j]:
                        break
                else:
                    if length_max < k:
                        length_max = k
                        break
    return length_max



for testcase in range(1, 11):

    result = f()

    print(f'#{testcase} {result}')