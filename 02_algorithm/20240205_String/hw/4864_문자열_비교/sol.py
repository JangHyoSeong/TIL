import sys
sys.stdin = open('input.txt')

T = int(input())

for testcase in range(1, T+1):
    short_str = str(input())
    long_str = str(input())


    short_len = len(short_str)
    long_len = len(long_str)

    
    for i in range(long_len - short_len + 1):
        temp = []
        for j in range(short_len):
            temp.append(short_str[j])

        if ''.join(temp) == long_str[i:i+short_len]:
            print(f'#{testcase} 1')
            break
    else:
        print(f'#{testcase} 0')