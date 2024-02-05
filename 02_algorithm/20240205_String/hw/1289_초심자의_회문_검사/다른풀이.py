T = int(input())
 
for tc in range(1,T+1):
    word = input()
    if word == word[::-1]:
        cnt=1
    else:
        cnt=0
    print(f'#{tc} {cnt}')