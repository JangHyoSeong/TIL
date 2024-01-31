import sys

sys.stdin = open('input.txt')

t = int(input())
 
for i in range(t) :
    n,k = map(int,input().split())
    test_list = []
    for _ in range(n) :
        test_list.append((input().split()))
     
    output = 0 
    # x 열 확인
    for arr in test_list :
        output += list(map(len,"".join(arr).split("0"))).count(k)
    
    for x in range(n) :
        char = ""
        for y in range(n) :
            char += test_list[y][x] 
        output += list(map(len,char.split("0"))).count(k)
        
    print(f"#{i+1} {output}")