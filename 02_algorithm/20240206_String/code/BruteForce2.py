def BruteForce(pattern, text, M, N):
    for i in range(N-M+1):
        for j in range(M):
            if text[i+j] != pattern[j]:     # 불일치하면 다음 시작위치로 이동
                break
        else:       # 불일치 하지 않았으면 찾은것, return으로 위치를 반환
            return i
    
    return -1



T = int(input())
for testcase in range(1, T+1):
    pattern = input()
    text = input()
    M = len(pattern)
    N = len(text)

    print(BruteForce(pattern, text, M, N))